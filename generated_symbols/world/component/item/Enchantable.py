"""
Generated from symbols.json for ::java::world::component::item::Enchantable
Local link to file: generated_symbols/world/component/item/Enchantable.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class Enchantable:
    value: Annotated[int, 'Range | `1` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Enchantable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "value",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

