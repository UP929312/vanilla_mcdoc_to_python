# Generated from symbols.json for ::java::data::util::RandomIntGenerator
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.RandomIntGeneratorType import RandomIntGeneratorType


@dataclass(kw_only=True)
class RandomIntGeneratorStruct1:
    type: RandomIntGeneratorType | None = None

type RandomIntGenerator = int | RandomIntGeneratorStruct1


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::RandomIntGenerator": {
        "kind": "union",
        "members": [
            {
                "kind": "int"
            },
            {
                "kind": "struct",
                "fields": [
                    {
                        "kind": "pair",
                        "key": "type",
                        "type": {
                            "kind": "reference",
                            "path": "::java::data::util::RandomIntGeneratorType"
                        },
                        "optional": True
                    },
                    {
                        "kind": "spread",
                        "type": {
                            "kind": "dispatcher",
                            "parallelIndices": [
                                {
                                    "kind": "dynamic",
                                    "accessor": [
                                        "type"
                                    ]
                                }
                            ],
                            "registry": "minecraft:random_int_generator"
                        }
                    }
                ]
            }
        ]
    }
}

