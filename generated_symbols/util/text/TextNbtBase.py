# Generated from symbols.json for ::java::util::text::TextNbtBase
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class TextNbtBase(TextBase):
    interpret: bool | None = None
    plain: bool | None = None  # Whether to remove colors from pretty-printed NBT structure when `interpret` is `false`. Defaults to `false`.  Cannot be `true` when `interpret` is `true`.
    separator: Text | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::TextNbtBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "interpret",
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "Whether to remove colors from pretty-printed NBT structure when `interpret` is `False`.\nDefaults to `False`. \\\nCannot be `True` when `interpret` is `True`.",
                "key": "plain",
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
                                "value": "1.17"
                            }
                        }
                    }
                ],
                "key": "separator",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
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
        ]
    }
}

