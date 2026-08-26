"""
Generated from symbols.json for ::java::data::loot::function::FireworkExplosions
Local link to file: generated_symbols/data/loot/function/FireworkExplosions.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from generated_symbols.world.component.item.Explosion import Explosion


@dataclass(kw_only=True)
class FireworkExplosionsAppend:
    values: list[Explosion]
    mode: Literal['minecraft:append'] = 'minecraft:append'  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FireworkExplosionsInsert(InsertListOperation):
    values: list[Explosion]
    mode: Literal['minecraft:insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FireworkExplosionsReplaceAll:
    values: list[Explosion]
    mode: Literal['minecraft:replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FireworkExplosionsReplaceSection(ReplaceSectionListOperation):
    values: list[Explosion]
    mode: Literal['minecraft:replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type FireworkExplosions = FireworkExplosionsAppend | FireworkExplosionsInsert | FireworkExplosionsReplaceAll | FireworkExplosionsReplaceSection


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

