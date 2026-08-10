"""
Generated from symbols.json for ::java::util::game_event::BlockPositionSource
Local link to file: generated_symbols/util/game_event/BlockPositionSource.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass


@dataclass(kw_only=True)
class BlockPositionSource:
    pos: tuple[int, int, int]  # Block position


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::game_event::BlockPositionSource": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Block position",
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

