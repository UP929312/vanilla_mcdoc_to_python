# Generated from symbols.json for ::java::data::advancement::predicate::LocationPredicateLight
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class LocationPredicateLight:
    light: MinMaxBounds[Annotated[int, 'Range | `0`-`15` | both inclusive']] | Annotated[int, 'Range | `0`-`15` | both inclusive'] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::LocationPredicateLight": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "light",
                "type": {
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
                                "min": 0,
                                "max": 15
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

