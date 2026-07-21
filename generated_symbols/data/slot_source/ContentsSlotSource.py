# Generated from symbols.json for ::java::data::slot_source::ContentsSlotSource
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.function.ContainerComponents import ContainerComponents
    from generated_symbols.data.slot_source.SlotSource import SlotSource


@dataclass(kw_only=True)
class ContentsSlotSource:
    slot_source: SlotSource  # The slots to search.
    component: ContainerComponents  # If an item targeted by `slot_source` has this container component, selects all items inside.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::slot_source::ContentsSlotSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The slots to search.",
                "key": "slot_source",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::slot_source::SlotSource"
                }
            },
            {
                "kind": "pair",
                "desc": "If an item targeted by `slot_source` has this container component, selects all items inside.",
                "key": "component",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ContainerComponents",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            }
        ]
    }
}

