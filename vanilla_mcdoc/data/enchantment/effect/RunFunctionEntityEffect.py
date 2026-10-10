"""
Generated from symbols.json for ::java::data::enchantment::effect::RunFunctionEntityEffect
Local link to file: generated_symbols/data/enchantment/effect/RunFunctionEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec


class RunFunctionEntityEffect(GeneratedModel):
    function: Annotated[str, IdSpec(registry='function')]


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
