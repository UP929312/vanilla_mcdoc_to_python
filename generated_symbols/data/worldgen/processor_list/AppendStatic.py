# Generated from symbols.json for ::java::data::worldgen::processor_list::AppendStatic
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class AppendStatic:
    data: Any


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::AppendStatic": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "data",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "parent"
                                },
                                "output_state",
                                "Name"
                            ]
                        }
                    ],
                    "registry": "minecraft:block"
                }
            }
        ]
    }
}

