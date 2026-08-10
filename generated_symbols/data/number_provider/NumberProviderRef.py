"""
Generated from symbols.json for ::java::data::number_provider::NumberProviderRef
Local link to file: generated_symbols/data/number_provider/NumberProviderRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProvider import NumberProvider


type NumberProviderRef = NumberProvider | Annotated[str, IdSpec(registry='number_provider')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::NumberProviderRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::number_provider::NumberProvider"
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    },
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

