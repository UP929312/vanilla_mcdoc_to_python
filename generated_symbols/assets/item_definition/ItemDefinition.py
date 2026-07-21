# Generated from symbols.json for ::java::assets::item_definition::ItemDefinition
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ItemModel import ItemModel


@dataclass(kw_only=True)
class ItemDefinition:
    model: ItemModel
    hand_animation_on_swap: bool | None = None  # Whether the down-and-up animation should be played in first-person view when the item stack is changed. Defaults to `true`.
    oversized_in_gui: bool | None = None  # Whether the item model is allowed to be bigger than its item slot. Defaults to `false`, which clips the item model in GUI to the item slot size. The behavior of `true` is **not** officially supported.
    swap_animation_scale: float | None = None  # How fast the item moves up and down when swapping items in hotbar. Defaults to 1.0


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ItemDefinition": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ItemModel"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the down-and-up animation should be played in first-person view when the item stack is changed.\nDefaults to `True`.",
                "key": "hand_animation_on_swap",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.6"
                            }
                        }
                    }
                ],
                "desc": "Whether the item model is allowed to be bigger than its item slot.\nDefaults to `False`, which clips the item model in GUI to the item slot size.\nThe behavior of `True` is **not** officially supported.",
                "key": "oversized_in_gui",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.11"
                            }
                        }
                    }
                ],
                "desc": "How fast the item moves up and down when swapping items in hotbar.\nDefaults to 1.0",
                "key": "swap_animation_scale",
                "type": {
                    "kind": "float"
                },
                "optional": True
            }
        ]
    }
}

