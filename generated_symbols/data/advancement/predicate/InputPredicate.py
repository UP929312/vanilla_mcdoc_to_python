# Generated from symbols.json for ::java::data::advancement::predicate::InputPredicate
from dataclasses import dataclass


@dataclass(kw_only=True)
class InputPredicate:
    forward: bool | None = None
    backward: bool | None = None
    left: bool | None = None
    right: bool | None = None
    jump: bool | None = None
    sneak: bool | None = None
    sprint: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::InputPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "forward",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "backward",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "left",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "right",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "jump",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "sneak",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "sprint",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

