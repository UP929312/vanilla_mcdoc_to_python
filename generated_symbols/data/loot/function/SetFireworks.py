"""
Generated from symbols.json for ::java::data::loot::function::SetFireworks
Local link to file: generated_symbols/data/loot/function/SetFireworks.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.world.component.item.Explosion import Explosion


@dataclass(kw_only=True)
class ExplosionsStructAppend:
    values: list[Explosion]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ExplosionsStructInsert:
    values: list[Explosion]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class ExplosionsStructReplaceAll:
    values: list[Explosion]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ExplosionsStructReplaceSection:
    values: list[Explosion]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type ExplosionsStruct = ExplosionsStructAppend | ExplosionsStructInsert | ExplosionsStructReplaceAll | ExplosionsStructReplaceSection

@dataclass(kw_only=True)
class SetFireworks(Conditions):
    flight_duration: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None  # If omitted, the flight duration of the item is left untouched - or set to 0 if the component did not exist before.
    explosions: ExplosionsStruct | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetFireworks": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If omitted, the flight duration of the item is left untouched - or set to 0 if the component did not exist before.",
                "key": "flight_duration",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "explosions",
                "type": {
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
                },
                "optional": True
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

