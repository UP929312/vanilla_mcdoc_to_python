# Generated from symbols.json for ::java::util::text::Text
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.text.TextObject import TextObject


type Text = str | TextObject | Annotated[list[Text], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::Text": {
        "kind": "union",
        "members": [
            {
                "kind": "string"
            },
            {
                "kind": "reference",
                "path": "::java::util::text::TextObject"
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 1
                }
            }
        ]
    }
}

