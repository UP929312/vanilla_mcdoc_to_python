# Generated from symbols.json for ::java::world::entity::mob::player::EnderPearl
from dataclasses import dataclass
from generated_symbols.world.entity.AnyEntity import AnyEntity


@dataclass(kw_only=True)
class EnderPearl(AnyEntity):
    ender_pearl_dimension: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::EnderPearl": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "ender_pearl_dimension",
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
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::AnyEntity"
                }
            }
        ]
    }
}

