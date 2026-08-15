"""
Generated from symbols.json for ::java::data::loot::function::SetWriteableBookPages
Local link to file: generated_symbols/data/loot/function/SetWriteableBookPages.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from generated_symbols.util.Filterable import Filterable


@dataclass(kw_only=True)
class SetWriteableBookPagesAppend(Conditions):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class SetWriteableBookPagesInsert(Conditions):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class SetWriteableBookPagesReplaceAll(Conditions):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class SetWriteableBookPagesReplaceSection(Conditions):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


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

