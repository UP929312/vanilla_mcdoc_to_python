"""
Generated from symbols.json for ::java::assets::equipment::Equipment
Local link to file: vanilla_mcdoc/assets/equipment/Equipment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.equipment.Layers import Layers
    from vanilla_mcdoc.assets.equipment.TrimOverride import TrimOverride


class Equipment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'equipment'

    layers: Layers  # List of layers for each model layer type.
    trim_overrides: list[TrimOverride] | None = None  # Replaces trim texture based on armor trim.  Only the first entry that matches is applied.
