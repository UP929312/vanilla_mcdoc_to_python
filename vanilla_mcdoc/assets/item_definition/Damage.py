"""
Generated from symbols.json for ::java::assets::item_definition::Damage
Local link to file: vanilla_mcdoc/assets/item_definition/Damage.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Damage(GeneratedModel):
    normalize: bool | None = None  # If false, returns value of damage, clamped to `0..max_damage`. If true, returns value of damage divided by the `max_damage` component, clamped to `0..1`. Defaults to true.
