# Generated from symbols.json for ::java::pack::PackFilter
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.pack.BlockPattern import BlockPattern


@dataclass(kw_only=True)
class PackFilter:
    block: list[BlockPattern]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::PackFilter": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::pack::BlockPattern"
                    }
                }
            }
        ]
    }
}

