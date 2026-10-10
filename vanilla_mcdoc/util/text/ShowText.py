"""
Generated from symbols.json for ::java::util::text::ShowText
Local link to file: vanilla_mcdoc/util/text/ShowText.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class ShowText(GeneratedModel):
    value: Text
