# Generated from symbols.json for ::java::data::advancement::trigger::ChanneledLightning
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity


@dataclass(kw_only=True)
class ChanneledLightning(TriggerBase):
    victims: list[CompositeEntity] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::ChanneledLightning": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::trigger::TriggerBase"
                }
            },
            {
                "kind": "pair",
                "key": "victims",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::advancement::trigger::CompositeEntity"
                    }
                },
                "optional": True
            }
        ]
    }
}

