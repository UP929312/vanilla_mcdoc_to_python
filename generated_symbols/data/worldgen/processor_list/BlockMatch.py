# Generated from symbols.json for ::java::data::worldgen::processor_list::BlockMatch
from dataclasses import dataclass


@dataclass(kw_only=True)
class BlockMatch:
    block: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::BlockMatch": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "block",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

