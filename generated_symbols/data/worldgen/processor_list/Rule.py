# Generated from symbols.json for ::java::data::worldgen::processor_list::Rule
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.ProcessorRule import ProcessorRule


@dataclass(kw_only=True)
class Rule:
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

