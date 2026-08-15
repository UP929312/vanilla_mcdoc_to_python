"""
Generated from symbols.json for ::java::world::item::compass::Compass
Local link to file: generated_symbols/world/item/compass/Compass.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from generated_symbols.world.item.ItemBase import ItemBase
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.world.item.compass.LodestonePos import LodestonePos


@dataclass(kw_only=True)
class Compass(ItemBase):
    LodestoneDimension: Annotated[str, IdSpec(registry='dimension')] | None = None
    LodestonePos: LodestonePos | None = None
    LodestoneTracked: bool | None = None  # Whether the compass should be linked to a lodestone. When true, the compass will reset if the lodestone at the position is removed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::compass::Compass": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemBase"
                }
            },
            {
                "kind": "pair",
                "key": "LodestoneDimension",
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
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "LodestonePos",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::compass::LodestonePos"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the compass should be linked to a lodestone.\nWhen True, the compass will reset if the lodestone at the position is removed.",
                "key": "LodestoneTracked",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

