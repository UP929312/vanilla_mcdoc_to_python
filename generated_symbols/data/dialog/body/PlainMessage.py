# Generated from symbols.json for ::java::data::dialog::body::PlainMessage
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class PlainMessage:
    contents: Text  # A multiline label. Click events in the text trigger `after_action` like any other action.
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Maximum width of message. Defaults to 200.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::body::PlainMessage": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "A multiline label.\nClick events in the text trigger `after_action` like any other action.",
                "key": "contents",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "desc": "Maximum width of message.\nDefaults to 200.",
                "key": "width",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 1024
                    }
                },
                "optional": True
            }
        ]
    }
}

