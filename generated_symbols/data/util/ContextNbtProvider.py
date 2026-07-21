# Generated from symbols.json for ::java::data::util::ContextNbtProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.NbtContextTarget import NbtContextTarget


@dataclass(kw_only=True)
class ContextNbtProvider:
    target: NbtContextTarget


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::ContextNbtProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::NbtContextTarget"
                }
            }
        ]
    }
}

