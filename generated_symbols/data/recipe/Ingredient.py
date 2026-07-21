# Generated from symbols.json for ::java::data::recipe::Ingredient
from typing import Annotated


type Ingredient = Annotated[list[str], 'Length = 1 (inclusive) and above'] | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::Ingredient": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::recipe::IngredientValue",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::data::recipe::IngredientValue"
                },
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "list",
                "item": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "item"
                                        }
                                    },
                                    "exclude": {
                                        "kind": "tree",
                                        "values": {
                                            "0": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "air"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 1
                },
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
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
                                "value": "1.21.2"
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
                                        "value": "item"
                                    }
                                },
                                "tags": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "allowed"
                                    }
                                },
                                "exclude": {
                                    "kind": "tree",
                                    "values": {
                                        "0": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "air"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                ]
            }
        ]
    }
}

