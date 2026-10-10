"""
Generated from symbols.json for ::java::world::component::item::Compostable
Local link to file: generated_symbols/world/component/item/Compostable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownContextIntProviderId import KnownContextIntProviderId


class Compostable(GeneratedModel):
    layers: int | Annotated[str, IdSpec(registry='context_int_provider')] | KnownContextIntProviderId


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Compostable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "layers",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int"
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "context_int_provider"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
