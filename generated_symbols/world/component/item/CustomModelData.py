# Generated from symbols.json for ::java::world::component::item::CustomModelData
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class CustomModelData:
    floats: list[float] | None = None
    flags: list[bool] | None = None
    strings: list[str] | None = None
    colors: list[RGB] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::CustomModelData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "floats",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "flags",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "boolean"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "strings",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "colors",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::color::RGB"
                    }
                },
                "optional": True
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.21.4"
                    }
                }
            }
        ]
    }
}

