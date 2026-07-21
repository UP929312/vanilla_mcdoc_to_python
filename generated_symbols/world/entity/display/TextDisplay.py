# Generated from symbols.json for ::java::world::entity::display::TextDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.display.DisplayBase import DisplayBase

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.entity.display.TextAlignment import TextAlignment


@dataclass(kw_only=True)
class TextDisplay(DisplayBase):
    text: Text | None = None  # Text to display. Components are resolved with the executor set to the display entity and the position set to `0 0 0`.
    line_width: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Line width in pixels used to split lines (note: new line can also be added with `\n` characters). Defaults to 200.
    text_opacity: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None  # Opacity (alpha component) of rendered text. Defaults to 255. Interpolated.
    background: int | None = None  # Color of background. Includes alpha channel. Defaults to 0x40000000. Interpolated.  Calculated as `ALPHA << 24 | RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    default_background: bool | None = None  # If true, overrides `background` & rendering uses default text background color (same as in chat). Defaults to false.
    shadow: bool | None = None  # Whether to display the text with shadows. Defaults to false.
    see_through: bool | None = None  # Whether the text should be visible through opaque blocks. Defaults to false.
    alignment: TextAlignment | None = None  # How text should be aligned. Defaults to `center`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::display::TextDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::display::DisplayBase"
                }
            },
            {
                "kind": "pair",
                "desc": "Text to display. Components are resolved with the executor set to the display entity and the position set to `0 0 0`.",
                "key": "text",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                },
                                {
                                    "name": "text_component"
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::text::Text",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.5"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Line width in pixels used to split lines (note: new line can also be added with `\\n` characters). Defaults to 200.",
                "key": "line_width",
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
                "desc": "Opacity (alpha component) of rendered text. Defaults to 255. Interpolated.",
                "key": "text_opacity",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 255
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Color of background. Includes alpha channel. Defaults to 0x40000000. Interpolated.\n\nCalculated as `ALPHA << 24 | RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.",
                "key": "background",
                "type": {
                    "kind": "int",
                    "attributes": [
                        {
                            "name": "color",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "composite_argb"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If True, overrides `background` & rendering uses default text background color (same as in chat). Defaults to False.",
                "key": "default_background",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": " Whether to display the text with shadows. Defaults to False.",
                "key": "shadow",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the text should be visible through opaque blocks. Defaults to False.",
                "key": "see_through",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "How text should be aligned. Defaults to `center`.\n\nWill log an error when not specified, see [MC-261036](https://bugs.mojang.com/browse/MC-261036).",
                            "key": "alignment",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::entity::display::TextAlignment"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "desc": "How text should be aligned. Defaults to `center`.",
                            "key": "alignment",
                            "type": {
                                "kind": "reference",
                                "path": "::java::world::entity::display::TextAlignment"
                            },
                            "optional": True
                        }
                    ]
                }
            }
        ]
    }
}

