"""
Generated from symbols.json for ::java::world::item::Display
Local link to file: vanilla_mcdoc/world/item/Display.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Display(GeneratedModel):
    Name: str | None = None  # A JSON text component.
    Lore: list[str] | None = None  # A list of JSON text components, each element being a lore line.
