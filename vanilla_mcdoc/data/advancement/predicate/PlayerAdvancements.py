"""
Generated from symbols.json for ::java::data::advancement::predicate::PlayerAdvancements
Local link to file: vanilla_mcdoc/data/advancement/predicate/PlayerAdvancements.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type PlayerAdvancements = dict[Annotated[str, IdSpec(registry='advancement')], bool | dict[str, bool]]
