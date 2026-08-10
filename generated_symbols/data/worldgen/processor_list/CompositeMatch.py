"""
Generated from symbols.json for ::java::data::worldgen::processor_list::CompositeMatch
Local link to file: generated_symbols/data/worldgen/processor_list/CompositeMatch.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.RuleTest import RuleTest


@dataclass(kw_only=True)
class CompositeMatch:
    rules: list[RuleTest]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::CompositeMatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "rules",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::processor_list::RuleTest"
                    }
                }
            }
        ]
    }
}

