"""
Generated from symbols.json for ::java::data::villager_trade::TradeCost
Local link to file: vanilla_mcdoc/data/villager_trade/TradeCost.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate
from vanilla_mcdoc.world.item.SingleItemOfComponent import SingleItemOfComponent

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProvider import IntNumberProvider


class TradeCost(SingleItemOfComponent[DataComponentExactPredicate]):
    count: IntNumberProvider | None = None  # Defaults to `1`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::villager_trade::TradeCost": {
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
                "desc": "Defaults to `1`.",
                "key": "count",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::IntNumberProvider"
                },
                "optional": True
            }
        ]
    }
}
