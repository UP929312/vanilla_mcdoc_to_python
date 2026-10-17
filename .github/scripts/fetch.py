"""Downloads the upstream data the generator reads, from exact commits, so a build can always be reproduced. Run it from
the repo root, which is where the files go.

python .github/scripts/fetch.py [<vanilla-mcdoc commit> <mcmeta commit>]  symbols.json, versions.json and the newest version's registries.json and vanilla files (by default, the latest)
python .github/scripts/fetch.py version <minecraft version>              registries.json and vanilla's files for that version
python .github/scripts/fetch.py vanilla                                  Just vanilla's files, for registries.json's version (they aren't committed)
"""
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

# (repository, branch, file): symbols.json comes from vanilla-mcdoc, and the list of Minecraft versions from mcmeta
VANILLA_MCDOC = ("https://github.com/SpyglassMC/vanilla-mcdoc", "generated", "symbols.json")
MCMETA = ("https://github.com/misode/mcmeta", "summary", "versions/data.min.json")
MCMETA_REGISTRIES = "registries/data.min.json"  # Every registry's entries, e.g. all the loot condition types, on the same branch
# Vanilla's own data pack and resource pack files, which mcmeta tags for each version, e.g. 26.3-data-json. They're
# about 25 MB, so they go in mcmeta/, which isn't committed (utils.VANILLA_ZIPS is where the generator reads them)
MCMETA_ZIPS = ["data-json", "assets-json"]


def log(message: str) -> None:
    """Progress goes to stderr, because stdout is for $GITHUB_OUTPUT."""
    print(message, file=sys.stderr)


def download(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=120) as response:  # Only ever our fixed GitHub and PyPI URLs
        data: bytes = response.read()
        return data


def latest_commit(repository: str, branch: str) -> str:
    """The commit a branch is on right now, e.g. so symbols.json can be downloaded from that exact commit."""
    output = subprocess.run(["git", "ls-remote", repository, f"refs/heads/{branch}"], check=True, capture_output=True, text=True).stdout
    return output.split()[0]


def file_at_commit(repository: str, commit: str, path: str) -> bytes:
    return download(f"{repository.replace('https://github.com/', 'https://raw.githubusercontent.com/')}/{commit}/{path}")


def fetch(mcdoc_commit: str | None = None, mcmeta_commit: str | None = None) -> dict[str, str]:
    """Download symbols.json and versions.json from exact commits (the latest, unless given), so a build can always be
    reproduced, and record those commits in upstream.json (the package's __mcdoc_commit__ comes from it)."""
    commits = {
        "vanilla-mcdoc": mcdoc_commit or latest_commit(*VANILLA_MCDOC[:2]),
        "mcmeta": mcmeta_commit or latest_commit(*MCMETA[:2]),
    }
    log(f"Fetching symbols.json from vanilla-mcdoc@{commits['vanilla-mcdoc']}, versions from mcmeta@{commits['mcmeta']}")
    symbols = json.loads(file_at_commit(VANILLA_MCDOC[0], commits["vanilla-mcdoc"], VANILLA_MCDOC[2]))
    version_ids = [version["id"] for version in json.loads(file_at_commit(MCMETA[0], commits["mcmeta"], MCMETA[2]))]
    for path, contents in {"symbols.json": symbols, "versions.json": version_ids, "upstream.json": commits}.items():
        with open(path, "w", encoding="utf-8") as file:
            json.dump(contents, file, indent=4)
    fetch_version(version_ids[0], commits["mcmeta"])  # The summary branch is the newest version's
    return commits


def fetch_version(minecraft_version: str, mcmeta_commit: str | None = None) -> None:
    """Download what's specific to one Minecraft version: its registries, into registries.json, and vanilla's files.
    symbols.json doesn't have the registries, e.g. loot condition types with no fields of their own, like
    minecraft:survives_explosion. mcmeta tags each version's summary, e.g. 26.3-summary (and the summary branch is the newest version's)."""
    log(f"Fetching the registries for {minecraft_version}")
    registries = json.loads(file_at_commit(MCMETA[0], mcmeta_commit or f"{minecraft_version}-summary", MCMETA_REGISTRIES))
    with open("registries.json", "w", encoding="utf-8") as file:
        json.dump({"minecraft_version": minecraft_version, "registries": registries}, file, indent=4)
    fetch_vanilla_files(minecraft_version)


def fetch_vanilla_files(minecraft_version: str) -> None:
    """Download vanilla's own data pack and resource pack files for one version, which main.py puts in vanilla_mcdoc.vanilla."""
    Path("mcmeta").mkdir(exist_ok=True)
    for tag in MCMETA_ZIPS:
        log(f"Fetching vanilla's files ({tag}) for {minecraft_version}")
        Path("mcmeta", f"{tag}.zip").write_bytes(download(f"{MCMETA[0]}/archive/refs/tags/{minecraft_version}-{tag}.zip"))


def main(arguments: list[str]) -> None:
    match arguments:
        case ["version", version]:
            fetch_version(version)
        case ["vanilla"]:
            fetch_vanilla_files(json.loads(Path("registries.json").read_text(encoding="utf-8"))["minecraft_version"])
        case [*commits] if len(commits) in {0, 2}:
            fetch(*commits)
        case _:
            sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
