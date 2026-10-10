"""
Generated from symbols.json for ::java::data::enchantment::Enchantment
Local link to file: vanilla_mcdoc/data/enchantment/Enchantment.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.enchantment.EnchantmentCost import EnchantmentCost
    from vanilla_mcdoc.data.enchantment.effect_component.EnchantmentEffectComponentMap import EnchantmentEffectComponentMap
    from vanilla_mcdoc.registry.KnownItemId import KnownItemId
    from vanilla_mcdoc.util.slot.EquipmentSlotGroup import EquipmentSlotGroup
    from vanilla_mcdoc.util.text.Text import Text


class Enchantment(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'enchantment'

    description: Text
    exclusive_set: Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | list[Annotated[str, IdSpec(registry='enchantment')]] | None = None
    supported_items: Annotated[str, IdSpec(registry='item', tags='allowed')] | KnownItemId | list[Annotated[str, IdSpec(registry='item')] | KnownItemId]
    primary_items: Annotated[str, IdSpec(registry='item', tags='allowed')] | KnownItemId | list[Annotated[str, IdSpec(registry='item')] | KnownItemId] | None = None  # Item types for which this Enchantment shows up in Enchanting Tables and on traded equipment.  Must be a subset of `supported_items`.
    weight: Annotated[int, Field(ge=1, le=1024)]  # How commonly the Enchantment appears, compared to the total combined `weight` of all available Enchantments.
    max_level: Annotated[int, Field(ge=1, le=255)]  # Maximum level of the enchantment.
    min_cost: EnchantmentCost  # Minimum experience cost.
    max_cost: EnchantmentCost  # Maximum experience cost.
    anvil_cost: Annotated[int, Field(ge=0)]  # Halved when an Enchantment is added to a book. The effective fee is multiplied by the level of the Enchantment.
    slots: list[EquipmentSlotGroup]
    effects: EnchantmentEffectComponentMap | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::Enchantment": {
        "kind": "struct",
        "fields": [
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
                "key": "exclusive_set",
                "type": {
                    "kind": "union",
                    "members": [
                        {
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
                                                    "value": "enchantment"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
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
                                                "value": "enchantment"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "supported_items",
                "type": {
                    "kind": "union",
                    "members": [
                        {
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
                                                    "value": "item"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
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
                                                "value": "item"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Item types for which this Enchantment shows up in Enchanting Tables and on traded equipment.\n\nMust be a subset of `supported_items`.",
                "key": "primary_items",
                "type": {
                    "kind": "union",
                    "members": [
                        {
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
                                                    "value": "item"
                                                }
                                            },
                                            "tags": {
                                                "kind": "literal",
                                                "value": {
                                                    "kind": "string",
                                                    "value": "allowed"
                                                }
                                            }
                                        }
                                    }
                                }
                            ]
                        },
                        {
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
                                                "value": "item"
                                            }
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "How commonly the Enchantment appears, compared to the total combined `weight` of all available Enchantments.",
                "key": "weight",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 1024
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Maximum level of the enchantment.",
                "key": "max_level",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1,
                        "max": 255
                    }
                }
            },
            {
                "kind": "pair",
                "desc": "Minimum experience cost.",
                "key": "min_cost",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::EnchantmentCost"
                }
            },
            {
                "kind": "pair",
                "desc": "Maximum experience cost.",
                "key": "max_cost",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::EnchantmentCost"
                }
            },
            {
                "kind": "pair",
                "desc": "Halved when an Enchantment is added to a book.\nThe effective fee is multiplied by the level of the Enchantment.",
                "key": "anvil_cost",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            },
            {
                "kind": "pair",
                "key": "slots",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::slot::EquipmentSlotGroup"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::enchantment::effect_component::EnchantmentEffectComponentMap"
                },
                "optional": True
            }
        ]
    }
}
