"""
Generated from symbols.json for ::java::world::component::predicate::ItemCountPseudoPredicate
Local link to file: generated_symbols/world/component/predicate/ItemCountPseudoPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


ItemCountPseudoPredicate = MinMaxBounds[Annotated[int, 'Range | `1`-`99` | both inclusive']] | Annotated[int, 'Range | `1`-`99` | both inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::ItemCountPseudoPredicate": {
        "kind": "concrete",
        "child": {
            "kind": "reference",
            "path": "::java::data::util::MinMaxBounds"
        },
        "typeArgs": [
            {
                "kind": "int",
                "valueRange": {
                    "kind": 0,
                    "min": 1,
                    "max": 99
                }
            }
        ]
    }
}

