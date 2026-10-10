"""
Generated from symbols.json for ::java::util::text::CustomAction
Local link to file: vanilla_mcdoc/util/text/CustomAction.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Any

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class CustomAction(GeneratedModel):
    id: Annotated[str, IdSpec()]  # ID of a custom action. Has no functionality on vanilla servers.
    payload: Any | None = None
