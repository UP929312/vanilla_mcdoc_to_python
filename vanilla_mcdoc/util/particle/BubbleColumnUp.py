"""
Generated from symbols.json for ::java::util::particle::BubbleColumnUp
Local link to file: vanilla_mcdoc/util/particle/BubbleColumnUp.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class BubbleColumnUp(GeneratedModel):
    pop_chance: Annotated[float, Field(ge=0, le=1)] | None = None  # The chance that the particle will spawn a pop particle and play a pop sound once at the end of its lifecycle.  Defaults to 0.
