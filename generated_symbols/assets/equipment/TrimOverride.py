# Generated from symbols.json for ::java::assets::equipment::TrimOverride
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.PaletteRef import PaletteRef


@dataclass(kw_only=True)
class WhenStruct:
    pattern: Annotated[str, IdSpec(registry='trim_pattern')] | None = None
    material: Annotated[str, IdSpec(registry='trim_material')] | None = None


@dataclass(kw_only=True)
class TrimOverride:
    when: WhenStruct
    texture: Annotated[str, IdSpec()] | None = None  # When present, overrides the base texture provided by trim pattern.  The texture is located under `trims/entity/<layer>/`.
    palette: PaletteRef | None = None  # When present, overrides the palette texture provided by trim material.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::equipment::TrimOverride": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "when",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "pattern",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "trim_pattern"
                                            }
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        },
                        {
                            "kind": "pair",
                            "key": "material",
                            "type": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "id",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "trim_material"
                                            }
                                        }
                                    }
                                ]
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "When present, overrides the base texture provided by trim pattern. \\\nThe texture is located under `trims/entity/<layer>/`.",
                "key": "texture",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "When present, overrides the palette texture provided by trim material.",
                "key": "palette",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::atlas::PaletteRef"
                },
                "optional": True
            }
        ]
    }
}

