"""
Generated from symbols.json for ::java::util::text::TextBase
Local link to file: generated_symbols/util/text/TextBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.util.text.TextStyle import TextStyle

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


class TextBase(TextStyle):
    extra: Annotated[list[Text], Field(min_length=1)] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::TextBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "extra",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::text::Text"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::TextStyle"
                }
            }
        ]
    }
}
