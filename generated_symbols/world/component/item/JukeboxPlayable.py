"""
Generated from symbols.json for ::java::world::component::item::JukeboxPlayable
Local link to file: generated_symbols/world/component/item/JukeboxPlayable.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class JukeboxPlayable:
    song: Annotated[str, IdSpec(registry='jukebox_song')]
    show_in_tooltip: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::JukeboxPlayable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "song",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "jukebox_song"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "show_in_tooltip",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ],
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
        ]
    }
}

