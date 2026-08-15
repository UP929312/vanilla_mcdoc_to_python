"""
Generated from symbols.json for ::java::world::component::predicate::JukeboxPlayablePredicate
Local link to file: generated_symbols/world/component/predicate/JukeboxPlayablePredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class JukeboxPlayablePredicate:
    song: Annotated[str, IdSpec(registry='jukebox_song', tags='allowed')] | list[Annotated[str, IdSpec(registry='jukebox_song')]] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::predicate::JukeboxPlayablePredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "song",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "tree",
                                        "values": {
                                            "registry": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "jukebox_song"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "list",
                            "item": {
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
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

