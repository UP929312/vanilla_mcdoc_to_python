# Generated from symbols.json for ::java::data::util::IntRange
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class IntRangeStruct1:
    min: NumberProviderRef | None = None  # Clamps to an integer.
    max: NumberProviderRef | None = None  # Clamps to an integer.

type IntRange = int | IntRangeStruct1


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::IntRange": {
        "kind": "union",
        "members": [
            {
                "kind": "int"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "desc": "Clamps to an integer.",
                        "key": "min",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::number_provider::NumberProviderRef"
                        },
                        "optional": True
                    },
                    {
                        "kind": "pair",
                        "desc": "Clamps to an integer.",
                        "key": "max",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::number_provider::NumberProviderRef"
                        },
                        "optional": True
                    }
                ]
            }
        ]
    }
}

