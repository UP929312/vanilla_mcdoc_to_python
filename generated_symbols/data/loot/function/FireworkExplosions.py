"""
Generated from symbols.json for ::java::data::loot::function::FireworkExplosions
Local link to file: generated_symbols/data/loot/function/FireworkExplosions.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.world.component.item.Explosion import Explosion


@dataclass(kw_only=True)
class FireworkExplosionsAppend:
    values: list[Explosion]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FireworkExplosionsInsert:
    values: list[Explosion]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class FireworkExplosionsReplaceAll:
    values: list[Explosion]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FireworkExplosionsReplaceSection:
    values: list[Explosion]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


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

