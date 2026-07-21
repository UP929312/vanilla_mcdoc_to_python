# Generated from symbols.json for ::java::data::damage_type::DamageType
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.damage_type.DamageEffects import DamageEffects
    from generated_symbols.data.damage_type.DamageScaling import DamageScaling
    from generated_symbols.data.damage_type.DeathMessageType import DeathMessageType


@dataclass(kw_only=True)
class DamageType:
    message_id: str  # The message id used for deaths caused by this damage type. Is combined with the result of `death_message_type` to form a translation key.
    exhaustion: Annotated[float, 'Range | Min `0` and above | inclusive']  # Amount of hunger exhaustion to cause.
    scaling: DamageScaling  # Whether to scale damage with difficulty levels.
    effects: DamageEffects | None = None  # Controls how damage manifests when inflicted on players. Defaults to `hurt`.
    death_message_type: DeathMessageType | None = None  # Controls if special death message variants are used. Defaults to `default`.  For more info see: https://minecraft.wiki/w/Damage_type#Death_messages


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::damage_type::DamageType": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The message id used for deaths caused by this damage type.\nIs combined with the result of `death_message_type` to form a translation key.",
                "key": "message_id",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "desc": "Amount of hunger exhaustion to cause.",
                "key": "exhaustion",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Whether to scale damage with difficulty levels.",
                "key": "scaling",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::damage_type::DamageScaling"
                }
            },
            {
                "kind": "pair",
                "desc": "Controls how damage manifests when inflicted on players. Defaults to `hurt`.",
                "key": "effects",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::damage_type::DamageEffects"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Controls if special death message variants are used. Defaults to `default`.\n\nFor more info see: https://minecraft.wiki/w/Damage_type#Death_messages",
                "key": "death_message_type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::damage_type::DeathMessageType"
                },
                "optional": True
            }
        ]
    }
}

