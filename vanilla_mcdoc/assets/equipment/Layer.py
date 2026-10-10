"""
Generated from symbols.json for ::java::assets::equipment::Layer
Local link to file: vanilla_mcdoc/assets/equipment/Layer.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Generic, TypeVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.equipment.Dyeable import Dyeable


T = TypeVar('T')


class Layer(GeneratedModel, Generic[T]):
    texture: T  # Texture location for this layer, inside `entity/equipment/<layer>/`.
    dyeable: Dyeable | None = None  # If specified, this layer will be tinted by the color contained in the `dyed_color` component.
