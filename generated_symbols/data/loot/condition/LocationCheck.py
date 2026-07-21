# Generated from symbols.json for ::java::data::loot::condition::LocationCheck
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate


@dataclass(kw_only=True)
class LocationCheck:
    predicate: LocationPredicate
    offsetX: int | None = None
    offsetY: int | None = None
    offsetZ: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::condition::LocationCheck": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "offsetX",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "offsetY",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "offsetZ",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "predicate",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::predicate::LocationPredicate"
                }
            }
        ]
    }
}

