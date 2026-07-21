# Generated from symbols.json for ::java::assets::item_definition::Time
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.TimeSource import TimeSource


@dataclass(kw_only=True)
class Time:
    source: TimeSource
    wobble: bool | None = None  # Whether to oscillate for some time around target before settling. Defaults to true.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Time": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "source",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::TimeSource"
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

