"""Runs CI's jobs on your machine, so a push isn't how you find out they fail: checks.yml's, and publish.yml's build of
each version it would publish, from the latest upstream data (checks.yml uses the committed symbols.json, so it can pass
while publishing fails). Run it from the repo root, and on Windows from Git Bash, as the steps are bash.

python .github/scripts/local_ci.py         | All of it
python .github/scripts/local_ci.py checks  | Just checks.yml (quicker, easier, better)

The steps are read from the workflow files, so they're always the same as CI's. Each job runs at the same time as the
others, in its own copy of your working tree (without what's gitignored, as a checkout wouldn't have it either). Setting up
the machine (pip install) is left out, and so is anything that isn't a run step, like publishing to PyPI, and the
generated-branch job, which pushes. `pre-commit install` sets it up to run before each push.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import yaml

WORKFLOWS = Path(".github/workflows")
BASH = shutil.which("bash") or "bash"  # Its full path, as otherwise Windows finds WSL's bash before Git's


def copy_working_tree(destination: Path) -> None:
    """Copy the working tree's files, apart from gitignored ones, i.e. what a checkout of it would have."""
    names = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], check=True, capture_output=True, text=True).stdout
    for name in filter(None, names.split("\0")):
        if Path(name).is_file():  # Not ones that are deleted but not committed yet
            (destination / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(name, destination / name)
    subprocess.run(["git", "init", "-q", destination], check=True)  # As a checkout is one, e.g. ruff only uses .gitignore in a repo


def run_job(workflow: str, job: str, variables: dict[str, str] | None = None, name: str | None = None) -> dict[str, str] | None:
    """Run a job's steps in a fresh copy of the repo, stopping at the first that fails, like CI. What the steps wrote to
    $GITHUB_OUTPUT, or None if one failed (and its output is printed)."""
    name = name or job
    steps: list[dict[str, Any]] = yaml.safe_load((WORKFLOWS / workflow).read_text(encoding="utf-8"))["jobs"][job]["steps"]
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as directory:  # Windows can't always delete it straight away
        repo, outputs = Path(directory, "repo"), Path(directory, "outputs.txt")
        copy_working_tree(repo)
        outputs.touch()
        environment = {**os.environ, **(variables or {}), "GITHUB_OUTPUT": outputs.as_posix(), "GITHUB_STEP_SUMMARY": Path(directory, "summary.md").as_posix()}
        for step in steps:
            if "run" not in step or step["run"].startswith("pip install"):
                continue
            print(f"{name}: {step['run'].partition('  # ')[0]}", flush=True)
            result = subprocess.run(
                [BASH, "-c", step["run"]], cwd=repo, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8", errors="replace", check=False,
            )
            if result.returncode:
                print(f"{name} failed:\n{result.stdout}", flush=True)
                return None
        return {key: value for key, _, value in (line.partition("=") for line in outputs.read_text(encoding="utf-8").splitlines())}


def main(arguments: list[str]) -> None:
    if arguments not in ([], ["checks"]):
        sys.exit(__doc__)
    with ThreadPoolExecutor() as pool:
        jobs = {"checks": pool.submit(run_job, "checks.yml", "checks")}
        if not arguments:
            jobs["plan"] = pool.submit(run_job, "publish.yml", "plan")
            plan = jobs["plan"].result() or {"versions": "[]"}
            for version in json.loads(plan["versions"]):
                variables = {"MINECRAFT_VERSION": version, "MCDOC_COMMIT": plan["mcdoc"], "MCMETA_COMMIT": plan["mcmeta"]}  # publish.yml's env, from the plan
                jobs[f"publish {version}"] = pool.submit(run_job, "publish.yml", "publish", variables, f"publish {version}")
        failed = [name for name, job in jobs.items() if job.result() is None]
    if failed:
        sys.exit(f"Failed: {', '.join(failed)}")
    print("All of it passed")


if __name__ == "__main__":
    main(sys.argv[1:])
