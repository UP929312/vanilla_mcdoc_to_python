"""
Generated from symbols.json for ::java::data::enchantment::effect::RunFunctionEntityEffect
Local link to file: vanilla_mcdoc/data/enchantment/effect/RunFunctionEntityEffect.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


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
