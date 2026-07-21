# Generated from symbols.json for ::java::assets::atlas::Filter
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.atlas.FilterPattern import FilterPattern


@dataclass(kw_only=True)
class Filter:
    pattern: FilterPattern  # Pattern to remove sprite identifiers already in the atlas. The order of sprite sources is important.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::Filter": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Pattern to remove sprite identifiers already in the atlas. The order of sprite sources is important.",
                "key": "pattern",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::atlas::FilterPattern"
                }
            }
        ]
    }
}

