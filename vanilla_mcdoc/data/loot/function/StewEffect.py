"""
Generated from symbols.json for ::java::data::loot::function::StewEffect
Local link to file: vanilla_mcdoc/data/loot/function/StewEffect.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class StewEffect(GeneratedModel):
    type: Annotated[str, IdSpec(registry='mob_effect')]  # The status effect of this stew effect.
    duration: IntNumberProviderRef  # The duration of this stew effect, in seconds.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::StewEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The status effect of this stew effect.",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "mob_effect"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "The duration of this stew effect, in seconds.",
                "key": "duration",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::util::RandomValueBounds",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::number_provider::IntNumberProviderRef",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.17"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
