# Generated from symbols.json for ::java::world::component::item::ItemDamageFunction
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ItemDamageFunction:
    threshold: Annotated[float, 'Range | Min `0` and above | inclusive']  # Minimum amount of damage dealt by the attack before this item damage is applied to the item.
    base: float  # Constant amount of damage applied to the item, if `threshold` is passed.
    factor: float  # Fraction of the dealt damage that should be applied to the item, if `threshold` is passed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::ItemDamageFunction": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Minimum amount of damage dealt by the attack before this item damage is applied to the item.",
                "key": "threshold",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Constant amount of damage applied to the item, if `threshold` is passed.",
                "key": "base",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "Fraction of the dealt damage that should be applied to the item, if `threshold` is passed.",
                "key": "factor",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

