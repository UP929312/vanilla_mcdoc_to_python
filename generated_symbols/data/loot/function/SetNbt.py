# Generated from symbols.json for ::java::data::loot::function::SetNbt
from dataclasses import dataclass
from generated_symbols.data.loot.function.Conditions import Conditions


@dataclass(kw_only=True)
class SetNbt(Conditions):
    tag: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetNbt": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "tag",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "nbt",
                            "value": {
                                "kind": "dispatcher",
                                "parallelIndices": [
                                    {
                                        "kind": "static",
                                        "value": "%fallback"
                                    }
                                ],
                                "registry": "minecraft:item"
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

