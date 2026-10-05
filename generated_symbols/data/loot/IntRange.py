"""
Generated from symbols.json for ::java::data::loot::IntRange
Local link to file: generated_symbols/data/loot/IntRange.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.IntNumberProviderRef import IntNumberProviderRef


class IntRangeStruct(GeneratedModel):
    min: IntNumberProviderRef | None = None
    max: IntNumberProviderRef | None = None


type IntRange = IntNumberProviderRef | IntRangeStruct


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::IntRange": {
        "kind": "union",
        "members": [
            {
                "kind": "int",
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
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "min",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::number_provider::LegacyNumberProvider"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "key": "max",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::number_provider::LegacyNumberProvider"
                        },
                        "optional": True
                    }
                ],
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
                "path": "::java::data::number_provider::IntNumberProviderRef",
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
}

