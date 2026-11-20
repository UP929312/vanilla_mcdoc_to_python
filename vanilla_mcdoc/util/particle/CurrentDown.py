"""
Generated from symbols.json for ::java::util::particle::CurrentDown
Local link to file: vanilla_mcdoc/util/particle/CurrentDown.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class CurrentDown(GeneratedModel):
    radius: Annotated[float, Field(ge=0)]
