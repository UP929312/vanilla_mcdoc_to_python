# Generated from symbols.json for ::java::world::block::command_block::BaseCommandBlock
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class BaseCommandBlock:
    Command: str | None = None  # The command to run.
    SuccessCount: int | None = None  # Success count of the last command.
    LastOutput: Text | None = None  # Output of the last command.
    TrackOutput: bool | None = None  # Whether to record command output.
    UpdateLastExecution: bool | None = None  # Whether to record the tick of the latest command execution.
    LastExecution: int | None = None  # Tick of the latest command execution.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::command_block::BaseCommandBlock": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The command to run.",
                "key": "Command",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "command",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "slash": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "allowed"
                                        }
                                    },
                                    "empty": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "allowed"
                                        }
                                    },
                                    "max_length": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "int",
                                            "value": 32500
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Success count of the last command.",
                "key": "SuccessCount",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Output of the last command.",
                "key": "LastOutput",
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
            },
            {
                "kind": "pair",
                "desc": "Whether to record command output.",
                "key": "TrackOutput",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether to record the tick of the latest command execution.",
                "key": "UpdateLastExecution",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Tick of the latest command execution.",
                "key": "LastExecution",
                "type": {
                    "kind": "long"
                },
                "optional": True
            }
        ]
    }
}

