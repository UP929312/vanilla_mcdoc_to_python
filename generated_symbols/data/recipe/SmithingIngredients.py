# Generated from symbols.json for ::java::data::recipe::SmithingIngredients
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient


@dataclass(kw_only=True)
class SmithingIngredients:
    base: Ingredient | None = None  # Ingredient specifying an item to be trimmed. (eg. `"#minecraft:trimmable_armor"`)
    addition: Ingredient | None = None  # Material that will be used. (eg. `"#minecraft:trim_materials"`)
    template: Ingredient | None = None  # Template item that will be used for the pattern.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::SmithingIngredients": {
        "kind": "union",
        "members": [
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Ingredient specifying an item to be trimmed. (eg. `{ \"tag\": \"minecraft:trimmable_armor\" }`)",
                        "key": "base",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::recipe::Ingredient"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Material that will be used. (eg. `{ \"tag\": \"minecraft:trim_materials\" }`)",
                        "key": "addition",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::recipe::Ingredient"
                        }
                    },
                    {
                        "kind": "pair",
                        "desc": "Template item that will be used for the pattern.",
                        "key": "template",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::recipe::Ingredient"
                        }
                    }
                ],
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
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Ingredient specifying an item to be trimmed. (eg. `\"#minecraft:trimmable_armor\"`)",
                        "key": "base",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::recipe::Ingredient"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Material that will be used. (eg. `\"#minecraft:trim_materials\"`)",
                        "key": "addition",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::recipe::Ingredient"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Template item that will be used for the pattern.",
                        "key": "template",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::recipe::Ingredient"
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
                                "value": "1.21.2"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

