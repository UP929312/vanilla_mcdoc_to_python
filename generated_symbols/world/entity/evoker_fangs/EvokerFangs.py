# Generated from symbols.json for ::java::world::entity::evoker_fangs::EvokerFangs
from dataclasses import dataclass
from generated_symbols.world.entity.EntityBase import EntityBase


@dataclass(kw_only=True)
class EvokerFangs(EntityBase):
    Warmup: int | None = None  # Ticks until the fangs pop out of the ground.
    Owner: tuple[int, int, int, int] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::evoker_fangs::EvokerFangs": {
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
                "desc": "Ticks until the fangs pop out of the ground.",
                "key": "Warmup",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Owner",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::world::entity::evoker_fangs::Owner",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "uuid"
                                }
                            ]
                        },
                        {
                            "kind": "int_array",
                            "lengthRange": {
                                "kind": 0,
                                "min": 4,
                                "max": 4
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "uuid"
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

