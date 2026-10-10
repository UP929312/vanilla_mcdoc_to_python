"""
Generated from symbols.json for ::java::data::villager_trade::VillagerTrade
Local link to file: vanilla_mcdoc/data/villager_trade/VillagerTrade.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.item_modifier.ItemModifierWithoutRootRef import ItemModifierWithoutRootRef
    from vanilla_mcdoc.data.number_provider.FloatNumberProvider import FloatNumberProvider
    from vanilla_mcdoc.data.number_provider.IntNumberProvider import IntNumberProvider
    from vanilla_mcdoc.data.predicate.Predicate import Predicate
    from vanilla_mcdoc.data.villager_trade.TradeCost import TradeCost
    from vanilla_mcdoc.world.item.ItemStackTemplate import ItemStackTemplate


class VillagerTrade(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'villager_trade'

    wants: TradeCost  # Price item required by the merchant.  The count is affected by various factors, including offered item, demand and player reputation.
    additional_wants: TradeCost | None = None  # Second item required by the merchant.  The count is not affected by any factors.
    gives: ItemStackTemplate  # Item being offered by the merchant.
    given_item_modifier: ItemModifierWithoutRootRef | None = None  # Modifiers applied to the `gives` item.  Does **not** support `reference` item modifier.  Some modifiers can affect the price through the `additional_trade_cost` transient component.  The `additional_trade_cost` component is not saved on the offered item.  ID reference is not allowed here.
    max_uses: IntNumberProvider | None = None  # Maximum number of uses of this trade before the villager has to restock. Defaults to `4`.
    reputation_discount: FloatNumberProvider | None = None  # How much demand & reputation each affect the price, is serialized as `priceMultiplier`. Defaults to `0.0`.
    xp: IntNumberProvider | None = None  # Amount to increase the merchant's XP score by that determines their trade tier. Defaults to `1`.
    merchant_predicate: Predicate | None = None  # Check whether the trade should be offered by the merchant.  Does **not** support the `reference` predicate.
    double_trade_price_enchantments: Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | list[Annotated[str, IdSpec(registry='enchantment')]] | None = None  # If the offered enchanted book has the specified enchantments, the price will be affected by doubling the `additional_trade_cost` transient component.
