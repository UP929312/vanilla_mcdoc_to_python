# Generated from symbols.json for ::java::assets::shader::program::BlendMode
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.shader.program.BlendFactor import BlendFactor
    from generated_symbols.assets.shader.program.BlendFunc import BlendFunc


@dataclass(kw_only=True)
class BlendMode:
    func: BlendFunc | None = None
    srcrgb: BlendFactor | None = None
    dstrgb: BlendFactor | None = None
    srcalpha: BlendFactor | None = None
    dstalpha: BlendFactor | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::program::BlendMode": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "func",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::program::BlendFunc"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "srcrgb",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::program::BlendFactor"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "dstrgb",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::program::BlendFactor"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "srcalpha",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::program::BlendFactor"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "dstalpha",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::program::BlendFactor"
                },
                "optional": True
            }
        ]
    }
}

