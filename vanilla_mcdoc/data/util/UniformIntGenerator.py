"""
Generated from symbols.json for ::java::data::util::UniformIntGenerator
Local link to file: vanilla_mcdoc/data/util/UniformIntGenerator.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class UniformIntGenerator(GeneratedModel):
    min: int | None = None
    max: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::UniformIntGenerator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
