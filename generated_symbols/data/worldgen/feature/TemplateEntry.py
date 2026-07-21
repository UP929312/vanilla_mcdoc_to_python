# Generated from symbols.json for ::java::data::worldgen::feature::TemplateEntry
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.Rotation import Rotation


@dataclass(kw_only=True)
class TemplateEntry:
    id: str  # The structure template to place.
    rotations: list[Rotation] | None = None  # Rotations to choose from and apply to this template, centered around the origin. If not specified, defaults to all allowed rotations.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::TemplateEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The structure template to place.",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "structure"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Rotations to choose from and apply to this template, centered around the origin.\nIf not specified, defaults to all allowed rotations.",
                "key": "rotations",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::Rotation"
                    }
                },
                "optional": True
            }
        ]
    }
}

