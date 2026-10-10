"""
Generated from symbols.json for ::java::util::text::ChangePage
Local link to file: vanilla_mcdoc/util/text/ChangePage.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ChangePage(GeneratedModel):
    page: Annotated[int, Field(ge=1)]  # The page number to go to.
