"""
Generated from symbols.json for ::java::data::number_provider::ResolvableNumber
Local link to file: generated_symbols/data/number_provider/ResolvableNumber.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.registry.KnownNumberProviderId import KnownNumberProviderId


type ResolvableNumber = float | Annotated[str, IdSpec(registry='number_provider')] | KnownNumberProviderId


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::ResolvableNumber": {
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
                                "value": "number_provider"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

