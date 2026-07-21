# Generated from symbols.json for ::java::data::advancement::Advancement
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.advancement.AdvancementCriterion import AdvancementCriterion
    from generated_symbols.data.advancement.AdvancementDisplay import AdvancementDisplay
    from generated_symbols.data.advancement.AdvancementRewards import AdvancementRewards


@dataclass(kw_only=True)
class Advancement:
    criteria: dict[str, AdvancementCriterion]  # If `requirements` is not defined, all defined criteria will be required.
    display: AdvancementDisplay | None = None  # If present, advancement will be visible in the advancement tabs.
    parent: str | None = None  # If this field is absent, this advancement is a root advancement. Circular references cause a loading failure.
    requirements: Annotated[list[Annotated[list[str], 'Length = 1 (inclusive) and above']], 'Length = 1 (inclusive) and above'] | None = None  # If all criteria are required at once, this may be omitted.  Contains all of the `criteria` keys.  If all of the lists each have at least one criteria met, the advancement is complete (basically AND grouping of OR groups).
    rewards: AdvancementRewards | None = None  # Provided to the player when this advancement is obtained.
    sends_telemetry_event: bool | None = None  # Defaults to `false`. The vanilla game client only reads this for advancements from the `minecraft` namespace.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::Advancement": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If present, advancement will be visible in the advancement tabs.",
                "key": "display",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::AdvancementDisplay"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If this field is absent, this advancement is a root advancement.\nCircular references cause a loading failure.",
                "key": "parent",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "advancement"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If `requirements` is not defined, all defined criteria will be required.",
                "key": "criteria",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "criterion",
                                        "value": {
                                            "kind": "tree",
                                            "values": {
                                                "definition": {
                                                    "kind": "literal",
                                                    "value": {
                                                        "kind": "boolean",
                                                        "value": True
                                                    }
                                                }
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "reference",
                                "path": "::java::data::advancement::AdvancementCriterion"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "If all criteria are required at once, this may be omitted.\n\nContains all of the `criteria` keys.\n\nIf all of the lists each have at least one criteria met, the advancement is complete (basically AND grouping of OR groups).",
                "key": "requirements",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "list",
                        "item": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "criterion"
                                }
                            ]
                        },
                        "lengthRange": {
                            "kind": 0,
                            "min": 1
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Provided to the player when this advancement is obtained.",
                "key": "rewards",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::AdvancementRewards"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `False`. The vanilla game client only reads this for advancements from the `minecraft` namespace.",
                "key": "sends_telemetry_event",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

