# Generated from symbols.json for ::java::assets::equipment::WingsLayer
from dataclasses import dataclass
from typing import Generic, TypeVar
from generated_symbols.assets.equipment.Layer import Layer


T = TypeVar('T')

@dataclass(kw_only=True)
class WingsLayer(Layer[T], Generic[T]):
    use_player_texture: bool | None = None  # Whether this layer texture should be overridden by the player's custom elytra texture.  Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::equipment::WingsLayer": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "spread",
                    "type": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::assets::equipment::Layer"
                        },
                        "typeArgs": [
                            {
                                "kind": "reference",
                                "path": "::java::assets::equipment::T"
                            }
                        ]
                    }
                },
                {
                    "kind": "pair",
                    "desc": "Whether this layer texture should be overridden by the player's custom elytra texture. \\\nDefaults to `False`.",
                    "key": "use_player_texture",
                    "type": {
                        "kind": "boolean"
                    },
                    "optional": True
                }
            ]
        },
        "typeParams": [
            {
                "path": "::java::assets::equipment::T"
            }
        ]
    }
}

