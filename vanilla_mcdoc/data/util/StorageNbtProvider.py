"""
Generated from symbols.json for ::java::data::util::StorageNbtProvider
Local link to file: vanilla_mcdoc/data/util/StorageNbtProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class StorageNbtProvider(GeneratedModel):
    source: Annotated[str, IdSpec(registry='storage')]
