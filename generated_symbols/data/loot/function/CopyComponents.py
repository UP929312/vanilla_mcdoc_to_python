"""
Generated from symbols.json for ::java::data::loot::function::CopyComponents
Local link to file: generated_symbols/data/loot/function/CopyComponents.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from generated_symbols.data.loot.function.Conditions import Conditions
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.loot.BlockEntityTarget import BlockEntityTarget
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.data.loot.ItemStackTarget import ItemStackTarget


@dataclass(kw_only=True)
class CopyComponents(Conditions):
    source: BlockEntityTarget | EntityTarget | ItemStackTarget
    include: list[Annotated[str, IdSpec(registry='data_component_type')]] | None = None  # If omitted, all components present are included
    exclude: list[Annotated[str, IdSpec(registry='data_component_type')]] | None = None  # Defaults to none.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::CopyComponents": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "source",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::BlockEntityTarget"
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::EntityTarget",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.9"
                                        }
                                    }
                                }
                            ]
                        },
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::ItemStackTarget",
                            "attributes": [
                                {
                                    "name": "since",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.21.9"
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
                "desc": "If omitted, all components present are included",
                "key": "include",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "data_component_type"
                                    }
                                }
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to none.",
                "key": "exclude",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "data_component_type"
                                    }
                                }
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::function::Conditions"
                }
            }
        ]
    }
}

