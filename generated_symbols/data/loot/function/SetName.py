# Generated from symbols.json for ::java::data::loot::function::SetName
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.data.loot.function.SetNameTarget import SetNameTarget
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class SetName(Conditions):
    name: Text
    entity: EntityTarget | None = None  # Specifies the entity to act as the target `@s` in the JSON text component.
    target: SetNameTarget | None = None  # Which name component to set. Defaults to `custom_name`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetName": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Specifies the entity to act as the target `@s` in the JSON text component.",
                "key": "entity",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::EntityTarget"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "name",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Which name component to set. Defaults to `custom_name`.",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::SetNameTarget"
                },
                "optional": True
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

