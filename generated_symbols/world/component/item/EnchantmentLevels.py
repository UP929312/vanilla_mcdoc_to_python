# Generated from symbols.json for ::java::world::component::item::EnchantmentLevels
from typing import Annotated


type EnchantmentLevels = dict[str, Annotated[int, 'Range | `1`-`255` | both inclusive']]


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

