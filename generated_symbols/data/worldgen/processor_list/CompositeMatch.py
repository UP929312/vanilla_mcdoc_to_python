"""
Generated from symbols.json for ::java::data::worldgen::processor_list::CompositeMatch
Local link to file: generated_symbols/data/worldgen/processor_list/CompositeMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.RuleTest import RuleTest


class CompositeMatch(GeneratedModel):
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

