"""
Generated from symbols.json for ::java::data::loot::function::SetLore
Local link to file: generated_symbols/data/loot/function/SetLore.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class SetLoreAppend(Conditions):
    lore: list[Text]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.
    entity: EntityTarget | None = None  # The entity used to resolve the text components.


@dataclass(kw_only=True)
class SetLoreInsert(Conditions):
    lore: list[Text]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class SetLoreReplaceAll(Conditions):
    lore: list[Text]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.
    entity: EntityTarget | None = None  # The entity used to resolve the text components.


@dataclass(kw_only=True)
class SetLoreReplaceSection(Conditions):
    lore: list[Text]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type SetLore = SetLoreAppend | SetLoreInsert | SetLoreReplaceAll | SetLoreReplaceSection


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

