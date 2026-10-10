"""
Generated from symbols.json for ::java::assets::item_definition::Count
Local link to file: vanilla_mcdoc/assets/item_definition/Count.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Count(GeneratedModel):
    normalize: bool | None = None  # If false, returns count clamped to `0..max_stack_size`. If true, returns count divided by the `max_stack_size` component, clamped to `0..1`. Defaults to true.
