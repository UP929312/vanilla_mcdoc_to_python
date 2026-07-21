# Generated from symbols.json for ::java::world::entity::end_crystal::EndCrystal
from dataclasses import dataclass
from generated_symbols.world.entity.EntityBase import EntityBase


@dataclass(kw_only=True)
class EndCrystal(EntityBase):
    ShowBottom: bool | None = None  # Whether to show the base of the end crystal.
    beam_target: tuple[int, int, int] | None = None  # Coordinates that the beam is pointing to


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::end_crystal::EndCrystal": {
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
                "desc": "Whether to show the base of the end crystal.",
                "key": "ShowBottom",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Coordinates that the beam is pointing to",
                "key": "BeamTarget",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::end_crystal::BeamTarget"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "desc": "Coordinates that the beam is pointing to",
                "key": "beam_target",
                "type": {
                    "kind": "int_array",
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

