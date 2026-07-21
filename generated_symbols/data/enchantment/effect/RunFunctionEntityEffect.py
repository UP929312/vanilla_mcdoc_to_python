# Generated from symbols.json for ::java::data::enchantment::effect::RunFunctionEntityEffect
from dataclasses import dataclass


@dataclass(kw_only=True)
class RunFunctionEntityEffect:
    function: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::RunFunctionEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "function",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "function"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

