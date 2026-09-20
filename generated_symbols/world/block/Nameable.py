"""
Generated from symbols.json for ::java::world::block::Nameable
Local link to file: generated_symbols/world/block/Nameable.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


class Nameable(GeneratedModel):
    CustomName: Text | None = None  # The custom name of this block.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::Nameable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The custom name of this block.",
                "key": "CustomName",
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
                                },
                                {
                                    "name": "text_component"
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::text::Text",
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
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

