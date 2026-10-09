"""
Generated from symbols.json for ::java::data::loot::function::SetFireworks
Local link to file: generated_symbols/data/loot/function/SetFireworks.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation
from pydantic import Field

if TYPE_CHECKING:
    from generated_symbols.world.component.item.Explosion import Explosion


class ExplosionsStructAppend(GeneratedModel):
    values: list[Explosion]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class ExplosionsStructInsert(InsertListOperation):
    values: list[Explosion]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class ExplosionsStructReplaceAll(GeneratedModel):
    values: list[Explosion]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class ExplosionsStructReplaceSection(ReplaceSectionListOperation):
    values: list[Explosion]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type ExplosionsStruct = Annotated[
    ExplosionsStructAppend | ExplosionsStructInsert | ExplosionsStructReplaceAll | ExplosionsStructReplaceSection,
    Field(discriminator='mode'),
]

class SetFireworks(Conditions):
    flight_duration: Annotated[int, Field(ge=0, le=255)] | None = None  # If omitted, the flight duration of the item is left untouched - or set to 0 if the component did not exist before.
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

