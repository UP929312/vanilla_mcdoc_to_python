# Generated from symbols.json for ::java::world::component::item::JukeboxPlayable
from dataclasses import dataclass


@dataclass(kw_only=True)
class JukeboxPlayable:
    song: str
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

