"""
Generated from symbols.json for ::java::data::loot::function::FireworkExplosions
Local link to file: vanilla_mcdoc/data/loot/function/FireworkExplosions.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.Explosion import Explosion


class FireworkExplosionsAppend(GeneratedModel):
    values: list[Explosion]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class FireworkExplosionsInsert(InsertListOperation):
    values: list[Explosion]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class FireworkExplosionsReplaceAll(GeneratedModel):
    values: list[Explosion]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class FireworkExplosionsReplaceSection(ReplaceSectionListOperation):
    values: list[Explosion]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type FireworkExplosions = Annotated[
    FireworkExplosionsAppend | FireworkExplosionsInsert | FireworkExplosionsReplaceAll | FireworkExplosionsReplaceSection,
    Field(discriminator='mode'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::FireworkExplosions": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "dispatcher",
                        "parallelIndices": [
                            {
                                "kind": "static",
                                "value": "firework_explosion"
                            }
                        ],
                        "registry": "minecraft:data_component"
                    }
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ListOperation"
                }
            }
        ]
    }
}
