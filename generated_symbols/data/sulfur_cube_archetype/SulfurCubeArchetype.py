# Generated from symbols.json for ::java::data::sulfur_cube_archetype::SulfurCubeArchetype
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.sulfur_cube_archetype.AttributeEntry import AttributeEntry
    from generated_symbols.data.sulfur_cube_archetype.ContactDamage import ContactDamage
    from generated_symbols.data.sulfur_cube_archetype.ExplosionData import ExplosionData
    from generated_symbols.data.sulfur_cube_archetype.KnockbackModifiers import KnockbackModifiers
    from generated_symbols.data.sulfur_cube_archetype.SoundSettings import SoundSettings


@dataclass(kw_only=True)
class SulfurCubeArchetype:
    items: str | list[str]
    knockback_modifiers: KnockbackModifiers
    attribute_modifiers: list[AttributeEntry]
    sound_settings: SoundSettings
    buoyant: bool | None = None  # Defaults to `false`.
    explosion: ExplosionData | None = None  # When present, sulfur cube with this archetype will explode when ignited.
    contact_damage: ContactDamage | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::sulfur_cube_archetype::SulfurCubeArchetype": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "items",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "item"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "item"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to `False`.",
                "key": "buoyant",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "When present, sulfur cube with this archetype will explode when ignited.",
                "key": "explosion",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::sulfur_cube_archetype::ExplosionData"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "contact_damage",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::sulfur_cube_archetype::ContactDamage"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "knockback_modifiers",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::sulfur_cube_archetype::KnockbackModifiers"
                }
            },
            {
                "kind": "pair",
                "key": "attribute_modifiers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::sulfur_cube_archetype::AttributeEntry"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "sound_settings",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::sulfur_cube_archetype::SoundSettings"
                }
            }
        ]
    }
}

