# Generated from symbols.json for ::java::util::text::ItemHoverContent
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.DataComponentPatch import DataComponentPatch


@dataclass(kw_only=True)
class ItemHoverContent:
    id: str
    count: int | None = None
    components: DataComponentPatch | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ItemHoverContent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "item"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "count",
                "type": {
                    "kind": "int"
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "tag",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "nbt",
                            "value": {
                                "kind": "dispatcher",
                                "parallelIndices": [
                                    {
                                        "kind": "dynamic",
                                        "accessor": [
                                            "id"
                                        ]
                                    }
                                ],
                                "registry": "minecraft:item"
                            }
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
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "components",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::DataComponentPatch"
                },
                "optional": True
            }
        ]
    }
}

