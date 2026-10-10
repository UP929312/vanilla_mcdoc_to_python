"""
Generated from symbols.json for ::java::assets::regional_compliancies::Notification
Local link to file: vanilla_mcdoc/assets/regional_compliancies/Notification.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Notification(GeneratedModel):
    delay: int | None = None
    period: int
    title: str
    message: str


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
