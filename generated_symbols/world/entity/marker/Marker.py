# Generated from symbols.json for ::java::world::entity::marker::Marker
from dataclasses import dataclass
from generated_symbols.world.entity.EntityBase import EntityBase


@dataclass(kw_only=True)
class Marker(EntityBase):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::marker::Marker": {
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "desc": "Any stored data",
                "key": "data",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string",
                                "attributes": [
                                    {
                                        "name": "dispatcher_key",
                                        "value": {
                                            "kind": "literal",
                                            "value": {
                                                "kind": "string",
                                                "value": "mcdoc:marker_data"
                                            }
                                        }
                                    }
                                ]
                            },
                            "type": {
                                "kind": "dispatcher",
                                "parallelIndices": [
                                    {
                                        "kind": "dynamic",
                                        "accessor": [
                                            {
                                                "keyword": "key"
                                            }
                                        ]
                                    }
                                ],
                                "registry": "mcdoc:marker_data"
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

