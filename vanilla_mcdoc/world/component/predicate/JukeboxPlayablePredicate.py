"""
Generated from symbols.json for ::java::world::component::predicate::JukeboxPlayablePredicate
Local link to file: vanilla_mcdoc/world/component/predicate/JukeboxPlayablePredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class JukeboxPlayablePredicate(GeneratedModel):
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
