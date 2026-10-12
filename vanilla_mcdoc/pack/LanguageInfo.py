"""
Generated from symbols.json for ::java::pack::LanguageInfo
Local link to file: vanilla_mcdoc/pack/LanguageInfo.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class LanguageInfo(GeneratedModel):
    name: Annotated[str, Field(min_length=1)]  # Language name displayed in the language menu.
    region: Annotated[str, Field(min_length=1)]  # Region name displayed in the language menu.
    bidirectional: bool | None = None  # Whether the language reads right to left. Defaults to `false`.
