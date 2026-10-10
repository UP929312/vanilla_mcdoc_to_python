"""
Generated from symbols.json for ::java::util::text::StorageNbtText
Local link to file: vanilla_mcdoc/util/text/StorageNbtText.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.util.text.TextNbtBase import TextNbtBase


class StorageNbtText(TextNbtBase):
    storage: Annotated[str, IdSpec(registry='storage')]
    nbt: str
    source: Literal['storage'] | None = 'storage'
    type: Literal['nbt'] | None = 'nbt'
