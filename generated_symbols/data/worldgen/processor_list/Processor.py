# Generated from symbols.json for ::java::data::worldgen::processor_list::Processor
from dataclasses import dataclass


@dataclass(kw_only=True)
class Processor:
    processor_type: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::Processor": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "processor_type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/structure_processor"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "processor_type"
                            ]
                        }
                    ],
                    "registry": "minecraft:template_processor"
                }
            }
        ]
    }
}

