# Generated from symbols.json for ::java::world::entity::mob::breedable::villager::Villager
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated
from generated_symbols.world.entity.mob.breedable.Breedable import Breedable
from generated_symbols.world.entity.mob.breedable.villager.VillagerBase import VillagerBase

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.breedable.villager.PlayerReputationPart import PlayerReputationPart
    from generated_symbols.world.entity.mob.breedable.villager.VillagerData import VillagerData


@dataclass(kw_only=True)
class Villager(Breedable, VillagerBase):
    VillagerData: VillagerData | None = None
    FoodLevel: Annotated[int, 'Range | `0`-`12` | both inclusive'] | None = None  # Determines whether the villager will be available to reproduce.  When the value is `12` the villager can reproduce.  After reproducing, the value is reset to `0`.  To increase this value villagers will pick up food that is in range.  Foods: Potatoes, Carrots, & Beetroots increase the level by `1`. Bread increases the level by `4`.
    Gossips: list[PlayerReputationPart] | None = None  # Affects per-player reputation which affects trade offer pricing and iron golem behavior.  Reputation is assembled through events the villager has witnessed (within 16 blocks) or heard about from other villagers through gossip.  All reputation parts decay over time except `major_positive` which is only ever increased (when the villager is cured).  Decay occurs every 24k ticks (20 minutes), tracked by `LastGossipDecay`.  Once a reputation part decays to zero it is removed from the list.
    LastGossipDecay: int | None = None  # Last game-tick every gossip significance `Value` could have decayed.  Once this reaches 24k (20 minutes) less than the current game tick a decay occurs again.
    LastRestock: int | None = None  # Last game-tick it removed `uses` & updated `demand` of every trade offer by going to its `job_site`.
    RestocksToday: Annotated[int, 'Range | `0`-`2` | both inclusive'] | None = None  # Times it has reset the `uses` & updated `demand` of every trade offer by going to its `job_site` in the past 12k ticks (10 minutes).  Time is tracked by `LastRestock`.  When two restocks have occurred, another restock (and reset of this value to `0`) will only occur after 10 minutes.
    Xp: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # XP it has, increases when trades are used by each trade offer's `xp` value.  After `250` the XP will continue to increase, but will do nothing more.  Trade tiers: - `0..9`     - Tier 1: Novice - `10..69`   - Tier 2: Apprentice - `70..149`  - Tier 3: Journeyman - `150..249` - Tier 4: Expert - `250..`    - Tier 5: Master


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::breedable::villager::Villager": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::Breedable"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::VillagerBase"
                }
            },
            {
                "kind": "pair",
                "key": "VillagerData",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::breedable::villager::VillagerData"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Determines whether the villager will be available to reproduce.\n\nWhen the value is `12` the villager can reproduce.\n\nAfter reproducing, the value is reset to `0`.\n\nTo increase this value villagers will pick up food that is in range.\n\nFoods: Potatoes, Carrots, & Beetroots increase the level by `1`. Bread increases the level by `4`.",
                "key": "FoodLevel",
                "type": {
                    "kind": "byte",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 12
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Affects per-player reputation which affects trade offer pricing and iron golem behavior.\n\nReputation is assembled through events the villager has witnessed (within 16 blocks) or heard about from other villagers through gossip.\n\nAll reputation parts decay over time except `major_positive` which is only ever increased (when the villager is cured).\n\nDecay occurs every 24k ticks (20 minutes), tracked by `LastGossipDecay`.\n\nOnce a reputation part decays to zero it is removed from the list.",
                "key": "Gossips",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::entity::mob::breedable::villager::PlayerReputationPart"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Last game-tick every gossip significance `Value` could have decayed.\n\nOnce this reaches 24k (20 minutes) less than the current game tick a decay occurs again.",
                "key": "LastGossipDecay",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Last game-tick it removed `uses` & updated `demand` of every trade offer by going to its `job_site`.",
                "key": "LastRestock",
                "type": {
                    "kind": "long"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Times it has reset the `uses` & updated `demand` of every trade offer by going to its `job_site` in the past 12k ticks (10 minutes).\n\nTime is tracked by `LastRestock`.\n\nWhen two restocks have occurred, another restock (and reset of this value to `0`) will only occur after 10 minutes.",
                "key": "RestocksToday",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 2
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "XP it has, increases when trades are used by each trade offer's `xp` value.\n\nAfter `250` the XP will continue to increase, but will do nothing more.\n\nTrade tiers:\n- `0..9`     - Tier 1: Novice\n- `10..69`   - Tier 2: Apprentice\n- `70..149`  - Tier 3: Journeyman\n- `150..249` - Tier 4: Expert\n- `250..`    - Tier 5: Master",
                "key": "Xp",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}

