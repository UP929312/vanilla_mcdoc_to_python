# Generated from symbols.json for ::java::assets::shader::post::Pass
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.shader.post.TargetInput import TargetInput
    from generated_symbols.assets.shader.post.TextureInput import TextureInput
    from generated_symbols.assets.shader.post.UniformBlocks import UniformBlocks


@dataclass(kw_only=True)
class Pass:
    vertex_shader: str
    fragment_shader: str
    output: str
    inputs: list[TargetInput | TextureInput] | None = None
    uniforms: UniformBlocks | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::Pass": {
        "kind": "union",
        "members": [
            {
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
                        "key": "intarget",
                        "type": {
                            "kind": "string"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "outtarget",
                        "type": {
                            "kind": "string"
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "auxtargets",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "reference",
                                "path": "::java::assets::shader::post::AuxTarget"
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "use_linear_filter",
                        "type": {
                            "kind": "boolean"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "uniforms",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "list",
                                    "item": {
                                        "kind": "reference",
                                        "path": "::java::assets::shader::post::UniformValue"
                                    },
                                    "attributes": [
                                        {
                                            "name": "until",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.21.6"
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    "kind": "reference",
                                    "path": "::java::assets::shader::post::UniformBlocks",
                                    "attributes": [
                                        {
                                            "name": "since",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.21.6"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "optional": True
                    }
                ],
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
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "attributes": [
                            {
                                "name": "until",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.21.5"
                                    }
                                }
                            }
                        ],
                        "key": "program",
                        "type": {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "shader"
                                        }
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "kind": "spread",
                        "attributes": [
                            {
                                "name": "since",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "1.21.5"
                                    }
                                }
                            }
                        ],
                        "type": {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": "vertex_shader",
                                    "type": {
                                        "kind": "string",
                                        "attributes": [
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
                                },
                                {
                                    "kind": "pair",
                                    "key": "fragment_shader",
                                    "type": {
                                        "kind": "string",
                                        "attributes": [
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
                                }
                            ]
                        }
                    },
                    {
                        "kind": "pair",
                        "key": "inputs",
                        "type": {
                            "kind": "list",
                            "item": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "reference",
                                        "path": "::java::assets::shader::post::TargetInput"
                                    },
                                    {
                                        "kind": "reference",
                                        "path": "::java::assets::shader::post::TextureInput"
                                    }
                                ]
                            }
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "output",
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
                        "key": "uniforms",
                        "type": {
                            "kind": "union",
                            "members": [
                                {
                                    "kind": "list",
                                    "item": {
                                        "kind": "reference",
                                        "path": "::java::assets::shader::post::UniformValue"
                                    },
                                    "attributes": [
                                        {
                                            "name": "until",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.21.6"
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    "kind": "reference",
                                    "path": "::java::assets::shader::post::UniformBlocks",
                                    "attributes": [
                                        {
                                            "name": "since",
                                            "value": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "1.21.6"
                                                }
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        "optional": True
                    }
                ],
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
                ]
            }
        ]
    }
}

