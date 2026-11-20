"""
Generated from symbols.json for ::java::data::dispense_behavior::ShootProjectile
Local link to file: vanilla_mcdoc/data/dispense_behavior/ShootProjectile.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.SoundEventRef import SoundEventRef
    from vanilla_mcdoc.data.worldgen.FloatProvider import FloatProvider


class SoundStruct(GeneratedModel):
    sound: SoundEventRef
    volume: FloatProvider[float] | float
    pitch: FloatProvider[float] | float


class ShootProjectile(GeneratedModel):
    scale: float  # How far the spawn position of the projectile is from the center of the dispenser.  1.0 means the block center in front of the dispenser (i.e. 1 block away from the center of the dispenser).
    offset: tuple[float, float, float]  # **Absolute** offset added to the spawn position of the projectile.  Unaffected by the dispenser's rotation.
    uncertainty: Annotated[float, Field(ge=0)]  # The inaccuracy of the shot.  Vanilla behavior is `6.0`.  Each axis of the movement direction is added by a random number between `0.0` and `0.0172275 * uncertainty`.
    power: Annotated[float, Field(ge=0)]  # The velocity of the shot.  Vanilla behavior is `1.1`.  Scales the movement direction after the inaccuracy is added.
    sound: SoundStruct | None = None
