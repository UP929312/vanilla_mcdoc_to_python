"""
Generated from symbols.json for ::java::data::decorated_pot_pattern::DecoratedPotPattern
Local link to file: vanilla_mcdoc/data/decorated_pot_pattern/DecoratedPotPattern.py
"""
# ~~~ CODE ~~~
from typing import Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec


class DecoratedPotPattern(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'decorated_pot_pattern'

    asset_id: Annotated[str, IdSpec(registry='texture', path='entity/decorated_pot/')]
