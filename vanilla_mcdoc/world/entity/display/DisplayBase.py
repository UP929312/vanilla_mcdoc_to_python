"""
Generated from symbols.json for ::java::world::entity::display::DisplayBase
Local link to file: vanilla_mcdoc/world/entity/display/DisplayBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.display.Billboard import Billboard
    from vanilla_mcdoc.world.entity.display.Brightness import Brightness
    from vanilla_mcdoc.world.entity.display.Transformation import Transformation


class DisplayBase(EntityBase):
    transformation: Transformation | None = None  # Transformation applied to model (after normal entity orientation). Defaults to identity. Interpolated.  For an easy GUI, check out [Misode's tool](https://misode.github.io/transformation/).  The value is stored in decomposed object form for interpolation & ease-of-use,  Supports storing a [non-canonical matrix form](https://gist.github.com/MulverineX/f473dbfd7cc8dadb326074fef05ad76a) describing a row-major matrix, which is automatically decomposed by the game with a performance cost.
    shadow_radius: Annotated[float, Field(ge=0)] | None = None  # Size of shadow. Defaults to 0 (no shadow). Interpolated.
    shadow_strength: Annotated[float, Field(ge=0, le=1)] | None = None  # Strength of the shadow. Controls the opacity of the shadow as a function of distance to the block below. Defaults to 1. Interpolated.
    start_interpolation: int | None = None  # Ticks after the next client tick to wait until starting the interpolation.  Info:  All interpolated properties are part of a single interpolation set.  Any update to an interpolated property will cause all values of the interpolation set to be saved as "current".  - Data command executions that do not change the value of a property (even if it's present in NBT) do not count as updates.  - Updates are synchronized to clients at most once per tick, so multiple updates within a single command or a function will still count as a single update.  Previous current values are saved as "previous".  If interpolation is enabled, the entity will transition between "previous" and "current" values over time.  `interpolation_duration` must be set every time an interpolatable property is updated to cause interpolation.  Negative values are allowed, will cause an instant jump to the subtracted duration value, then interpolation will continue as normal.
    interpolation_duration: Annotated[int, Field(ge=0)] | None = None  # Ticks the interpolation should take to complete.
    teleport_duration: Annotated[int, Field(ge=0, le=59)] | None = None  # How long in game ticks the entity takes to interpolate from its starting location to its destination when teleported. Defaults to 0 (no interpolation).
    billboard: Billboard | None = None  # Controls if the model should pivot to face the player when rendered. Defaults to `fixed`.
    brightness: Brightness | None = None  # When defined, overrides light values used for rendering. Omitted by default (which means rendering uses values from the entity position).
    view_range: Annotated[float, Field(ge=0)] | None = None  # Maximum view range of this entity. Actual distance depends on client-side render distance and entity distance scaling. Default value 1.0 (roughly the same as fireball).
    width: Annotated[float, Field(ge=0)] | None = None  # Describe width of the culling bounding box.  Bounding box spans vertically from y to y+height and horizontally width/2 in all directions from the entity position.  If set to 0, culling is disabled. Defaults to 0.
    height: Annotated[float, Field(ge=0)] | None = None  # Describes height of the culling bounding box.  Bounding box spans vertically from y to y+height and horizontally width/2 in all directions from the entity position.  If set to 0, culling is disabled. Defaults to 0.
    glow_color_override: Literal[0] | int | None = None  # Override glow border color. If set to 0, uses team color. Defaults to 0.  Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
