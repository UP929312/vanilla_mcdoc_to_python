"""
Generated from symbols.json for ::java::data::worldgen::processor_list::InvertedMatch
Local link to file: generated_symbols/data/worldgen/processor_list/InvertedMatch.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.RuleTest import RuleTest


class InvertedMatch(GeneratedModel):
    rule: RuleTest


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::InvertedMatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "rule",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::RuleTest"
                }
            }
        ]
    }
}

