"""
Generated from symbols.json for ::java::data::number_provider::FloatNumberProvider
Local link to file: vanilla_mcdoc/data/number_provider/FloatNumberProvider.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider import ContextFloatProvider


type FloatNumberProvider = ContextFloatProvider


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::FloatNumberProvider": {
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
                "path": "::java::data::number_provider::context_float::ContextFloatProvider",
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
