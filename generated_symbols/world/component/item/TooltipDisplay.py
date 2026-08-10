"""
Generated from symbols.json for ::java::world::component::item::TooltipDisplay
Local link to file: generated_symbols/world/component/item/TooltipDisplay.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class TooltipDisplay:
    hide_tooltip: bool | None = None  # If `true`, the item will have no tooltip when hovered. Defaults to `false`.
    hidden_components: list[Annotated[str, IdSpec(registry='data_component_type')]] | None = None  # List of components that should be hidden in the item tooltip.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::TooltipDisplay": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If `True`, the item will have no tooltip when hovered. Defaults to `False`.",
                "key": "hide_tooltip",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "List of components that should be hidden in the item tooltip.",
                "key": "hidden_components",
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
            }
        ]
    }
}

