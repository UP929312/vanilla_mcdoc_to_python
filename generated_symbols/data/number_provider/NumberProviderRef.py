# Generated from symbols.json for ::java::data::number_provider::NumberProviderRef
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProvider import NumberProvider


type NumberProviderRef = NumberProvider | str


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

