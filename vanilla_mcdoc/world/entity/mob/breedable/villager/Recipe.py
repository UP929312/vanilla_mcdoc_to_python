"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::Recipe
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/villager/Recipe.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.entity.mob.breedable.villager.ItemCost import ItemCost
    from vanilla_mcdoc.world.item.ItemStack import ItemStack


class Recipe(GeneratedModel):
    rewardExp: bool | None = None  # Whether it should reward experience for using this trade.  Experience amount is `3 + random(0, 3)` plus `5` if the trade is causing the merchant to increase in tier.
    maxUses: Annotated[int, Field(ge=0)] | None = None  # Maximum number of uses for this trade before the merchant has to restock.
    uses: Annotated[int, Field(ge=0)] | None = None  # Times this trade has been used since the merchant last restocked.
    buy: ItemCost | None = None  # Price item required by the merchant, count is modified depending on `demand` & per-player context.
    buyB: ItemCost | None = None  # Second item required by the merchant, count does not change.
    sell: ItemStack | None = None  # Item being offered by the merchant.
    xp: Annotated[int, Field(ge=0)] | None = None  # XP the merchant gains from the trade.
    priceMultiplier: float | None = None  # How much demand & reputation each affect the count of the `buy` item.
    specialPrice: int | None = None  # Modifier added to the original count of the `buy` item.
    demand: int | None = None  # Count adjuster of the `buy` item based on demand.  Minus twice the number of times the villager has the trade in stock. When restocking subtract the number of possible purchases before running out of stock and add twice the number of actually made purchases. When the demand becomes positive, the count is increased by the initial count times `priceMultiplier` times the demand.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::Recipe": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Whether it should reward experience for using this trade.\n\nExperience amount is `3 + random(0, 3)` plus `5` if the trade is causing the merchant to increase in tier.",
                "key": "rewardExp",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Maximum number of uses for this trade before the merchant has to restock.",
                "key": "maxUses",
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
                "desc": "Times this trade has been used since the merchant last restocked.",
                "key": "uses",
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
                "desc": "Price item required by the merchant, count is modified depending on `demand` & per-player context.",
                "key": "buy",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::ItemCost"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Second item required by the merchant, count does not change.",
                "key": "buyB",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::ItemCost"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Item being offered by the merchant.",
                "key": "sell",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "XP the merchant gains from the trade.",
                "key": "xp",
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
                "desc": "How much demand & reputation each affect the count of the `buy` item.",
                "key": "priceMultiplier",
                "type": {
                    "kind": "float"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Modifier added to the original count of the `buy` item.",
                "key": "specialPrice",
                "type": {
                    "kind": "int"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Count adjuster of the `buy` item based on demand.\n\nMinus twice the number of times the villager has the trade in stock.\nWhen restocking subtract the number of possible purchases before running out of stock and add twice the number of actually made purchases.\nWhen the demand becomes positive, the count is increased by the initial count times `priceMultiplier` times the demand.",
                "key": "demand",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
