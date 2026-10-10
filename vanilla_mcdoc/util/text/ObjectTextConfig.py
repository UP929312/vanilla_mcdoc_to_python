"""
Generated from symbols.json for ::java::util::text::ObjectTextConfig
Local link to file: vanilla_mcdoc/util/text/ObjectTextConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class ObjectTextConfig(GeneratedModel):
    fallback: Text | None = None  # Used in places where object component cannot be displayed (for example, server log or narration).
