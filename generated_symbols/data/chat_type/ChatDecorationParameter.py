# Generated from symbols.json for ::java::data::chat_type::ChatDecorationParameter
from enum import Enum


class ChatDecorationParameter(Enum):
    SENDER = "sender"
    CONTENT = "content"
    TEAMNAME = "team_name"
    TARGET = "target"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::chat_type::ChatDecorationParameter": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Sender",
                "value": "sender"
            },
            {
                "identifier": "Content",
                "value": "content"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.1"
                            }
                        }
                    }
                ],
                "identifier": "TeamName",
                "value": "team_name"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.1"
                            }
                        }
                    }
                ],
                "identifier": "Target",
                "value": "target"
            }
        ]
    }
}

