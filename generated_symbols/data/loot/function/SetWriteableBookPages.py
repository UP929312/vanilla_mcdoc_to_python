"""
Generated from symbols.json for ::java::data::loot::function::SetWriteableBookPages
Local link to file: generated_symbols/data/loot/function/SetWriteableBookPages.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation

if TYPE_CHECKING:
    from generated_symbols.util.Filterable import Filterable


@dataclass(kw_only=True)
class SetWriteableBookPagesAppend(Conditions):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class SetWriteableBookPagesInsert(Conditions, InsertListOperation):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class SetWriteableBookPagesReplaceAll(Conditions):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class SetWriteableBookPagesReplaceSection(Conditions, ReplaceSectionListOperation):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.


type SetWriteableBookPages = SetWriteableBookPagesAppend | SetWriteableBookPagesInsert | SetWriteableBookPagesReplaceAll | SetWriteableBookPagesReplaceSection


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetWriteableBookPages": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Sets the pages of a book and quill.",
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
                                "kind": "string"
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

