# Generated from symbols.json for ::java::world::component::item::WritableBookContent
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.Filterable import Filterable


@dataclass(kw_only=True)
class WritableBookContent:
    pages: list[Filterable[str]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::WritableBookContent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
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
            }
        ]
    }
}

