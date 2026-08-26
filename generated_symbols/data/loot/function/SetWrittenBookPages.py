"""
Generated from symbols.json for ::java::data::loot::function::SetWrittenBookPages
Local link to file: generated_symbols/data/loot/function/SetWrittenBookPages.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.util.Filterable import Filterable
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class SetWrittenBookPagesAppend(Conditions):
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class SetWrittenBookPagesInsert(Conditions):
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class SetWrittenBookPagesReplaceAll(Conditions):
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class SetWrittenBookPagesReplaceSection(Conditions):
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type SetWrittenBookPages = SetWrittenBookPagesAppend | SetWrittenBookPagesInsert | SetWrittenBookPagesReplaceAll | SetWrittenBookPagesReplaceSection


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetWrittenBookPages": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Sets the pages of a written book.",
                "key": "pages",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "concrete",
                        "child": {
                            "kind": "reference",
                            "path": "::java::util::Filterable"
                        },
                        "typeArgs": [
                            {
                                "kind": "reference",
                                "path": "::java::util::text::Text"
                            }
                        ]
                    }
                }
            },
            {
                "kind": "spread",
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

