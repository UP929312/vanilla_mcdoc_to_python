# Generated from symbols.json for ::java::world::component::DataComponentExactPredicate
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from generated_symbols.world.component.PersistentDataComponent import PersistentDataComponent


type DataComponentExactPredicate = dict[PersistentDataComponent, Any]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::DataComponentExactPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::world::component::PersistentDataComponent"
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "minecraft:data_component"
                }
            }
        ]
    }
}

