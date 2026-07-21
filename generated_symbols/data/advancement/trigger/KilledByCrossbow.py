# Generated from symbols.json for ::java::data::advancement::trigger::KilledByCrossbow
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.advancement.trigger.TriggerBase import TriggerBase

if TYPE_CHECKING:
    from generated_symbols.data.advancement.trigger.CompositeEntity import CompositeEntity
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class KilledByCrossbow(TriggerBase):
    unique_entity_types: MinMaxBounds[int] | int | None = None  # How many different types of entities were killed.
    victims: list[CompositeEntity] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::KilledByCrossbow": {
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
                "desc": "How many different types of entities were killed.",
                "key": "unique_entity_types",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
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

