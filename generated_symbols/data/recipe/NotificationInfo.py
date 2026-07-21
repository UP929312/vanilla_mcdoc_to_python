# Generated from symbols.json for ::java::data::recipe::NotificationInfo
from dataclasses import dataclass


@dataclass(kw_only=True)
class NotificationInfo:
    show_notification: bool | None = None  # Determines if a notification is shown when unlocking this recipe. Defaults to `true`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::recipe::NotificationInfo": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Determines if a notification is shown when unlocking this recipe.\nDefaults to `True`.",
                "key": "show_notification",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

