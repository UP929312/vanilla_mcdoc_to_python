# Generated from symbols.json for ::java::data::worldgen::processor_list::InvertedMatch
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.RuleTest import RuleTest


@dataclass(kw_only=True)
class InvertedMatch:
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

