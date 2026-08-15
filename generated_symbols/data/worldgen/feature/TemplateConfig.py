"""
Generated from symbols.json for ::java::data::worldgen::feature::TemplateConfig
Local link to file: generated_symbols/data/worldgen/feature/TemplateConfig.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.TemplateEntry import TemplateEntry
    from generated_symbols.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef
    from generated_symbols.util.WeightedList import WeightedList


@dataclass(kw_only=True)
class TemplateConfig:
    templates: WeightedList[TemplateEntry]
    processors: ProcessorListRef | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::TemplateConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "templates",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::WeightedList"
                    },
                    "typeArgs": [
                        {
                            "kind": "reference",
                            "path": "::java::data::worldgen::feature::TemplateEntry"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "processors",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::ProcessorListRef"
                },
                "optional": True
            }
        ]
    }
}

