# Generated from symbols.json for ::java::data::dialog::Button
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.dialog.action.ClickAction import ClickAction
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class Button:
    label: Text
    tooltip: Text | None = None
    width: Annotated[int, 'Range | `1`-`1024` | both inclusive'] | None = None  # Width of the button. Defaults to 150.
    action: ClickAction | None = None  # If not present, clicking button will simply close dialog without any action.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::Button": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "label",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "key": "tooltip",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Width of the button.\nDefaults to 150.",
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
            },
            {
                "kind": "pair",
                "desc": "If not present, clicking button will simply close dialog without any action.",
                "key": "action",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::dialog::action::ClickAction"
                },
                "optional": True
            }
        ]
    }
}

