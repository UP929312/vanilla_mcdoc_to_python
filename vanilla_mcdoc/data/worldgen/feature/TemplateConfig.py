"""
Generated from symbols.json for ::java::data::worldgen::feature::TemplateConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/TemplateConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.TemplateEntry import TemplateEntry
    from vanilla_mcdoc.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef
    from vanilla_mcdoc.util.WeightedList import WeightedList


class TemplateConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

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
