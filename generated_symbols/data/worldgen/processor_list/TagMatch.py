# Generated from symbols.json for ::java::data::worldgen::processor_list::TagMatch
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class TagMatch:
    tag: Annotated[str, IdSpec(registry='block', tags='implicit')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::TagMatch": {
        "kind": "struct",
        "fields": [
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
                }
            }
        ]
    }
}

