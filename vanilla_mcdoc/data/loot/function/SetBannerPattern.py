"""
Generated from symbols.json for ::java::data::loot::function::SetBannerPattern
Local link to file: vanilla_mcdoc/data/loot/function/SetBannerPattern.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.loot.function.Conditions import Conditions

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.function.BannerPatternLayer import BannerPatternLayer


class SetBannerPattern(Conditions):
    patterns: list[BannerPatternLayer]  # List of banner pattern layers.
    append: bool  # Whether to add to the banner pattern list.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::SetBannerPattern": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "List of banner pattern layers.",
                "key": "patterns",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::loot::function::BannerPatternLayer"
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Whether to add to the banner pattern list.",
                "key": "append",
                "type": {
                    "kind": "boolean"
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
