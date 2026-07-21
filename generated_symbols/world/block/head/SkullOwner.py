# Generated from symbols.json for ::java::world::block::head::SkullOwner
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.block.head.Properties import Properties


@dataclass(kw_only=True)
class SkullOwner:
    Id: tuple[int, int, int, int] | None = None  # Optional.
    Name: str | None = None  # If missing appears as a steve head.
    Properties: Properties | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::head::SkullOwner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Optional.",
                "key": "Id",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
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
            },
            {
                "kind": "pair",
                "desc": "If missing appears as a steve head.",
                "key": "Name",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "Properties",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::head::Properties"
                },
                "optional": True
            }
        ]
    }
}

