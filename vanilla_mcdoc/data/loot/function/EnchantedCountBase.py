"""
Generated from symbols.json for ::java::data::loot::function::EnchantedCountBase
Local link to file: vanilla_mcdoc/data/loot/function/EnchantedCountBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.FloatNumberProviderRef import FloatNumberProviderRef


class EnchantedCountBase(GeneratedModel):
    count: FloatNumberProviderRef  # Rounded *after* the number was multiplied by the looting level.
    limit: int | None = None  # Limits the count of the item to a range.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::EnchantedCountBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Rounded *after* the number was multiplied by the looting level.",
                "key": "count",
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
                            "path": "::java::data::number_provider::FloatNumberProviderRef",
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
            },
            {
                "kind": "pair",
                "desc": "Limits the count of the item to a range.",
                "key": "limit",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
