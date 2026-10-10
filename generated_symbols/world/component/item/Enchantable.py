"""
Generated from symbols.json for ::java::world::component::item::Enchantable
Local link to file: generated_symbols/world/component/item/Enchantable.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel


class Enchantable(GeneratedModel):
    value: Annotated[int, Field(ge=1)]


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
