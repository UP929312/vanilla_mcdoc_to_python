# Generated from symbols.json for ::java::util::text::HoverEvent
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.HoverEventAction import HoverEventAction


@dataclass(kw_only=True)
class HoverEvent:
    action: HoverEventAction


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::HoverEvent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "action",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::HoverEventAction"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "action"
                            ]
                        }
                    ],
                    "registry": "minecraft:hover_event"
                }
            }
        ]
    }
}

