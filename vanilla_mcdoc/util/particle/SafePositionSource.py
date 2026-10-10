"""
Generated from symbols.json for ::java::util::particle::SafePositionSource
Local link to file: generated_symbols/util/particle/SafePositionSource.py
"""
# ~~~ CODE ~~~
from typing import Literal

from generated_symbols.base import GeneratedModel


class SafePositionSource(GeneratedModel):
    type: Literal['block'] = 'block'
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
