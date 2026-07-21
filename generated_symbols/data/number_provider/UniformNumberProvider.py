# Generated from symbols.json for ::java::data::number_provider::UniformNumberProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class UniformNumberProvider:
    min: NumberProviderRef | None = None
    max: NumberProviderRef | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::UniformNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "min",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "max",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderRef"
                },
                "optional": True
            }
        ]
    }
}

