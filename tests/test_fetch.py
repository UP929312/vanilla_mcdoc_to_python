import json
from pathlib import Path

from pytest import MonkeyPatch

import fetch  # type: ignore[import]


def test_fetch_version_saves_that_versions_registries_and_vanilla_files(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(fetch, "file_at_commit", lambda repository, commit, path: json.dumps({"loot_condition_type": [commit]}).encode())
    monkeypatch.setattr(fetch, "download", lambda url: url.encode())  # Each zip is where it came from
    fetch.fetch_version("26.3")
    assert json.loads(Path("registries.json").read_text(encoding="utf-8")) == {"minecraft_version": "26.3", "registries": {"loot_condition_type": ["26.3-summary"]}}
    assert Path("mcmeta/data-json.zip").read_bytes() == b"https://github.com/misode/mcmeta/archive/refs/tags/26.3-data-json.zip"
    assert Path("mcmeta/assets-json.zip").read_bytes() == b"https://github.com/misode/mcmeta/archive/refs/tags/26.3-assets-json.zip"


def test_fetch_vanilla_gets_registries_jsons_versions_files(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    Path("registries.json").write_text(json.dumps({"minecraft_version": "26.2", "registries": {}}), encoding="utf-8")
    monkeypatch.setattr(fetch, "download", lambda url: url.encode())
    fetch.main(["vanilla"])
    assert Path("mcmeta/data-json.zip").read_bytes().endswith(b"/26.2-data-json.zip")
    assert json.loads(Path("registries.json").read_text(encoding="utf-8"))["minecraft_version"] == "26.2"  # Left alone
