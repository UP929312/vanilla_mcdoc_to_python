import json
from pathlib import Path

from pytest import MonkeyPatch

import fetch


def test_fetch_version_saves_that_versions_registries(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(fetch, "file_at_commit", lambda repository, commit, path: json.dumps({"loot_condition_type": [commit]}).encode())
    fetch.fetch_version("26.3")
    assert json.loads(Path("registries.json").read_text(encoding="utf-8")) == {"minecraft_version": "26.3", "registries": {"loot_condition_type": ["26.3-summary"]}}
