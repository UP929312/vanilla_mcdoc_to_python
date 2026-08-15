"""
Generated from symbols.json for ::java::data::advancement::trigger::ChangedDimension
Local link to file: generated_symbols/data/advancement/trigger/ChangedDimension.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class ChangedDimension(TriggerBase):
    from_: Annotated[str, IdSpec(registry='dimension')] | None = None
    to: Annotated[str, IdSpec(registry='dimension')] | None = None


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

