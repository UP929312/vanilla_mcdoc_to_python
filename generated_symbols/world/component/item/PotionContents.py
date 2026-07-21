# Generated from symbols.json for ::java::world::component::item::PotionContents
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.effect.MobEffectInstance import MobEffectInstance


@dataclass(kw_only=True)
class PotionContents:
    potion: str | None = None
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

