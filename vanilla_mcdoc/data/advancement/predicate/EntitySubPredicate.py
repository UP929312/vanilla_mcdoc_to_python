"""
Generated from symbols.json for ::java::data::advancement::predicate::EntitySubPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/EntitySubPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.advancement.predicate.DistancePredicate import DistancePredicate
from vanilla_mcdoc.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
from vanilla_mcdoc.data.advancement.predicate.EntityTagPredicate import EntityTagPredicate
from vanilla_mcdoc.data.advancement.predicate.FishingHookPredicate import FishingHookPredicate
from vanilla_mcdoc.data.advancement.predicate.LightningBoltPredicate import LightningBoltPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.predicate.MovementPredicate import MovementPredicate
from vanilla_mcdoc.data.advancement.predicate.PlayerPredicate import PlayerPredicate
from vanilla_mcdoc.data.advancement.predicate.RaiderPredicate import RaiderPredicate
from vanilla_mcdoc.data.advancement.predicate.SheepPredicate import SheepPredicate
from vanilla_mcdoc.data.advancement.predicate.SlimePredicate import SlimePredicate


class EntitySubPredicateComponents(GeneratedModel):
    type: Literal['minecraft:components', 'components'] = 'minecraft:components'


class EntitySubPredicateDistance(DistancePredicate):
    type: Literal['minecraft:distance', 'distance'] = 'minecraft:distance'


class EntitySubPredicateEffects(GeneratedModel):
    type: Literal['minecraft:effects', 'effects'] = 'minecraft:effects'


class EntitySubPredicateEntityTags(EntityTagPredicate):
    type: Literal['minecraft:entity_tags', 'entity_tags'] = 'minecraft:entity_tags'


class EntitySubPredicateEntityType(GeneratedModel):
    type: Literal['minecraft:entity_type', 'entity_type'] = 'minecraft:entity_type'


class EntitySubPredicateEquipment(GeneratedModel):
    type: Literal['minecraft:equipment', 'equipment'] = 'minecraft:equipment'


class EntitySubPredicateFlags(EntityFlagsPredicate):
    type: Literal['minecraft:flags', 'flags'] = 'minecraft:flags'


class EntitySubPredicateLocation(LocationPredicate):
    type: Literal['minecraft:location', 'location'] = 'minecraft:location'


class EntitySubPredicateMovement(MovementPredicate):
    type: Literal['minecraft:movement', 'movement'] = 'minecraft:movement'


class EntitySubPredicateMovementAffectedBy(LocationPredicate):
    type: Literal['minecraft:movement_affected_by', 'movement_affected_by'] = 'minecraft:movement_affected_by'


class EntitySubPredicateNbt(GeneratedModel):
    type: Literal['minecraft:nbt', 'nbt'] = 'minecraft:nbt'


class EntitySubPredicatePassenger(GeneratedModel):
    type: Literal['minecraft:passenger', 'passenger'] = 'minecraft:passenger'


class EntitySubPredicatePeriodicTick(GeneratedModel):
    type: Literal['minecraft:periodic_tick', 'periodic_tick'] = 'minecraft:periodic_tick'


class EntitySubPredicatePredicates(GeneratedModel):
    type: Literal['minecraft:predicates', 'predicates'] = 'minecraft:predicates'


class EntitySubPredicateSlots(GeneratedModel):
    type: Literal['minecraft:slots', 'slots'] = 'minecraft:slots'


class EntitySubPredicateSteppingOn(LocationPredicate):
    type: Literal['minecraft:stepping_on', 'stepping_on'] = 'minecraft:stepping_on'


class EntitySubPredicateTargetedEntity(GeneratedModel):
    type: Literal['minecraft:targeted_entity', 'targeted_entity'] = 'minecraft:targeted_entity'


class EntitySubPredicateTeam(GeneratedModel):
    type: Literal['minecraft:team', 'team'] = 'minecraft:team'


class EntitySubPredicateTypeSpecificCubeMob(SlimePredicate):
    type: Literal['minecraft:type_specific/cube_mob', 'type_specific/cube_mob'] = 'minecraft:type_specific/cube_mob'


class EntitySubPredicateTypeSpecificFishingHook(FishingHookPredicate):
    type: Literal['minecraft:type_specific/fishing_hook', 'type_specific/fishing_hook'] = 'minecraft:type_specific/fishing_hook'


class EntitySubPredicateTypeSpecificLightning(LightningBoltPredicate):
    type: Literal['minecraft:type_specific/lightning', 'type_specific/lightning'] = 'minecraft:type_specific/lightning'


class EntitySubPredicateTypeSpecificPlayer(PlayerPredicate):
    type: Literal['minecraft:type_specific/player', 'type_specific/player'] = 'minecraft:type_specific/player'


class EntitySubPredicateTypeSpecificRaider(RaiderPredicate):
    type: Literal['minecraft:type_specific/raider', 'type_specific/raider'] = 'minecraft:type_specific/raider'


class EntitySubPredicateTypeSpecificSheep(SheepPredicate):
    type: Literal['minecraft:type_specific/sheep', 'type_specific/sheep'] = 'minecraft:type_specific/sheep'


class EntitySubPredicateVehicle(GeneratedModel):
    type: Literal['minecraft:vehicle', 'vehicle'] = 'minecraft:vehicle'


type EntitySubPredicate = Annotated[
    Annotated[EntitySubPredicateComponents, Tag('minecraft:components')]
    | Annotated[EntitySubPredicateDistance, Tag('minecraft:distance')]
    | Annotated[EntitySubPredicateEffects, Tag('minecraft:effects')]
    | Annotated[EntitySubPredicateEntityTags, Tag('minecraft:entity_tags')]
    | Annotated[EntitySubPredicateEntityType, Tag('minecraft:entity_type')]
    | Annotated[EntitySubPredicateEquipment, Tag('minecraft:equipment')]
    | Annotated[EntitySubPredicateFlags, Tag('minecraft:flags')]
    | Annotated[EntitySubPredicateLocation, Tag('minecraft:location')]
    | Annotated[EntitySubPredicateMovement, Tag('minecraft:movement')]
    | Annotated[EntitySubPredicateMovementAffectedBy, Tag('minecraft:movement_affected_by')]
    | Annotated[EntitySubPredicateNbt, Tag('minecraft:nbt')]
    | Annotated[EntitySubPredicatePassenger, Tag('minecraft:passenger')]
    | Annotated[EntitySubPredicatePeriodicTick, Tag('minecraft:periodic_tick')]
    | Annotated[EntitySubPredicatePredicates, Tag('minecraft:predicates')]
    | Annotated[EntitySubPredicateSlots, Tag('minecraft:slots')]
    | Annotated[EntitySubPredicateSteppingOn, Tag('minecraft:stepping_on')]
    | Annotated[EntitySubPredicateTargetedEntity, Tag('minecraft:targeted_entity')]
    | Annotated[EntitySubPredicateTeam, Tag('minecraft:team')]
    | Annotated[EntitySubPredicateTypeSpecificCubeMob, Tag('minecraft:type_specific/cube_mob')]
    | Annotated[EntitySubPredicateTypeSpecificFishingHook, Tag('minecraft:type_specific/fishing_hook')]
    | Annotated[EntitySubPredicateTypeSpecificLightning, Tag('minecraft:type_specific/lightning')]
    | Annotated[EntitySubPredicateTypeSpecificPlayer, Tag('minecraft:type_specific/player')]
    | Annotated[EntitySubPredicateTypeSpecificRaider, Tag('minecraft:type_specific/raider')]
    | Annotated[EntitySubPredicateTypeSpecificSheep, Tag('minecraft:type_specific/sheep')]
    | Annotated[EntitySubPredicateVehicle, Tag('minecraft:vehicle')],
    Discriminator(tag_of('type')),
]
