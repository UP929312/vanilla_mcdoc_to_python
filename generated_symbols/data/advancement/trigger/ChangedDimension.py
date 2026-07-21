# Generated from symbols.json for ::java::data::advancement::trigger::ChangedDimension
from dataclasses import dataclass
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase


@dataclass(kw_only=True)
class ChangedDimension(TriggerBase):
    from_: str | None = None
    to: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ChangedDimension": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
                }
            },
            {
                "kind": "pair",
                "key": "from",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dimension"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "to",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "dimension"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

