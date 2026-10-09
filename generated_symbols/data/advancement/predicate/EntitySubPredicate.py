"""
Generated from symbols.json for ::java::data::advancement::predicate::EntitySubPredicate
Local link to file: generated_symbols/data/advancement/predicate/EntitySubPredicate.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from generated_symbols.base import GeneratedModel
from generated_symbols.data.advancement.predicate.DistancePredicate import DistancePredicate
from generated_symbols.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
from generated_symbols.data.advancement.predicate.EntityTagPredicate import EntityTagPredicate
from generated_symbols.data.advancement.predicate.FishingHookPredicate import FishingHookPredicate
from generated_symbols.data.advancement.predicate.LightningBoltPredicate import LightningBoltPredicate
from generated_symbols.data.advancement.predicate.LocationPredicate import LocationPredicate
from generated_symbols.data.advancement.predicate.MovementPredicate import MovementPredicate
from generated_symbols.data.advancement.predicate.PlayerPredicate import PlayerPredicate
from generated_symbols.data.advancement.predicate.RaiderPredicate import RaiderPredicate
from generated_symbols.data.advancement.predicate.SheepPredicate import SheepPredicate
from generated_symbols.data.advancement.predicate.SlimePredicate import SlimePredicate
from pydantic import Field


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
    EntitySubPredicateComponents | EntitySubPredicateDistance | EntitySubPredicateEffects | EntitySubPredicateEntityTags | EntitySubPredicateEntityType | EntitySubPredicateEquipment | EntitySubPredicateFlags | EntitySubPredicateLocation | EntitySubPredicateMovement | EntitySubPredicateMovementAffectedBy | EntitySubPredicateNbt | EntitySubPredicatePassenger | EntitySubPredicatePeriodicTick | EntitySubPredicatePredicates | EntitySubPredicateSlots | EntitySubPredicateSteppingOn | EntitySubPredicateTargetedEntity | EntitySubPredicateTeam | EntitySubPredicateTypeSpecificCubeMob | EntitySubPredicateTypeSpecificFishingHook | EntitySubPredicateTypeSpecificLightning | EntitySubPredicateTypeSpecificPlayer | EntitySubPredicateTypeSpecificRaider | EntitySubPredicateTypeSpecificSheep | EntitySubPredicateVehicle,
    Field(discriminator='type'),
]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::EntitySubPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::advancement::predicate::SpecificType",
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
                            ]
                        },
                        {
                            "kind": "string",
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
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "entity_sub_predicate_type"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:entity_sub_predicate"
                }
            }
        ]
    }
}

