"""
Generated from symbols.json for ::java::data::advancement::predicate::EntityTypePredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/EntityTypePredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type EntityTypePredicate = Annotated[str, IdSpec(registry='entity_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='entity_type')]]
