"""
Generated from symbols.json for ::java::data::advancement::predicate::VillagerPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/VillagerPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class VillagerPredicate(GeneratedModel):
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
