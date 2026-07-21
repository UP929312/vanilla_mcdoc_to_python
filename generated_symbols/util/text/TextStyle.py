# Generated from symbols.json for ::java::util::text::TextStyle
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGBA import RGBA
    from generated_symbols.util.text.ClickEvent import ClickEvent
    from generated_symbols.util.text.HoverEvent import HoverEvent
    from generated_symbols.util.text.TextColor import TextColor


@dataclass(kw_only=True)
class TextStyle:
    color: str | TextColor | None = None
    shadow_color: RGBA | None = None  # Overrides the shadow properties of the text. If specified as 0, the shadow will never be displayed.
    font: str | None = None
    bold: bool | None = None
    italic: bool | None = None
    underlined: bool | None = None
    strikethrough: bool | None = None
    obfuscated: bool | None = None
    insertion: str | None = None
    click_event: ClickEvent | None = None
    hover_event: HoverEvent | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::TextStyle": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "hex_rgb"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::util::text::TextColor",
                            "attributes": [
                                {
                                    "name": "color",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "named"
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
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "desc": "Overrides the shadow properties of the text.\nIf specified as 0, the shadow will never be displayed.",
                "key": "shadow_color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGBA"
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
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "key": "font",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "font"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "bold",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "italic",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "underlined",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "strikethrough",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "obfuscated",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "insertion",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
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
                "key": "clickEvent",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::ClickEvent"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "click_event",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::ClickEvent"
                },
                "optional": True
            },
            {
                "kind": "pair",
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
                "key": "hoverEvent",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::HoverEvent"
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
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "hover_event",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::HoverEvent"
                },
                "optional": True
            }
        ]
    }
}

