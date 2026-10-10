"""
Generated from symbols.json for ::java::world::component::item::BrewingFuel
Local link to file: generated_symbols/world/component/item/BrewingFuel.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownContextFloatProviderId import KnownContextFloatProviderId
    from generated_symbols.registry.KnownContextIntProviderId import KnownContextIntProviderId


class BrewingFuel(GeneratedModel):
    uses: int | Annotated[str, IdSpec(registry='context_int_provider')] | KnownContextIntProviderId  # Total recipes the fuel will brew before being consumed.
    speed_multiplier: float | Annotated[str, IdSpec(registry='context_float_provider')] | KnownContextFloatProviderId  # Controls the recipe brewing speed.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::BrewingFuel": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Total recipes the fuel will brew before being consumed.",
                "key": "uses",
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
                "desc": "Controls the recipe brewing speed.",
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
