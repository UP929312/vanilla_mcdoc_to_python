"""
Generated from symbols.json for ::java::data::number_provider::IntNumberProviderRef
Local link to file: generated_symbols/data/number_provider/IntNumberProviderRef.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.number_provider.context_int.IntRef import IntRef


type IntNumberProviderRef = IntRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::IntNumberProviderRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::number_provider::legacy::LegacyNumberProvider",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::number_provider::context_int::IntRef",
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
                    }
                ]
            }
        ]
    }
}
