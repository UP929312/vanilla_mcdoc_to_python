"""
Generated from symbols.json for ::java::data::number_provider::FloatNumberProviderRef
Local link to file: vanilla_mcdoc/data/number_provider/FloatNumberProviderRef.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.number_provider.context_float.FloatRef import FloatRef


type FloatNumberProviderRef = FloatRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::FloatNumberProviderRef": {
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
                "path": "::java::data::number_provider::context_float::FloatRef",
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
