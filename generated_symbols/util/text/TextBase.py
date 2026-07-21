# Generated from symbols.json for ::java::util::text::TextBase
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.util.text.TextStyle import TextStyle

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class TextBase(TextStyle):
    extra: Annotated[list[Text], 'Length = 1 (inclusive) and above'] | None = None


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

