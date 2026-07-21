# Generated from symbols.json for ::java::world::block::Nameable
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class Nameable:
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

