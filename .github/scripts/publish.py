"""Helpers for publish.yml, which builds vanilla_mcdoc for each Minecraft version and publishes it to PyPI. Run it from
the repo root.

python .github/scripts/publish.py plan                             Fetch, then say which versions to build (lines for $GITHUB_OUTPUT)
python .github/scripts/publish.py set-version <minecraft version>  Pick the package's next version, or say nothing changed

Each Minecraft version is its own package version, e.g. 26.3 -> 26.3.0, and rebuilding it (because Spyglass fixed something,
or the generator changed) publishes the next post-release: 26.3.0.post1, 26.3.0.post2... So `vanilla-mcdoc==26.3.0.*`
always gets the newest build for 26.3. PyPI never lets a version be replaced, which is why rebuilds can't reuse 26.3.0.
"""
import io
import json
import re
import sys
import urllib.error
import zipfile
from pathlib import Path

from fetch import download, fetch, log

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # The repo root, for utils (Python only adds this script's folder)
PYPI_PROJECT = "vanilla-mcdoc"
PACKAGE_DIRECTORY = Path("vanilla_mcdoc")
RELEASES_TO_BUILD = 3  # The newest few releases keep getting fixes, plus the newest snapshot/pre-release/rc (if it's newer)


def versions_to_build(version_ids: list[str]) -> list[str]:
    """The newest few releases, plus the newest snapshot/pre-release/release candidate if it's newer than all of them.
    Only versions that can be package versions, so not old style snapshots like 25w14a. version_ids is newest first."""
    from utils import minecraft_to_python_version  # Not at the top, as utils loads symbols.json, which plan fetches first

    def publishable(version: str) -> bool:
        try:
            minecraft_to_python_version(version)
            return True
        except ValueError:
            return False

    candidates = [version for version in version_ids if publishable(version)]
    releases = [version for version in candidates if re.fullmatch(r"[\d.]+", version)]
    newest_unreleased = candidates[:1] if candidates and candidates[0] not in releases else []
    return newest_unreleased + releases[:RELEASES_TO_BUILD]


def plan() -> None:
    """Fetch the latest upstream data, and say which versions to build from it, and the commits it's from (so every
    build uses the same data)."""
    commits = fetch()
    versions = versions_to_build(json.loads(Path("versions.json").read_text(encoding="utf-8")))
    log(f"Versions to build: {versions}")
    print(f"versions={json.dumps(versions)}")
    print(f"mcdoc={commits['vanilla-mcdoc']}")
    print(f"mcmeta={commits['mcmeta']}")


def package_contents(files: dict[str, bytes]) -> dict[str, bytes]:
    """The package's files, minus the lines that change on every build without the code changing (the version and commit)."""
    contents = {}
    for name, data in files.items():
        if name == f"{PACKAGE_DIRECTORY.name}/__init__.py":
            data = b"\n".join(line for line in data.splitlines() if not line.startswith((b"__version__", b"__mcdoc_commit__")))
        contents[name] = data
    return contents


def published_builds(base_version: str) -> tuple[dict[str, list[dict[str, str]]], list[str]]:
    """Every release on PyPI, and the ones that are builds of this base version (oldest first), e.g. 26.3.0, 26.3.0.post1."""
    try:
        releases: dict[str, list[dict[str, str]]] = json.loads(download(f"https://pypi.org/pypi/{PYPI_PROJECT}/json"))["releases"]
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
        releases = {}  # Nothing's been published yet
    builds = [version for version in releases if version == base_version or version.startswith(f"{base_version}.post")]
    return releases, sorted(builds, key=lambda version: int(version.partition(".post")[2] or 0))


def description_changed(metadata: str) -> bool:
    """Whether README.md has changed since the build with this wheel METADATA. It's the PyPI page, which only changes when
    a new version is published, so a changed README is worth publishing for (even if the code's the same)."""
    readme = Path("README.md")
    published_description = metadata.partition("\n\n")[2]  # The description comes after the headers
    return bool(metadata) and readme.exists() and published_description.strip() != readme.read_text(encoding="utf-8").strip()


def set_version(minecraft_version: str) -> None:
    """Write the package's version into its __init__.py: the next post-release of this Minecraft version's builds,
    unless the newest one on PyPI is identical to what's just been generated, in which case there's nothing to publish."""
    from utils import minecraft_to_python_version

    base_version = minecraft_to_python_version(minecraft_version)
    releases, builds = published_builds(base_version)
    if builds:
        newest = builds[-1]
        wheel_url = next(file["url"] for file in releases[newest] if file["packagetype"] == "bdist_wheel")
        with zipfile.ZipFile(io.BytesIO(download(wheel_url))) as wheel:
            published = package_contents({name: wheel.read(name) for name in wheel.namelist() if name.startswith(f"{PACKAGE_DIRECTORY.name}/")})
            metadata = next((wheel.read(name).decode() for name in wheel.namelist() if name.endswith(".dist-info/METADATA")), "")
        generated = package_contents({
            path.as_posix(): path.read_bytes() for path in PACKAGE_DIRECTORY.rglob("*") if path.is_file() and "__pycache__" not in path.parts
        })
        if published == generated and not description_changed(metadata):
            log(f"{newest} is identical to what's just been generated, so there's nothing to publish")
            print("publish=false")
            return
        version = f"{base_version}.post{int(newest.partition('.post')[2] or 0) + 1}"
    else:
        version = base_version
    init_file = PACKAGE_DIRECTORY / "__init__.py"
    init_file.write_text(re.sub(r'^__version__ = ".*?"', f'__version__ = "{version}"', init_file.read_text(encoding="utf-8"), flags=re.MULTILINE), encoding="utf-8")
    log(f"Publishing {version} (for Minecraft {minecraft_version})")
    print("publish=true")
    print(f"version={version}")


def main(arguments: list[str]) -> None:
    match arguments:
        case ["plan"]:
            plan()
        case ["set-version", version]:
            set_version(version)
        case _:
            sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
