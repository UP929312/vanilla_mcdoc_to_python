"""
Generated from symbols.json for ::java::assets::item_definition::UseCycle
Local link to file: vanilla_mcdoc/assets/item_definition/UseCycle.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class UseCycle(GeneratedModel):
    period: float | None = None  # returns remaining item use ticks modulo `period`. Defaults to 1.
