"""
Generated from symbols.json for ::java::data::advancement::predicate::EntitySubPredicate
Local link to file: generated_symbols/data/advancement/predicate/EntitySubPredicate.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Literal

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


@dataclass(kw_only=True)
class EntitySubPredicateComponents:
    type: Literal['minecraft:components'] = 'minecraft:components'


@dataclass(kw_only=True)
class EntitySubPredicateDistance(DistancePredicate):
    type: Literal['minecraft:distance'] = 'minecraft:distance'


@dataclass(kw_only=True)
class EntitySubPredicateEffects:
    type: Literal['minecraft:effects'] = 'minecraft:effects'


@dataclass(kw_only=True)
class EntitySubPredicateEntityTags(EntityTagPredicate):
    type: Literal['minecraft:entity_tags'] = 'minecraft:entity_tags'


@dataclass(kw_only=True)
class EntitySubPredicateEntityType:
    type: Literal['minecraft:entity_type'] = 'minecraft:entity_type'


@dataclass(kw_only=True)
class EntitySubPredicateEquipment:
    type: Literal['minecraft:equipment'] = 'minecraft:equipment'


@dataclass(kw_only=True)
class EntitySubPredicateFlags(EntityFlagsPredicate):
    type: Literal['minecraft:flags'] = 'minecraft:flags'


@dataclass(kw_only=True)
class EntitySubPredicateLocation(LocationPredicate):
    type: Literal['minecraft:location'] = 'minecraft:location'


@dataclass(kw_only=True)
class EntitySubPredicateMovement(MovementPredicate):
    type: Literal['minecraft:movement'] = 'minecraft:movement'


@dataclass(kw_only=True)
class EntitySubPredicateMovementAffectedBy(LocationPredicate):
    type: Literal['minecraft:movement_affected_by'] = 'minecraft:movement_affected_by'


@dataclass(kw_only=True)
class EntitySubPredicateNbt:
    type: Literal['minecraft:nbt'] = 'minecraft:nbt'


@dataclass(kw_only=True)
class EntitySubPredicatePassenger:
    type: Literal['minecraft:passenger'] = 'minecraft:passenger'


@dataclass(kw_only=True)
class EntitySubPredicatePeriodicTick:
    type: Literal['minecraft:periodic_tick'] = 'minecraft:periodic_tick'


@dataclass(kw_only=True)
class EntitySubPredicatePredicates:
    type: Literal['minecraft:predicates'] = 'minecraft:predicates'


@dataclass(kw_only=True)
class EntitySubPredicateSlots:
    type: Literal['minecraft:slots'] = 'minecraft:slots'


@dataclass(kw_only=True)
class EntitySubPredicateSteppingOn(LocationPredicate):
    type: Literal['minecraft:stepping_on'] = 'minecraft:stepping_on'


@dataclass(kw_only=True)
class EntitySubPredicateTargetedEntity:
    type: Literal['minecraft:targeted_entity'] = 'minecraft:targeted_entity'


@dataclass(kw_only=True)
class EntitySubPredicateTeam:
    type: Literal['minecraft:team'] = 'minecraft:team'


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificCubeMob(SlimePredicate):
    type: Literal['minecraft:type_specific/cube_mob'] = 'minecraft:type_specific/cube_mob'


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificFishingHook(FishingHookPredicate):
    type: Literal['minecraft:type_specific/fishing_hook'] = 'minecraft:type_specific/fishing_hook'


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificLightning(LightningBoltPredicate):
    type: Literal['minecraft:type_specific/lightning'] = 'minecraft:type_specific/lightning'


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificPlayer(PlayerPredicate):
    type: Literal['minecraft:type_specific/player'] = 'minecraft:type_specific/player'


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificRaider(RaiderPredicate):
    type: Literal['minecraft:type_specific/raider'] = 'minecraft:type_specific/raider'


@dataclass(kw_only=True)
class EntitySubPredicateTypeSpecificSheep(SheepPredicate):
    type: Literal['minecraft:type_specific/sheep'] = 'minecraft:type_specific/sheep'


@dataclass(kw_only=True)
class EntitySubPredicateVehicle:
    type: Literal['minecraft:vehicle'] = 'minecraft:vehicle'


type EntitySubPredicate = EntitySubPredicateComponents | EntitySubPredicateDistance | EntitySubPredicateEffects | EntitySubPredicateEntityTags | EntitySubPredicateEntityType | EntitySubPredicateEquipment | EntitySubPredicateFlags | EntitySubPredicateLocation | EntitySubPredicateMovement | EntitySubPredicateMovementAffectedBy | EntitySubPredicateNbt | EntitySubPredicatePassenger | EntitySubPredicatePeriodicTick | EntitySubPredicatePredicates | EntitySubPredicateSlots | EntitySubPredicateSteppingOn | EntitySubPredicateTargetedEntity | EntitySubPredicateTeam | EntitySubPredicateTypeSpecificCubeMob | EntitySubPredicateTypeSpecificFishingHook | EntitySubPredicateTypeSpecificLightning | EntitySubPredicateTypeSpecificPlayer | EntitySubPredicateTypeSpecificRaider | EntitySubPredicateTypeSpecificSheep | EntitySubPredicateVehicle


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

