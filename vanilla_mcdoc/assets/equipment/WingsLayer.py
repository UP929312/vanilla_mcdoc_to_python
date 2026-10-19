"""
Generated from symbols.json for ::java::assets::equipment::WingsLayer
Local link to file: vanilla_mcdoc/assets/equipment/WingsLayer.py
"""
# ~~~ CODE ~~~
from typing import Any, Generic, TypeVar

from vanilla_mcdoc.assets.equipment.Layer import Layer


T = TypeVar('T', default=Any)


class WingsLayer(Layer[T], Generic[T]):
    use_player_texture: bool | None = None  # Whether this layer texture should be overridden by the player's custom elytra texture.  Defaults to `false`.
