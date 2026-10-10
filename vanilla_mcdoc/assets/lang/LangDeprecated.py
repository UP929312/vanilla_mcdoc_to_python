"""
Generated from symbols.json for ::java::assets::lang::LangDeprecated
Local link to file: vanilla_mcdoc/assets/lang/LangDeprecated.py
"""
# ~~~ CODE ~~~
from typing import ClassVar

from vanilla_mcdoc.base import GeneratedModel


class LangDeprecated(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'lang/deprecated'

    removed: list[str]  # List of removed translation keys.
    renamed: dict[str, str]  # Mapping renamed translation keys from old to new keys.
