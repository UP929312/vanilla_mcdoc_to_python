import subprocess
from pathlib import Path

from pytest import CaptureFixture, MonkeyPatch, raises

import local_ci

WORKFLOW = """
jobs:
  build:
    steps:
      - uses: actions/checkout@v5
      - run: pip install something-ci-needs-but-you-have-already
      - run: echo "greeting=$GREETING" >> "$GITHUB_OUTPUT"
      - run: test -f committed.py && test -f new.py && test ! -f ignored.py
      - run: git check-ignore -q ignored.py  # It's a repo, so tools that use .gitignore still do
  broken:
    steps:
      - run: echo "Oh no" && exit 1
      - run: echo "reached=yes" >> "$GITHUB_OUTPUT"
"""


def make_repo(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    subprocess.run(["git", "init", "-q"], check=True)
    Path(".github/workflows").mkdir(parents=True)
    Path(".github/workflows/ci.yml").write_text(WORKFLOW, encoding="utf-8")
    Path(".gitignore").write_text("ignored.py\n", encoding="utf-8")
    for name in ["committed.py", "new.py", "ignored.py"]:
        Path(name).write_text("", encoding="utf-8")
    subprocess.run(["git", "add", "committed.py"], check=True)


def test_a_job_runs_its_steps_in_a_copy_without_the_ignored_files(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    make_repo(tmp_path, monkeypatch)
    assert local_ci.run_job("ci.yml", "build", {"GREETING": "hi"}) == {"greeting": "hi"}  # The pip install would have failed


def test_a_job_stops_at_the_first_step_that_fails(tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    make_repo(tmp_path, monkeypatch)
    assert local_ci.run_job("ci.yml", "broken") is None
    assert "broken failed:\nOh no" in capsys.readouterr().out


def test_every_version_publish_would_build_is_built(monkeypatch: MonkeyPatch) -> None:
    ran: dict[str, dict[str, str] | None] = {}

    def run_job(workflow: str, job: str, variables: dict[str, str] | None = None, name: str | None = None) -> dict[str, str] | None:
        ran[f"{workflow} {name or job}"] = variables
        if job == "plan":
            return {"versions": '["26.4-snapshot-4", "26.3"]', "mcdoc": "abc", "mcmeta": "def"}
        return None if variables and variables["MINECRAFT_VERSION"] == "26.3" else {}

    monkeypatch.setattr(local_ci, "run_job", run_job)
    with raises(SystemExit, match="^Failed: publish 26.3$"):
        local_ci.main([])
    assert ran == {
        "checks.yml checks": None,
        "publish.yml plan": None,
        "publish.yml publish 26.4-snapshot-4": {"MINECRAFT_VERSION": "26.4-snapshot-4", "MCDOC_COMMIT": "abc", "MCMETA_COMMIT": "def"},
        "publish.yml publish 26.3": {"MINECRAFT_VERSION": "26.3", "MCDOC_COMMIT": "abc", "MCMETA_COMMIT": "def"},
    }

    ran.clear()
    local_ci.main(["checks"])
    assert ran == {"checks.yml checks": None}
