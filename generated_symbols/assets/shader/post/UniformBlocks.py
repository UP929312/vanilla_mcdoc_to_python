# Generated from symbols.json for ::java::assets::shader::post::UniformBlocks
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.shader.post.UniformValue import UniformValue


type UniformBlocks = dict[str, list[UniformValue]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::UniformBlocks": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "List of uniform values in this block. The order must match the order in the shader file.",
                "key": {
                    "kind": "string"
                },
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::shader::post::UniformValue"
                    }
                }
            }
        ]
    }
}

