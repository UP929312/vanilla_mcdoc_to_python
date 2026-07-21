# Generated from symbols.json for ::java::assets::shader::post::TargetInput
from dataclasses import dataclass


@dataclass(kw_only=True)
class TargetInput:
    target: str
    sampler_name: str
    use_depth_buffer: bool | None = None
    bilinear: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::TargetInput": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "shader_target"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "sampler_name",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "use_depth_buffer",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "bilinear",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

