# Generated from symbols.json for ::java::assets::item_definition::Compass
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.CompassTarget import CompassTarget


@dataclass(kw_only=True)
class Compass:
    target: CompassTarget
    wobble: bool | None = None  # Whether to oscillate for some time around target before settling. Defaults to true.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Compass": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::CompassTarget"
                }
            },
            {
                "kind": "pair",
                "desc": "Whether to oscillate for some time around target before settling. Defaults to True.",
                "key": "wobble",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

