import io
import json
import urllib.error
import zipfile
from pathlib import Path

from pytest import CaptureFixture, MonkeyPatch

import ci


def test_versions_to_build_are_the_newest_releases_plus_any_newer_snapshot() -> None:
    newest_first = ["26.4-snapshot-3", "26.3", "26.3-rc-1", "26.2", "25w46a", "26.1.2", "26.1"]
    assert ci.versions_to_build(newest_first) == ["26.4-snapshot-3", "26.3", "26.2", "26.1.2"]
    assert ci.versions_to_build(newest_first[1:]) == ["26.3", "26.2", "26.1.2"]  # Nothing newer than the newest release


def make_package(directory: Path, version: str, body: str) -> dict[str, bytes]:
    """Write a tiny generated package into directory, and return the files a wheel of it would have."""
    (directory / "vanilla_mcdoc").mkdir(exist_ok=True)
    (directory / "vanilla_mcdoc" / "__init__.py").write_text(f'__version__ = "{version}"\n__mcdoc_commit__ = "abc"\n', encoding="utf-8")
    (directory / "vanilla_mcdoc" / "Thing.py").write_text(body, encoding="utf-8")
    return {f"vanilla_mcdoc/{path.name}": path.read_bytes() for path in (directory / "vanilla_mcdoc").iterdir()}


def fake_pypi(monkeypatch: MonkeyPatch, published: dict[str, dict[str, bytes]]) -> None:
    """Make ci.download answer like PyPI would, with these versions (and their wheel's files) published."""
    def download(url: str) -> bytes:
        if url.endswith("/json"):
            if not published:
                raise urllib.error.HTTPError(url, 404, "Not Found", None, None)  # type: ignore[arg-type]
            releases = {version: [{"packagetype": "bdist_wheel", "url": f"wheel:{version}"}] for version in published}
            return json.dumps({"releases": releases}).encode()
        wheel = io.BytesIO()
        with zipfile.ZipFile(wheel, "w") as archive:
            for name, data in published[url.removeprefix("wheel:")].items():
                archive.writestr(name, data)
        return wheel.getvalue()
    monkeypatch.setattr(ci, "download", download)


def test_first_build_of_a_version_gets_the_plain_version(tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    monkeypatch.chdir(tmp_path)
    make_package(tmp_path, "26.3.0", "x = 1\n")
    fake_pypi(monkeypatch, {})  # Nothing's been published yet
    ci.set_version("26.3")
    assert capsys.readouterr().out.split() == ["publish=true", "version=26.3.0"]


def test_unchanged_build_isnt_published_again(tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    monkeypatch.chdir(tmp_path)
    published = make_package(tmp_path, "26.3.0.post1", "x = 1\n")
    make_package(tmp_path, "26.3.0", "x = 1\n")  # Same code, only the version (and commit) lines differ
    fake_pypi(monkeypatch, {"26.3.0": published, "26.3.0.post1": published})
    ci.set_version("26.3")
    assert capsys.readouterr().out.split() == ["publish=false"]


def test_changed_build_gets_the_next_post_release(tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    monkeypatch.chdir(tmp_path)
    published = make_package(tmp_path, "26.3.0.post1", "x = 1\n")
    make_package(tmp_path, "26.3.0", "x = 2\n")
    fake_pypi(monkeypatch, {"26.3.0": published, "26.3.0.post1": published, "26.4.0a1": published})  # Other versions don't count
    ci.set_version("26.3")
    assert capsys.readouterr().out.split() == ["publish=true", "version=26.3.0.post2"]
    assert '__version__ = "26.3.0.post2"' in (tmp_path / "vanilla_mcdoc" / "__init__.py").read_text(encoding="utf-8")
