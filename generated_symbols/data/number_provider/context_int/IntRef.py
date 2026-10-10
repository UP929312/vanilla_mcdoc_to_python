"""
Generated from symbols.json for ::java::data::number_provider::context_int::IntRef
Local link to file: generated_symbols/data/number_provider/context_int/IntRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.context_int.ContextIntProvider import ContextIntProvider
    from generated_symbols.registry.KnownContextIntProviderId import KnownContextIntProviderId


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
