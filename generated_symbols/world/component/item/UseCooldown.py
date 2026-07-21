# Generated from symbols.json for ::java::world::component::item::UseCooldown
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class UseCooldown:
    seconds: Annotated[float, 'Range | Min `0` and above | inclusive']  # Time the cooldown will last.
    cooldown_group: str | None = None  # If present, this item will be part of a cooldown group and no longer share cooldowns with its base item type. Instead, cooldowns applied to this item will only be shared with any other items that are part of the same cooldown group.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::UseCooldown": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Time the cooldown will last.",
                "key": "seconds",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 2,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "If present, this item will be part of a cooldown group and no longer share cooldowns with its base item type.\nInstead, cooldowns applied to this item will only be shared with any other items that are part of the same cooldown group.",
                "key": "cooldown_group",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "cooldown_group"
                                        }
                                    },
                                    "definition": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "boolean",
                                            "value": True
                                        }
                                    }
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

