"""
Generated from symbols.json for ::java::util::memory::Memories
Local link to file: vanilla_mcdoc/util/memory/Memories.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.memory.AdmiringDisable import AdmiringDisable
    from vanilla_mcdoc.util.memory.AdmiringItem import AdmiringItem
    from vanilla_mcdoc.util.memory.AngryAt import AngryAt
    from vanilla_mcdoc.util.memory.AttackTargetCooldown import AttackTargetCooldown
    from vanilla_mcdoc.util.memory.BreezeJumpCooldown import BreezeJumpCooldown
    from vanilla_mcdoc.util.memory.BreezeJumpInhaling import BreezeJumpInhaling
    from vanilla_mcdoc.util.memory.BreezeJumpTarget import BreezeJumpTarget
    from vanilla_mcdoc.util.memory.BreezeLeavingWater import BreezeLeavingWater
    from vanilla_mcdoc.util.memory.BreezeShoot import BreezeShoot
    from vanilla_mcdoc.util.memory.BreezeShootCharging import BreezeShootCharging
    from vanilla_mcdoc.util.memory.BreezeShootCooldown import BreezeShootCooldown
    from vanilla_mcdoc.util.memory.BreezeShootRecover import BreezeShootRecover
    from vanilla_mcdoc.util.memory.ChargeCooldownTicks import ChargeCooldownTicks
    from vanilla_mcdoc.util.memory.DangerDetectedRecently import DangerDetectedRecently
    from vanilla_mcdoc.util.memory.DigCooldown import DigCooldown
    from vanilla_mcdoc.util.memory.GazeCooldownTicks import GazeCooldownTicks
    from vanilla_mcdoc.util.memory.GolemDetectedRecently import GolemDetectedRecently
    from vanilla_mcdoc.util.memory.HasHuntingCooldown import HasHuntingCooldown
    from vanilla_mcdoc.util.memory.Home import Home
    from vanilla_mcdoc.util.memory.HuntedRecently import HuntedRecently
    from vanilla_mcdoc.util.memory.IsEmerging import IsEmerging
    from vanilla_mcdoc.util.memory.IsInWater import IsInWater
    from vanilla_mcdoc.util.memory.IsPanicking import IsPanicking
    from vanilla_mcdoc.util.memory.IsPregnant import IsPregnant
    from vanilla_mcdoc.util.memory.IsSniffing import IsSniffing
    from vanilla_mcdoc.util.memory.ItemPickupCooldownTicks import ItemPickupCooldownTicks
    from vanilla_mcdoc.util.memory.JobSite import JobSite
    from vanilla_mcdoc.util.memory.LastSlept import LastSlept
    from vanilla_mcdoc.util.memory.LastWoken import LastWoken
    from vanilla_mcdoc.util.memory.LastWorkedAtPoi import LastWorkedAtPoi
    from vanilla_mcdoc.util.memory.LikedNoteblock import LikedNoteblock
    from vanilla_mcdoc.util.memory.LikedNoteblockCooldownTicks import LikedNoteblockCooldownTicks
    from vanilla_mcdoc.util.memory.LikedPlayer import LikedPlayer
    from vanilla_mcdoc.util.memory.LongJumpCoolingDown import LongJumpCoolingDown
    from vanilla_mcdoc.util.memory.MeetingPoint import MeetingPoint
    from vanilla_mcdoc.util.memory.PlayDeadTicks import PlayDeadTicks
    from vanilla_mcdoc.util.memory.PotentialJobSite import PotentialJobSite
    from vanilla_mcdoc.util.memory.RamCooldownTicks import RamCooldownTicks
    from vanilla_mcdoc.util.memory.RecentProjectile import RecentProjectile
    from vanilla_mcdoc.util.memory.RoarSoundCooldown import RoarSoundCooldown
    from vanilla_mcdoc.util.memory.RoarSoundDelay import RoarSoundDelay
    from vanilla_mcdoc.util.memory.SniffCooldown import SniffCooldown
    from vanilla_mcdoc.util.memory.SnifferExploredPositions import SnifferExploredPositions
    from vanilla_mcdoc.util.memory.SonicBoomCooldown import SonicBoomCooldown
    from vanilla_mcdoc.util.memory.SonicBoomSoundCooldown import SonicBoomSoundCooldown
    from vanilla_mcdoc.util.memory.SonicBoomSoundDelay import SonicBoomSoundDelay
    from vanilla_mcdoc.util.memory.TemptationCooldownTicks import TemptationCooldownTicks
    from vanilla_mcdoc.util.memory.TouchCooldown import TouchCooldown
    from vanilla_mcdoc.util.memory.UniversalAnger import UniversalAnger
    from vanilla_mcdoc.util.memory.UnreachableTransportBlockPositions import UnreachableTransportBlockPositions
    from vanilla_mcdoc.util.memory.VibrationCooldown import VibrationCooldown
    from vanilla_mcdoc.util.memory.VisitedBlockPositions import VisitedBlockPositions


class Memories(GeneratedModel):
    admiring_disabled: AdmiringDisable | None = Field(default=None, validation_alias='minecraft:admiring_disabled', serialization_alias='minecraft:admiring_disabled')
    admiring_item: AdmiringItem | None = Field(default=None, validation_alias='minecraft:admiring_item', serialization_alias='minecraft:admiring_item')
    angry_at: AngryAt | None = Field(default=None, validation_alias='minecraft:angry_at', serialization_alias='minecraft:angry_at')
    attack_target_cooldown: AttackTargetCooldown | None = Field(default=None, validation_alias='minecraft:attack_target_cooldown', serialization_alias='minecraft:attack_target_cooldown')
    breeze_jump_cooldown: BreezeJumpCooldown | None = Field(default=None, validation_alias='minecraft:breeze_jump_cooldown', serialization_alias='minecraft:breeze_jump_cooldown')
    breeze_jump_inhaling: BreezeJumpInhaling | None = Field(default=None, validation_alias='minecraft:breeze_jump_inhaling', serialization_alias='minecraft:breeze_jump_inhaling')
    breeze_jump_target: BreezeJumpTarget | None = Field(default=None, validation_alias='minecraft:breeze_jump_target', serialization_alias='minecraft:breeze_jump_target')
    breeze_leaving_water: BreezeLeavingWater | None = Field(default=None, validation_alias='minecraft:breeze_leaving_water', serialization_alias='minecraft:breeze_leaving_water')
    breeze_shoot: BreezeShoot | None = Field(default=None, validation_alias='minecraft:breeze_shoot', serialization_alias='minecraft:breeze_shoot')
    breeze_shoot_charging: BreezeShootCharging | None = Field(default=None, validation_alias='minecraft:breeze_shoot_charging', serialization_alias='minecraft:breeze_shoot_charging')
    breeze_shoot_cooldown: BreezeShootCooldown | None = Field(default=None, validation_alias='minecraft:breeze_shoot_cooldown', serialization_alias='minecraft:breeze_shoot_cooldown')
    breeze_shoot_recover: BreezeShootRecover | None = Field(default=None, validation_alias='minecraft:breeze_shoot_recover', serialization_alias='minecraft:breeze_shoot_recover')
    charge_cooldown_ticks: ChargeCooldownTicks | None = Field(default=None, validation_alias='minecraft:charge_cooldown_ticks', serialization_alias='minecraft:charge_cooldown_ticks')
    danger_detected_recently: DangerDetectedRecently | None = Field(default=None, validation_alias='minecraft:danger_detected_recently', serialization_alias='minecraft:danger_detected_recently')
    dig_cooldown: DigCooldown | None = Field(default=None, validation_alias='minecraft:dig_cooldown', serialization_alias='minecraft:dig_cooldown')
    gaze_cooldown_ticks: GazeCooldownTicks | None = Field(default=None, validation_alias='minecraft:gaze_cooldown_ticks', serialization_alias='minecraft:gaze_cooldown_ticks')
    golem_detected_recently: GolemDetectedRecently | None = Field(default=None, validation_alias='minecraft:golem_detected_recently', serialization_alias='minecraft:golem_detected_recently')
    has_hunting_cooldown: HasHuntingCooldown | None = Field(default=None, validation_alias='minecraft:has_hunting_cooldown', serialization_alias='minecraft:has_hunting_cooldown')
    home: Home | None = Field(default=None, validation_alias='minecraft:home', serialization_alias='minecraft:home')
    hunted_recently: HuntedRecently | None = Field(default=None, validation_alias='minecraft:hunted_recently', serialization_alias='minecraft:hunted_recently')
    is_emerging: IsEmerging | None = Field(default=None, validation_alias='minecraft:is_emerging', serialization_alias='minecraft:is_emerging')
    is_in_water: IsInWater | None = Field(default=None, validation_alias='minecraft:is_in_water', serialization_alias='minecraft:is_in_water')
    is_panicking: IsPanicking | None = Field(default=None, validation_alias='minecraft:is_panicking', serialization_alias='minecraft:is_panicking')
    is_pregnant: IsPregnant | None = Field(default=None, validation_alias='minecraft:is_pregnant', serialization_alias='minecraft:is_pregnant')
    is_sniffing: IsSniffing | None = Field(default=None, validation_alias='minecraft:is_sniffing', serialization_alias='minecraft:is_sniffing')
    item_pickup_cooldown_ticks: ItemPickupCooldownTicks | None = Field(default=None, validation_alias='minecraft:item_pickup_cooldown_ticks', serialization_alias='minecraft:item_pickup_cooldown_ticks')
    job_site: JobSite | None = Field(default=None, validation_alias='minecraft:job_site', serialization_alias='minecraft:job_site')
    last_slept: LastSlept | None = Field(default=None, validation_alias='minecraft:last_slept', serialization_alias='minecraft:last_slept')
    last_woken: LastWoken | None = Field(default=None, validation_alias='minecraft:last_woken', serialization_alias='minecraft:last_woken')
    last_worked_at_poi: LastWorkedAtPoi | None = Field(default=None, validation_alias='minecraft:last_worked_at_poi', serialization_alias='minecraft:last_worked_at_poi')
    liked_noteblock: LikedNoteblock | None = Field(default=None, validation_alias='minecraft:liked_noteblock', serialization_alias='minecraft:liked_noteblock')
    liked_noteblock_cooldown_ticks: LikedNoteblockCooldownTicks | None = Field(default=None, validation_alias='minecraft:liked_noteblock_cooldown_ticks', serialization_alias='minecraft:liked_noteblock_cooldown_ticks')
    liked_player: LikedPlayer | None = Field(default=None, validation_alias='minecraft:liked_player', serialization_alias='minecraft:liked_player')
    long_jump_cooling_down: LongJumpCoolingDown | None = Field(default=None, validation_alias='minecraft:long_jump_cooling_down', serialization_alias='minecraft:long_jump_cooling_down')
    meeting_point: MeetingPoint | None = Field(default=None, validation_alias='minecraft:meeting_point', serialization_alias='minecraft:meeting_point')
    play_dead_ticks: PlayDeadTicks | None = Field(default=None, validation_alias='minecraft:play_dead_ticks', serialization_alias='minecraft:play_dead_ticks')
    potential_job_site: PotentialJobSite | None = Field(default=None, validation_alias='minecraft:potential_job_site', serialization_alias='minecraft:potential_job_site')
    ram_cooldown_ticks: RamCooldownTicks | None = Field(default=None, validation_alias='minecraft:ram_cooldown_ticks', serialization_alias='minecraft:ram_cooldown_ticks')
    recent_projectile: RecentProjectile | None = Field(default=None, validation_alias='minecraft:recent_projectile', serialization_alias='minecraft:recent_projectile')
    roar_sound_cooldown: RoarSoundCooldown | None = Field(default=None, validation_alias='minecraft:roar_sound_cooldown', serialization_alias='minecraft:roar_sound_cooldown')
    roar_sound_delay: RoarSoundDelay | None = Field(default=None, validation_alias='minecraft:roar_sound_delay', serialization_alias='minecraft:roar_sound_delay')
    sniff_cooldown: SniffCooldown | None = Field(default=None, validation_alias='minecraft:sniff_cooldown', serialization_alias='minecraft:sniff_cooldown')
    sniffer_explored_positions: SnifferExploredPositions | None = Field(default=None, validation_alias='minecraft:sniffer_explored_positions', serialization_alias='minecraft:sniffer_explored_positions')
    sonic_boom_cooldown: SonicBoomCooldown | None = Field(default=None, validation_alias='minecraft:sonic_boom_cooldown', serialization_alias='minecraft:sonic_boom_cooldown')
    sonic_boom_sound_cooldown: SonicBoomSoundCooldown | None = Field(default=None, validation_alias='minecraft:sonic_boom_sound_cooldown', serialization_alias='minecraft:sonic_boom_sound_cooldown')
    sonic_boom_sound_delay: SonicBoomSoundDelay | None = Field(default=None, validation_alias='minecraft:sonic_boom_sound_delay', serialization_alias='minecraft:sonic_boom_sound_delay')
    temptation_cooldown_ticks: TemptationCooldownTicks | None = Field(default=None, validation_alias='minecraft:temptation_cooldown_ticks', serialization_alias='minecraft:temptation_cooldown_ticks')
    touch_cooldown: TouchCooldown | None = Field(default=None, validation_alias='minecraft:touch_cooldown', serialization_alias='minecraft:touch_cooldown')
    universal_anger: UniversalAnger | None = Field(default=None, validation_alias='minecraft:universal_anger', serialization_alias='minecraft:universal_anger')
    unreachable_transport_block_positions: UnreachableTransportBlockPositions | None = Field(default=None, validation_alias='minecraft:unreachable_transport_block_positions', serialization_alias='minecraft:unreachable_transport_block_positions')
    vibration_cooldown: VibrationCooldown | None = Field(default=None, validation_alias='minecraft:vibration_cooldown', serialization_alias='minecraft:vibration_cooldown')
    visited_block_positions: VisitedBlockPositions | None = Field(default=None, validation_alias='minecraft:visited_block_positions', serialization_alias='minecraft:visited_block_positions')
