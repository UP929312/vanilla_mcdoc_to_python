# Generated from symbols.json for ::java::util::text::PlayerHeadText
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.text.ObjectTextConfig import ObjectTextConfig
from generated_symbols.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from generated_symbols.util.avatar.Profile import Profile


@dataclass(kw_only=True)
class PlayerHeadText(ObjectTextConfig, TextBase):
    player: Profile
    hat: bool | None = None  # Whether the head layer is rendered. Defaults to `true`.
    object: str | None = None
    type: str | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::PlayerHeadText": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "player",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::avatar::Profile"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether the head layer is rendered. Defaults to `True`.",
                "key": "hat",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::ObjectTextConfig"
                }
            },
            {
                "kind": "pair",
                "key": "object",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "player"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "object"
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::TextBase"
                }
            }
        ],
        "attributes": [
            {
                "name": "since",
                "value": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "1.21.9"
                    }
                }
            }
        ]
    }
}

