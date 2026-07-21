# Generated from symbols.json for ::java::data::worldgen::structure::RandomGroupPoolAlias
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.PoolAlias import PoolAlias
    from generated_symbols.util.NonEmptyWeightedList import NonEmptyWeightedList


@dataclass(kw_only=True)
class RandomGroupPoolAlias:
    groups: NonEmptyWeightedList[list[PoolAlias]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::RandomGroupPoolAlias": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "groups",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::NonEmptyWeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::data::worldgen::structure::PoolAlias"
                            }
                        }
                    ]
                }
            }
        ]
    }
}

