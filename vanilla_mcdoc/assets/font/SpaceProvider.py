"""
Generated from symbols.json for ::java::assets::font::SpaceProvider
Local link to file: vanilla_mcdoc/assets/font/SpaceProvider.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class SpaceProvider(GeneratedModel):
    advances: dict[Annotated[str, Field(min_length=1, max_length=1)], float]
