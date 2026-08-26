"""
Generated from symbols.json for ::java::world::component::item::SwingAnimation
Local link to file: generated_symbols/world/component/item/SwingAnimation.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.world.component.item.SwingAnimationType import SwingAnimationType


@dataclass(kw_only=True)
class SwingAnimation:
    type: SwingAnimationType | None = None  # The animation type to play when attacking or interacting using this item. Defaults to `whack`.
    duration: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The animation duration in ticks. Defaults to 6


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::SwingAnimation": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The animation type to play when attacking or interacting using this item.\nDefaults to `whack`.",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::SwingAnimationType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The animation duration in ticks.\nDefaults to 6",
                "key": "duration",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 1
                            },
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0
                            },
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "26.3"
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

