"""
Generated from symbols.json for ::java::world::entity::mob::breedable::villager::PlayerReputationPart
Local link to file: vanilla_mcdoc/world/entity/mob/breedable/villager/PlayerReputationPart.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Field, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.minecraft_types import MinecraftUUID


class PlayerReputationPartMajorNegative(GeneratedModel):
    Type: Literal['minecraft:major_negative', 'major_negative'] | None = 'minecraft:major_negative'
    Value: Annotated[int, Field(ge=5, le=100)] | None = None
    Target: MinecraftUUID | None = None  # UUID of the player that caused the gossip-worthy event(s) related to this reputation part.


class PlayerReputationPartMajorPositive(GeneratedModel):
    Type: Literal['minecraft:major_positive', 'major_positive'] | None = 'minecraft:major_positive'
    Value: Literal[20] | None = 20
    Target: MinecraftUUID | None = None  # UUID of the player that caused the gossip-worthy event(s) related to this reputation part.


class PlayerReputationPartMinorNegative(GeneratedModel):
    Type: Literal['minecraft:minor_negative', 'minor_negative'] | None = 'minecraft:minor_negative'
    Value: Annotated[int, Field(ge=5, le=200)] | None = None
    Target: MinecraftUUID | None = None  # UUID of the player that caused the gossip-worthy event(s) related to this reputation part.


class PlayerReputationPartMinorPositive(GeneratedModel):
    Type: Literal['minecraft:minor_positive', 'minor_positive'] | None = 'minecraft:minor_positive'
    Value: Annotated[int, Field(ge=1, le=25)] | None = None
    Target: MinecraftUUID | None = None  # UUID of the player that caused the gossip-worthy event(s) related to this reputation part.


class PlayerReputationPartTrading(GeneratedModel):
    Type: Literal['minecraft:trading', 'trading'] | None = 'minecraft:trading'
    Value: Annotated[int, Field(ge=1, le=25)] | None = None
    Target: MinecraftUUID | None = None  # UUID of the player that caused the gossip-worthy event(s) related to this reputation part.


type PlayerReputationPart = Annotated[
    Annotated[PlayerReputationPartMajorNegative, Tag('minecraft:major_negative')]
    | Annotated[PlayerReputationPartMajorPositive, Tag('minecraft:major_positive')]
    | Annotated[PlayerReputationPartMinorNegative, Tag('minecraft:minor_negative')]
    | Annotated[PlayerReputationPartMinorPositive, Tag('minecraft:minor_positive')]
    | Annotated[PlayerReputationPartTrading, Tag('minecraft:trading')],
    Discriminator(tag_of('Type')),
]
