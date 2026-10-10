"""
Generated from symbols.json for ::java::assets::shader::program::Sampler
Local link to file: vanilla_mcdoc/assets/shader/program/Sampler.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Sampler(GeneratedModel):
    name: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::program::Sampler": {
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
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "key": "file",
                "type": {
                    "kind": "string"
                },
                "optional": True
            }
        ]
    }
}
