"""
Generated from symbols.json for ::java::data::number_provider::context_float::FloatRef
Local link to file: generated_symbols/data/number_provider/context_float/FloatRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.context_float.ContextFloatProvider import ContextFloatProvider
    from generated_symbols.registry.KnownContextFloatProviderId import KnownContextFloatProviderId


type FloatRef = Annotated[str, IdSpec(registry='context_float_provider')] | KnownContextFloatProviderId | ContextFloatProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::context_float::FloatRef": {
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
                                "value": "context_float_provider"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::number_provider::context_float::ContextFloatProvider"
            }
        ]
    }
}
