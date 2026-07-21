# Generated from symbols.json for ::java::assets::shader::program::Uniform
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.shader.program.UniformType import UniformType


@dataclass(kw_only=True)
class Uniform:
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

