"""
Generated from symbols.json for ::java::data::loot::function::LimitCount
Local link to file: vanilla_mcdoc/data/loot/function/LimitCount.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class LimitStruct(GeneratedModel):
    min: IntNumberProviderRef | None = None
    max: IntNumberProviderRef | None = None


class LimitCount(Conditions):
    limit: LimitStruct  # Limits the count of the item to a range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::LimitCount": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Limits the count of the item to a range.",
                "key": "limit",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::util::IntLimiter",
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
                            "path": "::java::data::loot::IntRange",
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
                                },
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
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": "min",
                                    "type": {
                                        "kind": "reference",
                                        "path": "::java::data::number_provider::IntNumberProviderRef"
                                    },
                                    "optional": True
                                },
                                {
                                    "kind": "pair",
                                    "key": "max",
                                    "type": {
                                        "kind": "reference",
                                        "path": "::java::data::number_provider::IntNumberProviderRef"
                                    },
                                    "optional": True
                                }
                            ],
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
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}
