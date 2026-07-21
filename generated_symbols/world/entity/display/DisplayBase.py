# Generated from symbols.json for ::java::world::entity::display::DisplayBase
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.EntityBase import EntityBase

if TYPE_CHECKING:
    from generated_symbols.world.entity.display.Billboard import Billboard
    from generated_symbols.world.entity.display.Brightness import Brightness
    from generated_symbols.world.entity.display.Transformation import Transformation


@dataclass(kw_only=True)
class DisplayBase(EntityBase):
    transformation: Transformation | None = None  # Transformation applied to model (after normal entity orientation). Defaults to identity. Interpolated.  For an easy GUI, check out [Misode's tool](https://misode.github.io/transformation/).  The value is stored in decomposed object form for interpolation & ease-of-use,  Supports storing a [non-canonical matrix form](https://gist.github.com/MulverineX/f473dbfd7cc8dadb326074fef05ad76a) describing a row-major matrix, which is automatically decomposed by the game with a performance cost.
    shadow_radius: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Size of shadow. Defaults to 0 (no shadow). Interpolated.
    shadow_strength: Annotated[float, 'Range | `0`-`1` | both inclusive'] | None = None  # Strength of the shadow. Controls the opacity of the shadow as a function of distance to the block below. Defaults to 1. Interpolated.
    start_interpolation: int | None = None  # Ticks after the next client tick to wait until starting the interpolation.  Info:  All interpolated properties are part of a single interpolation set.  Any update to an interpolated property will cause all values of the interpolation set to be saved as "current".  - Data command executions that do not change the value of a property (even if it's present in NBT) do not count as updates.  - Updates are synchronized to clients at most once per tick, so multiple updates within a single command or a function will still count as a single update.  Previous current values are saved as "previous".  If interpolation is enabled, the entity will transition between "previous" and "current" values over time.  `interpolation_duration` must be set every time an interpolatable property is updated to cause interpolation.  Negative values are allowed, will cause an instant jump to the subtracted duration value, then interpolation will continue as normal.
    interpolation_duration: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Ticks the interpolation should take to complete.
    teleport_duration: Annotated[int, 'Range | `0`-`59` | both inclusive'] | None = None  # How long in game ticks the entity takes to interpolate from its starting location to its destination when teleported. Defaults to 0 (no interpolation).
    billboard: Billboard | None = None  # Controls if the model should pivot to face the player when rendered. Defaults to `fixed`.
    brightness: Brightness | None = None  # When defined, overrides light values used for rendering. Omitted by default (which means rendering uses values from the entity position).
    view_range: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Maximum view range of this entity. Actual distance depends on client-side render distance and entity distance scaling. Default value 1.0 (roughly the same as fireball).
    width: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Describe width of the culling bounding box.  Bounding box spans vertically from y to y+height and horizontally width/2 in all directions from the entity position.  If set to 0, culling is disabled. Defaults to 0.
    height: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Describes height of the culling bounding box.  Bounding box spans vertically from y to y+height and horizontally width/2 in all directions from the entity position.  If set to 0, culling is disabled. Defaults to 0.
    glow_color_override: int | None = None  # Override glow border color. If set to 0, uses team color. Defaults to 0.  Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::DisplayBase": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::EntityBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Transformation applied to model (after normal entity orientation). Defaults to identity. Interpolated.\n\nFor an easy GUI, check out [Misode's tool](https://misode.github.io/transformation/).\n\nThe value is stored in decomposed object form for interpolation & ease-of-use,\n\nSupports storing a [non-canonical matrix form](https://gist.github.com/MulverineX/f473dbfd7cc8dadb326074fef05ad76a) describing a row-major matrix, which is automatically decomposed by the game with a performance cost.",
                "key": "transformation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::Transformation"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Size of shadow. Defaults to 0 (no shadow). Interpolated.",
                "key": "shadow_radius",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Strength of the shadow. Controls the opacity of the shadow as a function of distance to the block below. Defaults to 1. Interpolated.",
                "key": "shadow_strength",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks after the next client tick to wait until starting the interpolation.\n\nInfo:\n\nAll interpolated properties are part of a single interpolation set.\n\nAny update to an interpolated property will cause all values of the interpolation set to be saved as \"current\".\n - Data command executions that do not change the value of a property (even if it's present in NBT) do not count as updates.\n - Updates are synchronized to clients at most once per tick, so multiple updates within a single command or a function will still count as a single update.\n\nPrevious current values are saved as \"previous\".\n\nIf interpolation is enabled, the entity will transition between \"previous\" and \"current\" values over time.\n\n`interpolation_duration` must be set every time an interpolatable property is updated to cause interpolation.\n\nNegative values are allowed, will cause an instant jump to the subtracted duration value, then interpolation will continue as normal.",
                "key": "start_interpolation",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks the interpolation should take to complete.",
                "key": "interpolation_duration",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "desc": "How long in game ticks the entity takes to interpolate from its starting location to its destination when teleported. Defaults to 0 (no interpolation).",
                "key": "teleport_duration",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 59
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Controls if the model should pivot to face the player when rendered. Defaults to `fixed`.",
                "key": "billboard",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::Billboard"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "When defined, overrides light values used for rendering. Omitted by default (which means rendering uses values from the entity position).",
                "key": "brightness",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::Brightness"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum view range of this entity. Actual distance depends on client-side render distance and entity distance scaling. Default value 1.0 (roughly the same as fireball).",
                "key": "view_range",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Describe width of the culling bounding box.\n\nBounding box spans vertically from y to y+height and horizontally width/2 in all directions from the entity position.\n\nIf set to 0, culling is disabled. Defaults to 0.",
                "key": "width",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Describes height of the culling bounding box.\n\nBounding box spans vertically from y to y+height and horizontally width/2 in all directions from the entity position.\n\nIf set to 0, culling is disabled. Defaults to 0.",
                "key": "height",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Override glow border color. If set to 0, uses team color. Defaults to 0.\n\nCalculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "glow_color_override",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "literal",
                            "value": {
                                "kind": "int",
                                "value": 0
                            }
                        },
                        {
                            "kind": "int",
                            "attributes": [
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "composite_rgb"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

