# Generated from symbols.json for ::java::data::loot::condition::TimeCheck
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.IntRange import IntRange


@dataclass(kw_only=True)
class TimeCheck:
    clock: str  # The world clock to check.
    value: IntRange  # Check the current game tick.
    period: int | None = None  # Game tick supplied to `value` check gets modulo-divided by this. For example, if set to 24000, `value` operates on a time period of days.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::TimeCheck": {
        "kind": "struct",
        "fields": [
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
                "desc": "The world clock to check.",
                "key": "clock",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "world_clock"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Check the current game tick.",
                "key": "value",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::util::RandomValueBounds",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::util::IntRange",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Game tick supplied to `value` check gets modulo-divided by this.\nFor example, if set to 24000, `value` operates on a time period of days.",
                "key": "period",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

