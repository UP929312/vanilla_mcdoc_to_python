# Generated from symbols.json for ::java::assets::item_definition::DyeTint
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ActuallyTranslucentRGB import ActuallyTranslucentRGB


@dataclass(kw_only=True)
class DyeTint:
    default: ActuallyTranslucentRGB  # Tint to apply when the `dyed_color` component is not present.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::DyeTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Tint to apply when the `dyed_color` component is not present.",
                "key": "default",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::ActuallyTranslucentRGB"
                }
            }
        ]
    }
}

