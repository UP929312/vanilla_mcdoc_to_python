"""
Generated from symbols.json for ::java::world::component::item::Compostable
Local link to file: generated_symbols/world/component/item/Compostable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.ResolvableNumber import ResolvableNumber


class Compostable(GeneratedModel):
    layers: ResolvableNumber


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Compostable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "layers",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::ResolvableNumber"
                }
            }
        ]
    }
}

