"""
Generated from symbols.json for ::java::data::advancement::predicate::PlayerPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/PlayerPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.EntityPredicate import EntityPredicate
    from vanilla_mcdoc.data.advancement.predicate.GameMode import GameMode
    from vanilla_mcdoc.data.advancement.predicate.StatisticPredicate import StatisticPredicate
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class InputStruct(GeneratedModel):
    forward: bool | None = None
    backward: bool | None = None
    left: bool | None = None
    right: bool | None = None
    jump: bool | None = None
    sneak: bool | None = None
    sprint: bool | None = None


class FoodStruct(GeneratedModel):
    level: MinMaxBounds[int] | int | None = None
    saturation: MinMaxBounds[float] | float | None = None


class PlayerPredicate(GeneratedModel):
    advancements: dict[Annotated[str, IdSpec(registry='advancement')], bool | dict[str, bool]] | None = None
    gamemode: list[GameMode] | None = None
    level: MinMaxBounds[int] | int | None = None  # Experience/XP level.
    recipes: dict[Annotated[str, IdSpec(registry='recipe')], bool] | None = None
    stats: list[StatisticPredicate] | None = None
    looking_at: EntityPredicate | None = None
    input: InputStruct | None = None  # Checks the movement keys of the player.
    food: FoodStruct | None = None
