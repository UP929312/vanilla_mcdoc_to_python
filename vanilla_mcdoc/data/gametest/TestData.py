"""
Generated from symbols.json for ::java::data::gametest::TestData
Local link to file: vanilla_mcdoc/data/gametest/TestData.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.gametest.test_environment.TestEnvironment import TestEnvironment
    from vanilla_mcdoc.util.Rotation import Rotation


class TestData(GeneratedModel):
    environment: Annotated[str, IdSpec(registry='test_environment')] | TestEnvironment  # The test environment to run this test as part of.
    dimension: Annotated[str, IdSpec(registry='dimension')] | None = None  # Defaults to overworld.
    structure: Annotated[str, IdSpec(registry='structure')]  # Structure NBT file to use for the test.
    max_ticks: Annotated[int, Field(ge=1)]  # Maximum number of ticks allowed to pass before the test is considered timed out.
    setup_ticks: Annotated[int, Field(ge=0)] | None = None  # Ticks to wait after placing the structure before starting the test. Defaults to `0`.
    required: bool | None = None  # Whether the test is considered required to pass for the full test suite to pass. Defaults to `true`.
    rotation: Rotation | None = None  # Rotation to apply to the test structure. Defaults to `none`.
    manual_only: bool | None = None  # If `true`, test is not included as part of automated test runs. Defaults to `false`.
    max_attempts: Annotated[int, Field(ge=1)] | None = None  # Number of attempts to run the test. Defaults to `1`.
    required_successes: Annotated[int, Field(ge=1)] | None = None  # Number of attempts that must succeed for the test to be considered successful. Defaults to `1`.
    sky_access: bool | None = None  # Whether the test needs clear access to the sky. Defaults to `false`. If `false`, test is enclosed in barrier blocks. If `true`, the top is left open.
    padding: Annotated[int, Field(ge=0, le=128)] | None = None  # Additional padding in blocks placed around the structure. Defaults to `0`.
