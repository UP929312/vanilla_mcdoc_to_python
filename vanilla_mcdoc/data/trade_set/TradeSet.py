"""
Generated from symbols.json for ::java::data::trade_set::TradeSet
Local link to file: vanilla_mcdoc/data/trade_set/TradeSet.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.number_provider.IntNumberProvider import IntNumberProvider


class TradeSet(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'trade_set'

    trades: Annotated[str, IdSpec(registry='villager_trade', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_trade')]]  # Possible trade generators.
    amount: IntNumberProvider  # Amount of trades to be generated.
    allow_duplicates: bool | None = None  # Whether the trade set can use the same generator multiple times and generate duplicate trades. Defaults to `false`.
    random_sequence: Annotated[str, IdSpec(registry='random_sequence', definition=True)] | None = None
