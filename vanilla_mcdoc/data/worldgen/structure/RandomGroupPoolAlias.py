"""
Generated from symbols.json for ::java::data::worldgen::structure::RandomGroupPoolAlias
Local link to file: vanilla_mcdoc/data/worldgen/structure/RandomGroupPoolAlias.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure.PoolAlias import PoolAlias
    from vanilla_mcdoc.util.NonEmptyWeightedList import NonEmptyWeightedList


class RandomGroupPoolAlias(GeneratedModel):
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
