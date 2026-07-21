# Generated from symbols.json for ::java::assets::item_definition::Damage
from dataclasses import dataclass


@dataclass(kw_only=True)
class Damage:
    normalize: bool | None = None  # If false, returns value of damage, clamped to `0..max_damage`. If true, returns value of damage divided by the `max_damage` component, clamped to `0..1`. Defaults to true.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Damage": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If False, returns value of damage, clamped to `0..max_damage`.\nIf True, returns value of damage divided by the `max_damage` component, clamped to `0..1`.\nDefaults to True.",
                "key": "normalize",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

