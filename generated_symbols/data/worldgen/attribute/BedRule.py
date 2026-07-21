# Generated from symbols.json for ::java::data::worldgen::attribute::BedRule
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.attribute.BedRuleType import BedRuleType
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class BedRule:
    can_sleep: BedRuleType
    can_set_spawn: BedRuleType
    destroy_on_use: bool | None = None
    destroy_on_leave: bool | None = None
    error_message: Text | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::attribute::BedRule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "can_sleep",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::BedRuleType"
                }
            },
            {
                "kind": "pair",
                "key": "can_set_spawn",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::attribute::BedRuleType"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "explodes",
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "destroy_on_use",
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
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "destroy_on_leave",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "error_message",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
                "optional": True
            }
        ]
    }
}

