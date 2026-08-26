"""
Generated from symbols.json for ::java::data::advancement::RootAdvancementDisplay
Local link to file: generated_symbols/data/advancement/RootAdvancementDisplay.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from generated_symbols.data.advancement.AdvancementDisplay import AdvancementDisplay
from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class RootAdvancementDisplay(AdvancementDisplay):
    background: Annotated[str, IdSpec(registry='texture')]  # Used for the advancement tab.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::RootAdvancementDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::AdvancementDisplay"
                }
            },
            {
                "kind": "pair",
                "desc": "Used for the advancement tab.",
                "key": "background",
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
                                            "value": "1.21.5"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "texture"
                                        }
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

