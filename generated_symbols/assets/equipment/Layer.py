# Generated from symbols.json for ::java::assets::equipment::Layer
from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from generated_symbols.assets.equipment.Dyeable import Dyeable


T = TypeVar('T')

@dataclass(kw_only=True)
class Layer(Generic[T]):
    texture: T  # Texture location for this layer, inside `entity/equipment/<layer>/`.
    dyeable: Dyeable | None = None  # If specified, this layer will be tinted by the color contained in the `dyed_color` component.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::equipment::Layer": {
        "kind": "template",
        "child": {
            "kind": "struct",
            "fields": [
                {
                    "kind": "pair",
                    "desc": "Texture location for this layer, inside `entity/equipment/<layer>/`.",
                    "key": "texture",
                    "type": {
                        "kind": "reference",
                        "path": "::java::assets::equipment::T"
                    }
                },
                {
                    "kind": "spread",
                    "attributes": [
                        {
                            "name": "until",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "1.21.5"
                                }
                            }
                        }
                    ],
                    "type": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "desc": "If specified, this layer will be tinted by the color contained in the `dyed_color` component. \\\nItems not in the `#dyeable` tag are always considered \"not dyed\".",
                                "key": "dyeable",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::assets::equipment::Dyeable"
                                },
                                "optional": True
                            }
                        ]
                    }
                },
                {
                    "kind": "spread",
                    "attributes": [
                        {
                            "name": "since",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "1.21.5"
                                }
                            }
                        }
                    ],
                    "type": {
                        "kind": "struct",
                        "fields": [
                            {
                                "kind": "pair",
                                "desc": "If specified, this layer will be tinted by the color contained in the `dyed_color` component.",
                                "key": "dyeable",
                                "type": {
                                    "kind": "reference",
                                    "path": "::java::assets::equipment::Dyeable"
                                },
                                "optional": True
                            }
                        ]
                    }
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

