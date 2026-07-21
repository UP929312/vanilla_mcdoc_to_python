# Generated from symbols.json for ::java::data::advancement::predicate::VillagerPredicate
from dataclasses import dataclass


@dataclass(kw_only=True)
class VillagerPredicate:
    variant: str


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

