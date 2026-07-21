# Generated from symbols.json for ::java::world::item::TradeCost
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.item.SingleItemOfComponent import SingleItemOfComponent

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProvider import NumberProvider
    from generated_symbols.world.component.DataComponentExactPredicate import DataComponentExactPredicate


@dataclass(kw_only=True)
class TradeCost(SingleItemOfComponent[DataComponentExactPredicate]):
    count: NumberProvider | None = None  # Number of items in the stack. Defaults to `1`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::TradeCost": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::world::item::SingleItemOfComponent"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::world::component::DataComponentExactPredicate"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Number of items in the stack.\nDefaults to `1`.",
                "key": "count",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProvider"
                },
                "optional": True
            }
        ]
    }
}

