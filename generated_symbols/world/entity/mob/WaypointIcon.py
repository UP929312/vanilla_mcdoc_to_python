# Generated from symbols.json for ::java::world::entity::mob::WaypointIcon
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class WaypointIcon:
    style: str
    color: RGB | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::WaypointIcon": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "style",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "waypoint_style"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
                },
                "optional": True
            }
        ]
    }
}

