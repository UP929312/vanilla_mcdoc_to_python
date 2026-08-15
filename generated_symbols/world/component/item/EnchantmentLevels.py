"""
Generated from symbols.json for ::java::world::component::item::EnchantmentLevels
Local link to file: generated_symbols/world/component/item/EnchantmentLevels.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from minecraft_registry import IdSpec


type EnchantmentLevels = dict[Annotated[str, IdSpec(registry='enchantment')], Annotated[int, 'Range | `1`-`255` | both inclusive']]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::EnchantmentLevels": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "enchantment"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 255
                    }
                }
            }
        ]
    }
}

