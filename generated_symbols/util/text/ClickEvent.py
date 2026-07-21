# Generated from symbols.json for ::java::util::text::ClickEvent
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.ClickEventAction import ClickEventAction


@dataclass(kw_only=True)
class ClickEvent:
    action: ClickEventAction


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ClickEvent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "action",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::ClickEventAction"
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
                    "registry": "minecraft:click_event"
                }
            }
        ]
    }
}

