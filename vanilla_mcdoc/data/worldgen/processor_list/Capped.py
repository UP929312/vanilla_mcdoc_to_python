"""
Generated from symbols.json for ::java::data::worldgen::processor_list::Capped
Local link to file: vanilla_mcdoc/data/worldgen/processor_list/Capped.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.IntProvider import IntProvider
    from vanilla_mcdoc.data.worldgen.processor_list.Processor import Processor


class Capped(GeneratedModel):
    delegate: Processor
    limit: IntProvider[Annotated[int, Field(ge=0)]] | Annotated[int, Field(ge=0)]
