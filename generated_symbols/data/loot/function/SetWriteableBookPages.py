# Generated from symbols.json for ::java::data::loot::function::SetWriteableBookPages
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.ListOperation import ListOperation

if TYPE_CHECKING:
    from generated_symbols.util.Filterable import Filterable


@dataclass(kw_only=True)
class SetWriteableBookPages(ListOperation, Conditions):
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.


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

