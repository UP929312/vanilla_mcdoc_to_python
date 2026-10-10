"""
Generated from symbols.json for ::java::assets::shader::post::PostEffect
Local link to file: vanilla_mcdoc/assets/shader/post/PostEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.shader.post.Pass import Pass
    from vanilla_mcdoc.assets.shader.post.Targets import Targets


class PostEffect(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'post_effect'

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
