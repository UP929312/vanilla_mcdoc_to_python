"""
Generated from symbols.json for ::java::util::particle::SafePositionSource
Local link to file: vanilla_mcdoc/util/particle/SafePositionSource.py
"""
# ~~~ CODE ~~~
from typing import Literal

from vanilla_mcdoc.base import GeneratedModel


class SafePositionSource(GeneratedModel):
    type: Literal['block'] = 'block'
    pos: tuple[int, int, int]
