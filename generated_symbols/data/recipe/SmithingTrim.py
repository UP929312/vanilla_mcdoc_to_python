"""
Generated from symbols.json for ::java::data::recipe::SmithingTrim
Local link to file: generated_symbols/data/recipe/SmithingTrim.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from generated_symbols.data.recipe.NotificationInfo import NotificationInfo
from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.recipe.Ingredient import Ingredient


@dataclass(kw_only=True)
class SmithingTrim(NotificationInfo):
    base: Ingredient  # Ingredient specifying an item to be trimmed.
    addition: Ingredient  # Material that will be used.
    template: Ingredient  # Template item that will be used for the pattern.
    pattern: Annotated[str, IdSpec(registry='trim_pattern')]  # The trim pattern to apply to the result item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::SmithingTrim": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::NotificationInfo"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "deprecated"
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "This field is unused by the game.",
                "key": "group",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ingredient specifying an item to be trimmed.",
                "key": "base",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::recipe::Ingredient"
                }
            },
            {
                "kind": "pair",
                "desc": "Material that will be used.",
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
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "The trim pattern to apply to the result item.",
                "key": "pattern",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "trim_pattern"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

