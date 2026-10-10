"""
Generated from symbols.json for ::java::data::advancement::predicate::PlayerAdvancements
Local link to file: generated_symbols/data/advancement/predicate/PlayerAdvancements.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from minecraft_registry import IdSpec


type PlayerAdvancements = dict[Annotated[str, IdSpec(registry='advancement')], bool | dict[str, bool]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::PlayerAdvancements": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "advancement"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "boolean"
                        },
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": {
                                        "kind": "string"
                                    },
                                    "type": {
                                        "kind": "boolean"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
