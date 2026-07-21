# Generated from symbols.json for ::java::data::dialog::action::DynamicRunCommand
from dataclasses import dataclass


@dataclass(kw_only=True)
class DynamicRunCommand:
    template: str  # A macro template to be interpred as a command. Special characters (including both `'` and `"`) from text input will be escaped to fit in SNBT literal.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::dialog::action::DynamicRunCommand": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "A macro template to be interpred as a command.\nSpecial characters (including both `'` and `\"`) from text input will be escaped to fit in SNBT literal.",
                "key": "template",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "command",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "macro": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "implicit"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

