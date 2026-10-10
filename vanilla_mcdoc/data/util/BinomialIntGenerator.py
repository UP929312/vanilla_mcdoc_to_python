"""
Generated from symbols.json for ::java::data::util::BinomialIntGenerator
Local link to file: vanilla_mcdoc/data/util/BinomialIntGenerator.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class BinomialIntGenerator(GeneratedModel):
    n: Annotated[int, Field(ge=0)]
    p: Annotated[float, Field(ge=0, le=1)]
