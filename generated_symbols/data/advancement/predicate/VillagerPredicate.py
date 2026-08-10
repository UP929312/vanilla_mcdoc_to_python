"""
Generated from symbols.json for ::java::data::advancement::predicate::VillagerPredicate
Local link to file: generated_symbols/data/advancement/predicate/VillagerPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class VillagerPredicate:
    variant: Annotated[str, IdSpec(registry='villager_type')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::VillagerPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "variant",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "villager_type"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

