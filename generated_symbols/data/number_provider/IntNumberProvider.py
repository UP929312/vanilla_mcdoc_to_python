"""
Generated from symbols.json for ::java::data::number_provider::IntNumberProvider
Local link to file: generated_symbols/data/number_provider/IntNumberProvider.py
"""
# ~~~ CODE ~~~
from generated_symbols.data.number_provider.context_int.ContextIntProvider import ContextIntProvider


type IntNumberProvider = ContextIntProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::IntNumberProvider": {
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
                "path": "::java::data::number_provider::context_int::ContextIntProvider",
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
