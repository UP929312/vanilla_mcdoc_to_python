# Generated from symbols.json for ::java::world::component::block::SignLines
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


type SignLines = tuple[Text, Text, Text, Text]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::block::SignLines": {
        "kind": "union",
        "members": [
            {
                "kind": "list",
                "item": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "text_component"
                        }
                    ]
                },
                "lengthRange": {
                    "kind": 0,
                    "min": 4,
                    "max": 4
                },
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
                "kind": "list",
                "item": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

