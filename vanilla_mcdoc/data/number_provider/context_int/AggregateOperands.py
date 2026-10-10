"""
Generated from symbols.json for ::java::data::number_provider::context_int::AggregateOperands
Local link to file: vanilla_mcdoc/data/number_provider/context_int/AggregateOperands.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProvider
    from vanilla_mcdoc.data.number_provider.context_int.IntRef import IntRef
    from vanilla_mcdoc.registry.KnownContextIntProviderId import KnownContextIntProviderId


type AggregateOperands = ContextIntProvider | Annotated[str, IdSpec(registry='context_int_provider', tags='allowed')] | KnownContextIntProviderId | Annotated[list[IntRef], Field(min_length=1)]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::context_int::AggregateOperands": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::number_provider::context_int::ContextIntProvider"
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
                                        "value": "context_int_provider"
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
                    "path": "::java::data::number_provider::context_int::IntRef"
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 1
                }
            }
        ]
    }
}
