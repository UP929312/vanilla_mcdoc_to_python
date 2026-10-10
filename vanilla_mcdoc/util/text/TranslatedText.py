"""
Generated from symbols.json for ::java::util::text::TranslatedText
Local link to file: vanilla_mcdoc/util/text/TranslatedText.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.TranslationArg import TranslationArg


class TranslatedText(TextBase):
    translate: str
    fallback: str | None = None
    with_: Annotated[list[TranslationArg], Field(min_length=1)] | None = Field(default=None, alias='with')
    type: Literal['translatable'] | None = 'translatable'
