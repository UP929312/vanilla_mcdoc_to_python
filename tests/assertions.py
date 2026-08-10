from pathlib import Path

CODE_DIVIDER = "# ~~~ CODE ~~~"
DUMP_DIVIDER = "# ~~~ MODEL DUMP ~~~"
TEST_DIVIDER = "# ~~~ WHAT ARE WE TESTING ~~~"


def run_assertions() -> None:
    for file in Path("tests/assertions").iterdir():
        expected_file_contents = file.read_text().split(TEST_DIVIDER)[1]
        metadata, expected_code = expected_file_contents.split(CODE_DIVIDER)
        generated_file_path = Path(metadata.split("Local link to file: ")[1].split("\n")[0])
        generated_file_contents = generated_file_path.read_text().split(DUMP_DIVIDER)[0].split(CODE_DIVIDER)[1]
        assert generated_file_contents.strip().strip("\n") == expected_code.strip().strip("\n"), f"{generated_file_path} was different!"


if __name__ == "__main__":
    run_assertions()