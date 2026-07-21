# Generated from symbols.json for ::java::data::loot::function::SetPotion
from dataclasses import dataclass
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class SetPotion(Conditions):
    id: str  # The potion identifier.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetPotion": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The potion identifier.",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "potion"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

