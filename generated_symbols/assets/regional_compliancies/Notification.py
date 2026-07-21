# Generated from symbols.json for ::java::assets::regional_compliancies::Notification
from dataclasses import dataclass


@dataclass(kw_only=True)
class Notification:
    period: int
    title: str
    message: str
    delay: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::regional_compliancies::Notification": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "delay",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "period",
                "type": {
                    "kind": "long"
                }
            },
            {
                "kind": "pair",
                "key": "title",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "key": "message",
                "type": {
                    "kind": "string"
                }
            }
        ]
    }
}

