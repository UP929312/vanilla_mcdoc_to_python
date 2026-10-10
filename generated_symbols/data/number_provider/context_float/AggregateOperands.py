"""
Generated from symbols.json for ::java::data::number_provider::context_float::AggregateOperands
Local link to file: generated_symbols/data/number_provider/context_float/AggregateOperands.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.context_float.ContextFloatProvider import ContextFloatProvider
    from generated_symbols.data.number_provider.context_float.FloatRef import FloatRef
    from generated_symbols.registry.KnownContextFloatProviderId import KnownContextFloatProviderId


type AggregateOperands = ContextFloatProvider | Annotated[str, IdSpec(registry='context_float_provider', tags='allowed')] | KnownContextFloatProviderId | Annotated[list[FloatRef], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::context_float::AggregateOperands": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::number_provider::context_float::ContextFloatProvider"
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "id",
                        "value": {
                            "kind": "tree",
                            "values": {
                                "registry": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "context_float_provider"
                                    }
                                },
                                "tags": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "allowed"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::context_float::FloatRef"
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 1
                }
            }
        ]
    }
}

