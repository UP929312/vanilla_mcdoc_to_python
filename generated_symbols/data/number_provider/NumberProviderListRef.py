"""
Generated from symbols.json for ::java::data::number_provider::NumberProviderListRef
Local link to file: generated_symbols/data/number_provider/NumberProviderListRef.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProvider import NumberProvider
    from generated_symbols.registry.KnownNumberProviderId import KnownNumberProviderId


type NumberProviderListRef = NumberProvider | Annotated[str, IdSpec(registry='number_provider', tags='allowed')] | KnownNumberProviderId | list[Annotated[str, IdSpec(registry='number_provider')] | KnownNumberProviderId | NumberProvider]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::NumberProviderListRef": {
        "kind": "union",
        "members": [
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProvider"
                },
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
                "path": "::java::data::number_provider::NumberProvider",
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
                "kind": "string",
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
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "tree",
                            "values": {
                                "registry": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "number_provider"
                                    }
                                },
                                "tags": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "allowed"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "number_provider"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::number_provider::NumberProvider"
                        }
                    ]
                },
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

