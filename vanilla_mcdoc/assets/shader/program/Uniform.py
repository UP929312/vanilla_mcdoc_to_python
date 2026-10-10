"""
Generated from symbols.json for ::java::assets::shader::program::Uniform
Local link to file: vanilla_mcdoc/assets/shader/program/Uniform.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.program.UniformType import UniformType


class Uniform(GeneratedModel):
    name: str
    type: UniformType
    count: int
    values: list[float]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::program::Uniform": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "name",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::program::UniformType"
                }
            },
            {
                "kind": "pair",
                "key": "count",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    }
                }
            }
        ]
    }
}
