# Generated from symbols.json for ::java::data::worldgen::feature::block_predicate::PredicateOffset
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class PredicateOffset:
    offset: tuple[Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive'], Annotated[int, 'Range | `-16`-`16` | both inclusive']] | None = None  # The block offset to check.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::block_predicate::PredicateOffset": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The block offset to check.",
                "key": "offset",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int",
                        "valueRange": {
                            "kind": 0,
                            "min": -16,
                            "max": 16
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

