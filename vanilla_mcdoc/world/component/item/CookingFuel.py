"""
Generated from symbols.json for ::java::world::component::item::CookingFuel
Local link to file: generated_symbols/world/component/item/CookingFuel.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownContextFloatProviderId import KnownContextFloatProviderId
    from generated_symbols.registry.KnownContextIntProviderId import KnownContextIntProviderId


class CookingFuel(GeneratedModel):
    burn_time: int | Annotated[str, IdSpec(registry='context_int_provider')] | KnownContextIntProviderId
    speed_multiplier: float | Annotated[str, IdSpec(registry='context_float_provider')] | KnownContextFloatProviderId


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::CookingFuel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "burn_time",
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
            },
            {
                "kind": "pair",
                "key": "speed_multiplier",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "float"
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
                                            "value": "context_float_provider"
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
