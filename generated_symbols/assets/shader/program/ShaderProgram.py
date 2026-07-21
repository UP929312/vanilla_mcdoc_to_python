# Generated from symbols.json for ::java::assets::shader::program::ShaderProgram
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.shader.program.Defines import Defines
    from generated_symbols.assets.shader.program.Sampler import Sampler
    from generated_symbols.assets.shader.program.Uniform import Uniform


@dataclass(kw_only=True)
class ShaderProgram:
    vertex: str
    fragment: str
    uniforms: list[Uniform]
    samplers: list[Sampler] | None = None
    defines: Defines | None = None  # Defines GLSL directives to be injected into the shader source.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::program::ShaderProgram": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "vertex",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
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
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.2"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "shader/vertex"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "fragment",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
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
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.2"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "shader/fragment"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "samplers",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::shader::program::Sampler"
                    }
                },
                "optional": True
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
                "key": "attributes",
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
                "key": "uniforms",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::shader::program::Uniform"
                    }
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
                "desc": "Unused.",
                "key": "blend",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::program::BlendMode"
                },
                "optional": True
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
                "key": "cull",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "Defines GLSL directives to be injected into the shader source.",
                "key": "defines",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::shader::program::Defines"
                },
                "optional": True
            }
        ]
    }
}

