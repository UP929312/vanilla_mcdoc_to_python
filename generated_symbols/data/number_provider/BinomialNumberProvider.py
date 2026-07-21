# Generated from symbols.json for ::java::data::number_provider::BinomialNumberProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef


@dataclass(kw_only=True)
class BinomialNumberProvider:
    n: NumberProviderRef
    p: NumberProviderRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::number_provider::BinomialNumberProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "n",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderRef"
                }
            },
            {
                "kind": "pair",
                "key": "p",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::number_provider::NumberProviderRef"
                }
            }
        ]
    }
}

