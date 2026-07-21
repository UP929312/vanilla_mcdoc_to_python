# Generated from symbols.json for ::java::data::loot::function::SetLore
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.ListOperation import ListOperation

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class SetLore(ListOperation, Conditions):
    lore: list[Text]
    entity: EntityTarget | None = None  # The entity used to resolve the text components.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetLore": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The entity used to resolve the text components.",
                "key": "entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::EntityTarget"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "lore",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::text::Text"
                    }
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Whether to replace the existing lore list. Defaults to True.",
                "key": "replace",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::ListOperation"
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

