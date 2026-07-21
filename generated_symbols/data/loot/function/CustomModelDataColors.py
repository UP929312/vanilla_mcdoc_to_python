# Generated from symbols.json for ::java::data::loot::function::CustomModelDataColors
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.loot.function.ListOperation import ListOperation

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class CustomModelDataColors(ListOperation):
    values: list[NumberProviderRef | RGB]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CustomModelDataColors": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "values",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "union",
                        "members": [
                            {
                                "kind": "reference",
                                "path": "::java::data::number_provider::NumberProviderRef"
                            },
                            {
                                "kind": "reference",
                                "path": "::java::util::color::RGB"
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
            }
        ]
    }
}

