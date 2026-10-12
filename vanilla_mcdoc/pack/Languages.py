"""
Generated from symbols.json for ::java::pack::Languages
Local link to file: vanilla_mcdoc/pack/Languages.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

if TYPE_CHECKING:
    from vanilla_mcdoc.pack.LanguageInfo import LanguageInfo


type Languages = dict[Annotated[str, Field(min_length=1, max_length=16)], LanguageInfo]
