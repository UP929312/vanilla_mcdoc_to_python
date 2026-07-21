# Generated from symbols.json for ::java::world::component::item::VillagerFood
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class VillagerFood:
    nutrition: Annotated[int, 'Range | Min `1` and above | inclusive']  # How much hunger the item satiates in the Villager once eaten.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::VillagerFood": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "How much hunger the item satiates in the Villager once eaten.",
                "key": "nutrition",
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

