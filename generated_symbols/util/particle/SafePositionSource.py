# Generated from symbols.json for ::java::util::particle::SafePositionSource
from dataclasses import dataclass


@dataclass(kw_only=True)
class SafePositionSource:
    type: str
    pos: tuple[int, int, int]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::SafePositionSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "literal",
                    "value": {
                        "kind": "string",
                        "value": "block"
                    },
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "position_source_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "pos",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                }
            }
        ]
    }
}

