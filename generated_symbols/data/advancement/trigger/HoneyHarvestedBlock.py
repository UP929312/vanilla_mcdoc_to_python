"""
Generated from symbols.json for ::java::data::advancement::trigger::HoneyHarvestedBlock
Local link to file: generated_symbols/data/advancement/trigger/HoneyHarvestedBlock.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class HoneyHarvestedBlock:
    block: Annotated[str, IdSpec(registry='block')] | None = None
    tag: Annotated[str, IdSpec(registry='block', tags='implicit')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::trigger::HoneyHarvestedBlock": {
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
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "tag",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "block"
                                        }
                                    },
                                    "tags": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "implicit"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

