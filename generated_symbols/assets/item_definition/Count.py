# Generated from symbols.json for ::java::assets::item_definition::Count
from dataclasses import dataclass


@dataclass(kw_only=True)
class Count:
    normalize: bool | None = None  # If false, returns count clamped to `0..max_stack_size`. If true, returns count divided by the `max_stack_size` component, clamped to `0..1`. Defaults to true.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Count": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If False, returns count clamped to `0..max_stack_size`.\nIf True, returns count divided by the `max_stack_size` component, clamped to `0..1`.\nDefaults to True.",
                "key": "normalize",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

