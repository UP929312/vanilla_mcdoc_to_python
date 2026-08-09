# Generated from symbols.json for ::java::util::memory::Memories
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.memory.AdmiringDisable import AdmiringDisable
    from generated_symbols.util.memory.AdmiringItem import AdmiringItem
    from generated_symbols.util.memory.AngryAt import AngryAt
    from generated_symbols.util.memory.AttackTargetCooldown import AttackTargetCooldown
    from generated_symbols.util.memory.BreezeJumpCooldown import BreezeJumpCooldown
    from generated_symbols.util.memory.BreezeJumpInhaling import BreezeJumpInhaling
    from generated_symbols.util.memory.BreezeJumpTarget import BreezeJumpTarget
    from generated_symbols.util.memory.BreezeLeavingWater import BreezeLeavingWater
    from generated_symbols.util.memory.BreezeShoot import BreezeShoot
    from generated_symbols.util.memory.BreezeShootCharging import BreezeShootCharging
    from generated_symbols.util.memory.BreezeShootCooldown import BreezeShootCooldown
    from generated_symbols.util.memory.BreezeShootRecover import BreezeShootRecover
    from generated_symbols.util.memory.ChargeCooldownTicks import ChargeCooldownTicks
    from generated_symbols.util.memory.DangerDetectedRecently import DangerDetectedRecently
    from generated_symbols.util.memory.DigCooldown import DigCooldown
    from generated_symbols.util.memory.GazeCooldownTicks import GazeCooldownTicks
    from generated_symbols.util.memory.GolemDetectedRecently import GolemDetectedRecently
    from generated_symbols.util.memory.HasHuntingCooldown import HasHuntingCooldown
    from generated_symbols.util.memory.Home import Home
    from generated_symbols.util.memory.HuntedRecently import HuntedRecently
    from generated_symbols.util.memory.IsEmerging import IsEmerging
    from generated_symbols.util.memory.IsInWater import IsInWater
    from generated_symbols.util.memory.IsPanicking import IsPanicking
    from generated_symbols.util.memory.IsPregnant import IsPregnant
    from generated_symbols.util.memory.IsSniffing import IsSniffing
    from generated_symbols.util.memory.IsTempted import IsTempted
    from generated_symbols.util.memory.ItemPickupCooldownTicks import ItemPickupCooldownTicks
    from generated_symbols.util.memory.JobSite import JobSite
    from generated_symbols.util.memory.LastSlept import LastSlept
    from generated_symbols.util.memory.LastWoken import LastWoken
    from generated_symbols.util.memory.LastWorkedAtPoi import LastWorkedAtPoi
    from generated_symbols.util.memory.LikedNoteblock import LikedNoteblock
    from generated_symbols.util.memory.LikedNoteblockCooldownTicks import LikedNoteblockCooldownTicks
    from generated_symbols.util.memory.LikedPlayer import LikedPlayer
    from generated_symbols.util.memory.LongJumpCoolingDown import LongJumpCoolingDown
    from generated_symbols.util.memory.MeetingPoint import MeetingPoint
    from generated_symbols.util.memory.PlayDeadTicks import PlayDeadTicks
    from generated_symbols.util.memory.PotentialJobSite import PotentialJobSite
    from generated_symbols.util.memory.RamCooldownTicks import RamCooldownTicks
    from generated_symbols.util.memory.RecentProjectile import RecentProjectile
    from generated_symbols.util.memory.RoarSoundCooldown import RoarSoundCooldown
    from generated_symbols.util.memory.RoarSoundDelay import RoarSoundDelay
    from generated_symbols.util.memory.SniffCooldown import SniffCooldown
    from generated_symbols.util.memory.SnifferExploredPositions import SnifferExploredPositions
    from generated_symbols.util.memory.SonicBoomCooldown import SonicBoomCooldown
    from generated_symbols.util.memory.SonicBoomSoundCooldown import SonicBoomSoundCooldown
    from generated_symbols.util.memory.SonicBoomSoundDelay import SonicBoomSoundDelay
    from generated_symbols.util.memory.TemptationCooldownTicks import TemptationCooldownTicks
    from generated_symbols.util.memory.TouchCooldown import TouchCooldown
    from generated_symbols.util.memory.UniversalAnger import UniversalAnger
    from generated_symbols.util.memory.UnreachableTransportBlockPositions import UnreachableTransportBlockPositions
    from generated_symbols.util.memory.VibrationCooldown import VibrationCooldown
    from generated_symbols.util.memory.VisitedBlockPositions import VisitedBlockPositions


type Memories = dict[Annotated[str, IdSpec(registry='memory_module_type')], None | AdmiringDisable | AdmiringItem | AngryAt | AttackTargetCooldown | BreezeJumpCooldown | BreezeJumpInhaling | BreezeJumpTarget | BreezeLeavingWater | BreezeShoot | BreezeShootCharging | BreezeShootCooldown | BreezeShootRecover | ChargeCooldownTicks | DangerDetectedRecently | DigCooldown | GazeCooldownTicks | GolemDetectedRecently | HasHuntingCooldown | Home | HuntedRecently | IsEmerging | IsInWater | IsPanicking | IsPregnant | IsSniffing | IsTempted | ItemPickupCooldownTicks | JobSite | LastSlept | LastWoken | LastWorkedAtPoi | LikedNoteblock | LikedNoteblockCooldownTicks | LikedPlayer | LongJumpCoolingDown | MeetingPoint | PlayDeadTicks | PotentialJobSite | RamCooldownTicks | RecentProjectile | RoarSoundCooldown | RoarSoundDelay | SniffCooldown | SnifferExploredPositions | SonicBoomCooldown | SonicBoomSoundCooldown | SonicBoomSoundDelay | TemptationCooldownTicks | TouchCooldown | UniversalAnger | UnreachableTransportBlockPositions | VibrationCooldown | VisitedBlockPositions]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::memory::Memories": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "memory_module_type"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                {
                                    "keyword": "key"
                                }
                            ]
                        }
                    ],
                    "registry": "minecraft:memory_module"
                }
            }
        ]
    }
}

