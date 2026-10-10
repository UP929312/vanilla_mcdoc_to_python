"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Rule
Local link to file: generated_symbols/data/worldgen/processor_list/Rule.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.ProcessorRule import ProcessorRule


class Rule(GeneratedModel):
    rules: list[ProcessorRule]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::Rule": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "rules",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::processor_list::ProcessorRule"
                    }
                }
            }
        ]
    }
}
