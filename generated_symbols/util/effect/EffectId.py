"""
Generated from symbols.json for ::java::util::effect::EffectId
Local link to file: generated_symbols/util/effect/EffectId.py
"""
# ~~~ CODE ~~~
from generated_symbols.util.effect.EffectIntId import EffectIntId


type EffectId = EffectIntId


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::effect::EffectId": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::util::effect::EffectByteId",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::util::effect::EffectIntId",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

