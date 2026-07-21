# Generated from symbols.json for ::java::assets::shader::post::PostEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.shader.post.Pass import Pass
    from generated_symbols.assets.shader.post.Targets import Targets


@dataclass(kw_only=True)
class PostEffect:
    targets: Targets | None = None
    passes: list[Pass] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::PostEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "targets",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "list",
                            "item": {
                                "kind": "union",
                                "members": [
                                    {
                                        "kind": "string"
                                    },
                                    {
                                        "kind": "reference",
                                        "path": "::java::assets::shader::post::OldTarget"
                                    }
                                ]
                            },
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
                            "kind": "reference",
                            "path": "::java::assets::shader::post::Targets",
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
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "passes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::shader::post::Pass"
                    }
                },
                "optional": True
            }
        ]
    }
}

