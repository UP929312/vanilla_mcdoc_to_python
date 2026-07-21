# Generated from symbols.json for ::java::data::loot::function::SetWrittenBookPages
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.ListOperation import ListOperation

if TYPE_CHECKING:
    from generated_symbols.util.Filterable import Filterable
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class SetWrittenBookPages(ListOperation, Conditions):
    pages: list[Filterable[Text]]  # Sets the pages of a written book.


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

