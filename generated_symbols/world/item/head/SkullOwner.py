# Generated from symbols.json for ::java::world::item::head::SkullOwner
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.item.head.Properties import Properties


@dataclass(kw_only=True)
class SkullOwner:
    Id: tuple[int, int, int, int] | None = None  # Optional.
    Name: str | None = None  # Name of the owner, if missing appears as a steve head.
    Properties: Properties | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::item::head::SkullOwner": {
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
                "desc": "Name of the owner, if missing appears as a steve head.",
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
                    "path": "::java::world::item::head::Properties"
                },
                "optional": True
            }
        ]
    }
}

