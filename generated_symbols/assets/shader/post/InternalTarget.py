# Generated from symbols.json for ::java::assets::shader::post::InternalTarget
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGBA import RGBA


@dataclass(kw_only=True)
class InternalTarget:
    width: int | None = None
    height: int | None = None
    persistent: bool | None = None  # If `true`, target will be persistent across frames. Defaults to `false`. The contents of the target will be cleared when the screen is resized.
    clear_color: RGBA | None = None  # Target will be filled with this color when created or cleared. Defaults to `0`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::post::InternalTarget": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "width",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "height",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If `True`, target will be persistent across frames. Defaults to `False`.\nThe contents of the target will be cleared when the screen is resized.",
                "key": "persistent",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Target will be filled with this color when created or cleared. Defaults to `0`.",
                "key": "clear_color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGBA"
                },
                "optional": True
            }
        ]
    }
}

