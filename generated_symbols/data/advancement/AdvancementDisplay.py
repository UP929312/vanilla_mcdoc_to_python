# Generated from symbols.json for ::java::data::advancement::AdvancementDisplay
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.advancement.AdvancementFrame import AdvancementFrame
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.item.ItemStackTemplate import ItemStackTemplate


@dataclass(kw_only=True)
class AdvancementDisplay:
    icon: ItemStackTemplate
    title: Text
    description: Text
    background: str | None = None  # Used for the advancement tab (root advancement only).
    frame: AdvancementFrame | None = None  # Controls the advancement tile frame. Defaults to `task`.
    show_toast: bool | None = None  # Whether to show the toast pop up after completing this advancement. Defaults to `true`.
    announce_to_chat: bool | None = None  # Whether to announce in the chat when this advancement has been completed. Defaults to `true`.
    hidden: bool | None = None  # Whether or not to hide this advancement and all its children from the advancement screen, until this advancement have been completed. Has no effect on root advancements themselves, but still affects all their children. Defaults to `false`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::AdvancementDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "icon",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::advancement::AdvancementIcon",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::world::item::ItemStackTemplate",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.20.5"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "title",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "key": "description",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                }
            },
            {
                "kind": "pair",
                "desc": "Used for the advancement tab (root advancement only).",
                "key": "background",
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
                                }
                            ]
                        },
                        {
                            "kind": "string",
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
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "texture"
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
                "desc": "Controls the advancement tile frame. Defaults to `task`.",
                "key": "frame",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::advancement::AdvancementFrame"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether to show the toast pop up after completing this advancement. Defaults to `True`.",
                "key": "show_toast",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether to announce in the chat when this advancement has been completed. Defaults to `True`.",
                "key": "announce_to_chat",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether or not to hide this advancement and all its children from the advancement screen,\nuntil this advancement have been completed.\nHas no effect on root advancements themselves, but still affects all their children.\nDefaults to `False`.",
                "key": "hidden",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

