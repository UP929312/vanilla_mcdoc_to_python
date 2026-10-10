"""
Generated from symbols.json for ::java::data::worldgen::template_pool::ListElement
Local link to file: vanilla_mcdoc/data/worldgen/template_pool/ListElement.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.data.worldgen.template_pool.ElementBase import ElementBase

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.template_pool.Element import Element


class ListElement(ElementBase):
    elements: list[Element]
