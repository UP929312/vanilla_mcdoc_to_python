"""
Generated from symbols.json for ::java::world::entity::boat::Boat
Local link to file: vanilla_mcdoc/world/entity/boat/Boat.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.entity.EntityBase import EntityBase


class Boat(EntityBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::boat::Boat": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "desc": "Wood type of this boat",
                "key": "Type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::boat::BoatType"
                },
                "optional": True
            }
        ]
    }
}
