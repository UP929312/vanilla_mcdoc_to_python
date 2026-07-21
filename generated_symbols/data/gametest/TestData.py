# Generated from symbols.json for ::java::data::gametest::TestData
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.gametest.test_environment.TestEnvironment import TestEnvironment
    from generated_symbols.util.Rotation import Rotation


@dataclass(kw_only=True)
class TestData:
    environment: str | TestEnvironment  # The test environment to run this test as part of.
    structure: str  # Structure NBT file to use for the test.
    max_ticks: Annotated[int, 'Range | Min `1` and above | inclusive']  # Maximum number of ticks allowed to pass before the test is considered timed out.
    setup_ticks: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Ticks to wait after placing the structure before starting the test. Defaults to `0`.
    required: bool | None = None  # Whether the test is considered required to pass for the full test suite to pass. Defaults to `true`.
    rotation: Rotation | None = None  # Rotation to apply to the test structure. Defaults to `none`.
    manual_only: bool | None = None  # If `true`, test is not included as part of automated test runs. Defaults to `false`.
    max_attempts: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Number of attempts to run the test. Defaults to `1`.
    required_successes: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Number of attempts that must succeed for the test to be considered successful. Defaults to `1`.
    sky_access: bool | None = None  # Whether the test needs clear access to the sky. Defaults to `false`. If `false`, test is enclosed in barrier blocks. If `true`, the top is left open.
    padding: Annotated[int, 'Range | `0`-`128` | both inclusive'] | None = None  # Additional padding in blocks placed around the structure. Defaults to `0`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::TestData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The test environment to run this test as part of.",
                "key": "environment",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "test_environment"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::gametest::test_environment::TestEnvironment"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Structure NBT file to use for the test.",
                "key": "structure",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "structure"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Maximum number of ticks allowed to pass before the test is considered timed out.",
                "key": "max_ticks",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Ticks to wait after placing the structure before starting the test. Defaults to `0`.",
                "key": "setup_ticks",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the test is considered required to pass for the full test suite to pass. Defaults to `True`.",
                "key": "required",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Rotation to apply to the test structure. Defaults to `none`.",
                "key": "rotation",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::Rotation"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If `True`, test is not included as part of automated test runs. Defaults to `False`.",
                "key": "manual_only",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of attempts to run the test. Defaults to `1`.",
                "key": "max_attempts",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Number of attempts that must succeed for the test to be considered successful. Defaults to `1`.",
                "key": "required_successes",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the test needs clear access to the sky. Defaults to `False`.\nIf `False`, test is enclosed in barrier blocks. If `True`, the top is left open.",
                "key": "sky_access",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "Additional padding in blocks placed around the structure. Defaults to `0`.",
                "key": "padding",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 128
                    }
                },
                "optional": True
            }
        ]
    }
}

