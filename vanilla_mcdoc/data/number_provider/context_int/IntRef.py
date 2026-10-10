"""
Generated from symbols.json for ::java::data::number_provider::context_int::IntRef
Local link to file: vanilla_mcdoc/data/number_provider/context_int/IntRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider import ContextIntProvider
    from vanilla_mcdoc.registry.KnownContextIntProviderId import KnownContextIntProviderId


type IntRef = Annotated[str, IdSpec(registry='context_int_provider')] | KnownContextIntProviderId | ContextIntProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::context_int::IntRef": {
        "kind": "union",
        "members": [
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
            },
            {
                "kind": "reference",
                "path": "::java::data::number_provider::context_int::ContextIntProvider"
            }
        ]
    }
}
