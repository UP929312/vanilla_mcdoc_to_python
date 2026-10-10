"""
Generated from symbols.json for ::java::world::component::item::PotionContents
Local link to file: vanilla_mcdoc/world/component/item/PotionContents.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.util.effect.MobEffectInstance import MobEffectInstance


class PotionContents(GeneratedModel):
    potion: Annotated[str, IdSpec(registry='potion')] | None = None
    custom_color: int | None = None  # Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    custom_name: str | None = None  # If present, is used to generate the item name using the translation key `item.minecraft.<potion_type>.effect.<custom_name>`.
    custom_effects: list[MobEffectInstance] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::PotionContents": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "potion",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "potion"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "custom_color",
                "type": {
                    "kind": "int",
                    "attributes": [
                        {
                            "name": "color",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "composite_rgb"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If present, is used to generate the item name using the translation key `item.minecraft.<potion_type>.effect.<custom_name>`.",
                "key": "custom_name",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "custom_effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::effect::MobEffectInstance"
                    }
                },
                "optional": True
            }
        ]
    }
}
