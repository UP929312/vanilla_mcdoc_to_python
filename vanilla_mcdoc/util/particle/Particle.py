"""
Generated from symbols.json for ::java::util::particle::Particle
Local link to file: vanilla_mcdoc/util/particle/Particle.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.util.particle.BlockParticle import BlockParticle
from vanilla_mcdoc.util.particle.DragonBreathParticle import DragonBreathParticle
from vanilla_mcdoc.util.particle.DustColorTransitionParticle import DustColorTransitionParticle
from vanilla_mcdoc.util.particle.DustParticle import DustParticle
from vanilla_mcdoc.util.particle.EffectParticle import EffectParticle
from vanilla_mcdoc.util.particle.EntityEffectParticle import EntityEffectParticle
from vanilla_mcdoc.util.particle.FlashParticle import FlashParticle
from vanilla_mcdoc.util.particle.GeyserBaseParticle import GeyserBaseParticle
from vanilla_mcdoc.util.particle.GeyserParticle import GeyserParticle
from vanilla_mcdoc.util.particle.ItemParticle import ItemParticle
from vanilla_mcdoc.util.particle.SculkChargeParticle import SculkChargeParticle
from vanilla_mcdoc.util.particle.ShriekParticle import ShriekParticle
from vanilla_mcdoc.util.particle.TintedLeavesParticle import TintedLeavesParticle
from vanilla_mcdoc.util.particle.TrailParticle import TrailParticle
from vanilla_mcdoc.util.particle.VibrationParticle import VibrationParticle


class ParticleDefault(GeneratedModel):
    type: Annotated[str, IdSpec(registry='particle_type')]


class ParticleBlock(BlockParticle):
    type: Literal['minecraft:block', 'block'] = 'minecraft:block'


class ParticleBlockCrumble(BlockParticle):
    type: Literal['minecraft:block_crumble', 'block_crumble'] = 'minecraft:block_crumble'


class ParticleBlockMarker(BlockParticle):
    type: Literal['minecraft:block_marker', 'block_marker'] = 'minecraft:block_marker'


class ParticleDragonBreath(DragonBreathParticle):
    type: Literal['minecraft:dragon_breath', 'dragon_breath'] = 'minecraft:dragon_breath'


class ParticleDust(DustParticle):
    type: Literal['minecraft:dust', 'dust'] = 'minecraft:dust'


class ParticleDustColorTransition(DustColorTransitionParticle):
    type: Literal['minecraft:dust_color_transition', 'dust_color_transition'] = 'minecraft:dust_color_transition'


class ParticleDustPillar(BlockParticle):
    type: Literal['minecraft:dust_pillar', 'dust_pillar'] = 'minecraft:dust_pillar'


class ParticleEffect(EffectParticle):
    type: Literal['minecraft:effect', 'effect'] = 'minecraft:effect'


class ParticleEntityEffect(EntityEffectParticle):
    type: Literal['minecraft:entity_effect', 'entity_effect'] = 'minecraft:entity_effect'


class ParticleFallingDust(BlockParticle):
    type: Literal['minecraft:falling_dust', 'falling_dust'] = 'minecraft:falling_dust'


class ParticleFlash(FlashParticle):
    type: Literal['minecraft:flash', 'flash'] = 'minecraft:flash'


class ParticleGeyser(GeyserParticle):
    type: Literal['minecraft:geyser', 'geyser'] = 'minecraft:geyser'


class ParticleGeyserBase(GeyserBaseParticle):
    type: Literal['minecraft:geyser_base', 'geyser_base'] = 'minecraft:geyser_base'


class ParticleGeyserPlume(GeyserParticle):
    type: Literal['minecraft:geyser_plume', 'geyser_plume'] = 'minecraft:geyser_plume'


class ParticleGeyserPoof(GeyserBaseParticle):
    type: Literal['minecraft:geyser_poof', 'geyser_poof'] = 'minecraft:geyser_poof'


class ParticleInstantEffect(EffectParticle):
    type: Literal['minecraft:instant_effect', 'instant_effect'] = 'minecraft:instant_effect'


class ParticleItem(ItemParticle):
    type: Literal['minecraft:item', 'item'] = 'minecraft:item'


class ParticleSculkCharge(SculkChargeParticle):
    type: Literal['minecraft:sculk_charge', 'sculk_charge'] = 'minecraft:sculk_charge'


class ParticleShriek(ShriekParticle):
    type: Literal['minecraft:shriek', 'shriek'] = 'minecraft:shriek'


class ParticleTintedLeaves(TintedLeavesParticle):
    type: Literal['minecraft:tinted_leaves', 'tinted_leaves'] = 'minecraft:tinted_leaves'


class ParticleTrail(TrailParticle):
    type: Literal['minecraft:trail', 'trail'] = 'minecraft:trail'


class ParticleVibration(VibrationParticle):
    type: Literal['minecraft:vibration', 'vibration'] = 'minecraft:vibration'


class ParticleAngryVillager(GeneratedModel):
    type: Literal['minecraft:angry_villager', 'angry_villager'] = 'minecraft:angry_villager'


class ParticleAsh(GeneratedModel):
    type: Literal['minecraft:ash', 'ash'] = 'minecraft:ash'


class ParticleBubble(GeneratedModel):
    type: Literal['minecraft:bubble', 'bubble'] = 'minecraft:bubble'


class ParticleBubbleColumnUp(GeneratedModel):
    type: Literal['minecraft:bubble_column_up', 'bubble_column_up'] = 'minecraft:bubble_column_up'


class ParticleBubblePop(GeneratedModel):
    type: Literal['minecraft:bubble_pop', 'bubble_pop'] = 'minecraft:bubble_pop'


class ParticleCampfireCosySmoke(GeneratedModel):
    type: Literal['minecraft:campfire_cosy_smoke', 'campfire_cosy_smoke'] = 'minecraft:campfire_cosy_smoke'


class ParticleCampfireSignalSmoke(GeneratedModel):
    type: Literal['minecraft:campfire_signal_smoke', 'campfire_signal_smoke'] = 'minecraft:campfire_signal_smoke'


class ParticleCherryLeaves(GeneratedModel):
    type: Literal['minecraft:cherry_leaves', 'cherry_leaves'] = 'minecraft:cherry_leaves'


class ParticleCloud(GeneratedModel):
    type: Literal['minecraft:cloud', 'cloud'] = 'minecraft:cloud'


class ParticleComposter(GeneratedModel):
    type: Literal['minecraft:composter', 'composter'] = 'minecraft:composter'


class ParticleCopperFireFlame(GeneratedModel):
    type: Literal['minecraft:copper_fire_flame', 'copper_fire_flame'] = 'minecraft:copper_fire_flame'


class ParticleCrimsonSpore(GeneratedModel):
    type: Literal['minecraft:crimson_spore', 'crimson_spore'] = 'minecraft:crimson_spore'


class ParticleCrit(GeneratedModel):
    type: Literal['minecraft:crit', 'crit'] = 'minecraft:crit'


class ParticleCurrentDown(GeneratedModel):
    type: Literal['minecraft:current_down', 'current_down'] = 'minecraft:current_down'


class ParticleDamageIndicator(GeneratedModel):
    type: Literal['minecraft:damage_indicator', 'damage_indicator'] = 'minecraft:damage_indicator'


class ParticleDolphin(GeneratedModel):
    type: Literal['minecraft:dolphin', 'dolphin'] = 'minecraft:dolphin'


class ParticleDrippingDripstoneLava(GeneratedModel):
    type: Literal['minecraft:dripping_dripstone_lava', 'dripping_dripstone_lava'] = 'minecraft:dripping_dripstone_lava'


class ParticleDrippingDripstoneWater(GeneratedModel):
    type: Literal['minecraft:dripping_dripstone_water', 'dripping_dripstone_water'] = 'minecraft:dripping_dripstone_water'


class ParticleDrippingHoney(GeneratedModel):
    type: Literal['minecraft:dripping_honey', 'dripping_honey'] = 'minecraft:dripping_honey'


class ParticleDrippingLava(GeneratedModel):
    type: Literal['minecraft:dripping_lava', 'dripping_lava'] = 'minecraft:dripping_lava'


class ParticleDrippingObsidianTear(GeneratedModel):
    type: Literal['minecraft:dripping_obsidian_tear', 'dripping_obsidian_tear'] = 'minecraft:dripping_obsidian_tear'


class ParticleDrippingWater(GeneratedModel):
    type: Literal['minecraft:dripping_water', 'dripping_water'] = 'minecraft:dripping_water'


class ParticleDustPlume(GeneratedModel):
    type: Literal['minecraft:dust_plume', 'dust_plume'] = 'minecraft:dust_plume'


class ParticleEggCrack(GeneratedModel):
    type: Literal['minecraft:egg_crack', 'egg_crack'] = 'minecraft:egg_crack'


class ParticleElderGuardian(GeneratedModel):
    type: Literal['minecraft:elder_guardian', 'elder_guardian'] = 'minecraft:elder_guardian'


class ParticleElectricSpark(GeneratedModel):
    type: Literal['minecraft:electric_spark', 'electric_spark'] = 'minecraft:electric_spark'


class ParticleEnchant(GeneratedModel):
    type: Literal['minecraft:enchant', 'enchant'] = 'minecraft:enchant'


class ParticleEnchantedHit(GeneratedModel):
    type: Literal['minecraft:enchanted_hit', 'enchanted_hit'] = 'minecraft:enchanted_hit'


class ParticleEndRod(GeneratedModel):
    type: Literal['minecraft:end_rod', 'end_rod'] = 'minecraft:end_rod'


class ParticleExplosion(GeneratedModel):
    type: Literal['minecraft:explosion', 'explosion'] = 'minecraft:explosion'


class ParticleExplosionEmitter(GeneratedModel):
    type: Literal['minecraft:explosion_emitter', 'explosion_emitter'] = 'minecraft:explosion_emitter'


class ParticleFallingDripstoneLava(GeneratedModel):
    type: Literal['minecraft:falling_dripstone_lava', 'falling_dripstone_lava'] = 'minecraft:falling_dripstone_lava'


class ParticleFallingDripstoneWater(GeneratedModel):
    type: Literal['minecraft:falling_dripstone_water', 'falling_dripstone_water'] = 'minecraft:falling_dripstone_water'


class ParticleFallingHoney(GeneratedModel):
    type: Literal['minecraft:falling_honey', 'falling_honey'] = 'minecraft:falling_honey'


class ParticleFallingLava(GeneratedModel):
    type: Literal['minecraft:falling_lava', 'falling_lava'] = 'minecraft:falling_lava'


class ParticleFallingNectar(GeneratedModel):
    type: Literal['minecraft:falling_nectar', 'falling_nectar'] = 'minecraft:falling_nectar'


class ParticleFallingObsidianTear(GeneratedModel):
    type: Literal['minecraft:falling_obsidian_tear', 'falling_obsidian_tear'] = 'minecraft:falling_obsidian_tear'


class ParticleFallingSporeBlossom(GeneratedModel):
    type: Literal['minecraft:falling_spore_blossom', 'falling_spore_blossom'] = 'minecraft:falling_spore_blossom'


class ParticleFallingWater(GeneratedModel):
    type: Literal['minecraft:falling_water', 'falling_water'] = 'minecraft:falling_water'


class ParticleFirefly(GeneratedModel):
    type: Literal['minecraft:firefly', 'firefly'] = 'minecraft:firefly'


class ParticleFirework(GeneratedModel):
    type: Literal['minecraft:firework', 'firework'] = 'minecraft:firework'


class ParticleFishing(GeneratedModel):
    type: Literal['minecraft:fishing', 'fishing'] = 'minecraft:fishing'


class ParticleFlame(GeneratedModel):
    type: Literal['minecraft:flame', 'flame'] = 'minecraft:flame'


class ParticleFreezing(GeneratedModel):
    type: Literal['minecraft:freezing', 'freezing'] = 'minecraft:freezing'


class ParticleGlow(GeneratedModel):
    type: Literal['minecraft:glow', 'glow'] = 'minecraft:glow'


class ParticleGlowSquidInk(GeneratedModel):
    type: Literal['minecraft:glow_squid_ink', 'glow_squid_ink'] = 'minecraft:glow_squid_ink'


class ParticleGust(GeneratedModel):
    type: Literal['minecraft:gust', 'gust'] = 'minecraft:gust'


class ParticleGustEmitterLarge(GeneratedModel):
    type: Literal['minecraft:gust_emitter_large', 'gust_emitter_large'] = 'minecraft:gust_emitter_large'


class ParticleGustEmitterSmall(GeneratedModel):
    type: Literal['minecraft:gust_emitter_small', 'gust_emitter_small'] = 'minecraft:gust_emitter_small'


class ParticleHappyVillager(GeneratedModel):
    type: Literal['minecraft:happy_villager', 'happy_villager'] = 'minecraft:happy_villager'


class ParticleHeart(GeneratedModel):
    type: Literal['minecraft:heart', 'heart'] = 'minecraft:heart'


class ParticleInfested(GeneratedModel):
    type: Literal['minecraft:infested', 'infested'] = 'minecraft:infested'


class ParticleItemCobweb(GeneratedModel):
    type: Literal['minecraft:item_cobweb', 'item_cobweb'] = 'minecraft:item_cobweb'


class ParticleItemSlime(GeneratedModel):
    type: Literal['minecraft:item_slime', 'item_slime'] = 'minecraft:item_slime'


class ParticleLandingHoney(GeneratedModel):
    type: Literal['minecraft:landing_honey', 'landing_honey'] = 'minecraft:landing_honey'


class ParticleLandingLava(GeneratedModel):
    type: Literal['minecraft:landing_lava', 'landing_lava'] = 'minecraft:landing_lava'


class ParticleLandingObsidianTear(GeneratedModel):
    type: Literal['minecraft:landing_obsidian_tear', 'landing_obsidian_tear'] = 'minecraft:landing_obsidian_tear'


class ParticleLargeSmoke(GeneratedModel):
    type: Literal['minecraft:large_smoke', 'large_smoke'] = 'minecraft:large_smoke'


class ParticleLava(GeneratedModel):
    type: Literal['minecraft:lava', 'lava'] = 'minecraft:lava'


class ParticleMycelium(GeneratedModel):
    type: Literal['minecraft:mycelium', 'mycelium'] = 'minecraft:mycelium'


class ParticleNautilus(GeneratedModel):
    type: Literal['minecraft:nautilus', 'nautilus'] = 'minecraft:nautilus'


class ParticleNote(GeneratedModel):
    type: Literal['minecraft:note', 'note'] = 'minecraft:note'


class ParticleNoxiousGas(GeneratedModel):
    type: Literal['minecraft:noxious_gas', 'noxious_gas'] = 'minecraft:noxious_gas'


class ParticleNoxiousGasCloud(GeneratedModel):
    type: Literal['minecraft:noxious_gas_cloud', 'noxious_gas_cloud'] = 'minecraft:noxious_gas_cloud'


class ParticleOminousSpawning(GeneratedModel):
    type: Literal['minecraft:ominous_spawning', 'ominous_spawning'] = 'minecraft:ominous_spawning'


class ParticleOrangePoplarLeaves(GeneratedModel):
    type: Literal['minecraft:orange_poplar_leaves', 'orange_poplar_leaves'] = 'minecraft:orange_poplar_leaves'


class ParticlePaleOakLeaves(GeneratedModel):
    type: Literal['minecraft:pale_oak_leaves', 'pale_oak_leaves'] = 'minecraft:pale_oak_leaves'


class ParticlePauseMobGrowth(GeneratedModel):
    type: Literal['minecraft:pause_mob_growth', 'pause_mob_growth'] = 'minecraft:pause_mob_growth'


class ParticlePoof(GeneratedModel):
    type: Literal['minecraft:poof', 'poof'] = 'minecraft:poof'


class ParticlePortal(GeneratedModel):
    type: Literal['minecraft:portal', 'portal'] = 'minecraft:portal'


class ParticleRaidOmen(GeneratedModel):
    type: Literal['minecraft:raid_omen', 'raid_omen'] = 'minecraft:raid_omen'


class ParticleRain(GeneratedModel):
    type: Literal['minecraft:rain', 'rain'] = 'minecraft:rain'


class ParticleRedPoplarLeaves(GeneratedModel):
    type: Literal['minecraft:red_poplar_leaves', 'red_poplar_leaves'] = 'minecraft:red_poplar_leaves'


class ParticleResetMobGrowth(GeneratedModel):
    type: Literal['minecraft:reset_mob_growth', 'reset_mob_growth'] = 'minecraft:reset_mob_growth'


class ParticleReversePortal(GeneratedModel):
    type: Literal['minecraft:reverse_portal', 'reverse_portal'] = 'minecraft:reverse_portal'


class ParticleScrape(GeneratedModel):
    type: Literal['minecraft:scrape', 'scrape'] = 'minecraft:scrape'


class ParticleSculkChargePop(GeneratedModel):
    type: Literal['minecraft:sculk_charge_pop', 'sculk_charge_pop'] = 'minecraft:sculk_charge_pop'


class ParticleSculkSoul(GeneratedModel):
    type: Literal['minecraft:sculk_soul', 'sculk_soul'] = 'minecraft:sculk_soul'


class ParticleSmallFlame(GeneratedModel):
    type: Literal['minecraft:small_flame', 'small_flame'] = 'minecraft:small_flame'


class ParticleSmallGust(GeneratedModel):
    type: Literal['minecraft:small_gust', 'small_gust'] = 'minecraft:small_gust'


class ParticleSmoke(GeneratedModel):
    type: Literal['minecraft:smoke', 'smoke'] = 'minecraft:smoke'


class ParticleSneeze(GeneratedModel):
    type: Literal['minecraft:sneeze', 'sneeze'] = 'minecraft:sneeze'


class ParticleSnowflake(GeneratedModel):
    type: Literal['minecraft:snowflake', 'snowflake'] = 'minecraft:snowflake'


class ParticleSonicBoom(GeneratedModel):
    type: Literal['minecraft:sonic_boom', 'sonic_boom'] = 'minecraft:sonic_boom'


class ParticleSoul(GeneratedModel):
    type: Literal['minecraft:soul', 'soul'] = 'minecraft:soul'


class ParticleSoulFireFlame(GeneratedModel):
    type: Literal['minecraft:soul_fire_flame', 'soul_fire_flame'] = 'minecraft:soul_fire_flame'


class ParticleSpit(GeneratedModel):
    type: Literal['minecraft:spit', 'spit'] = 'minecraft:spit'


class ParticleSplash(GeneratedModel):
    type: Literal['minecraft:splash', 'splash'] = 'minecraft:splash'


class ParticleSporeBlossomAir(GeneratedModel):
    type: Literal['minecraft:spore_blossom_air', 'spore_blossom_air'] = 'minecraft:spore_blossom_air'


class ParticleSquidInk(GeneratedModel):
    type: Literal['minecraft:squid_ink', 'squid_ink'] = 'minecraft:squid_ink'


class ParticleSulfurBubbles(GeneratedModel):
    type: Literal['minecraft:sulfur_bubbles', 'sulfur_bubbles'] = 'minecraft:sulfur_bubbles'


class ParticleSulfurCubeGoo(GeneratedModel):
    type: Literal['minecraft:sulfur_cube_goo', 'sulfur_cube_goo'] = 'minecraft:sulfur_cube_goo'


class ParticleSweepAttack(GeneratedModel):
    type: Literal['minecraft:sweep_attack', 'sweep_attack'] = 'minecraft:sweep_attack'


class ParticleTotemOfUndying(GeneratedModel):
    type: Literal['minecraft:totem_of_undying', 'totem_of_undying'] = 'minecraft:totem_of_undying'


class ParticleTrialOmen(GeneratedModel):
    type: Literal['minecraft:trial_omen', 'trial_omen'] = 'minecraft:trial_omen'


class ParticleTrialSpawnerDetection(GeneratedModel):
    type: Literal['minecraft:trial_spawner_detection', 'trial_spawner_detection'] = 'minecraft:trial_spawner_detection'


class ParticleTrialSpawnerDetectionOminous(GeneratedModel):
    type: Literal['minecraft:trial_spawner_detection_ominous', 'trial_spawner_detection_ominous'] = 'minecraft:trial_spawner_detection_ominous'


class ParticleUnderwater(GeneratedModel):
    type: Literal['minecraft:underwater', 'underwater'] = 'minecraft:underwater'


class ParticleVaultConnection(GeneratedModel):
    type: Literal['minecraft:vault_connection', 'vault_connection'] = 'minecraft:vault_connection'


class ParticleWarpedSpore(GeneratedModel):
    type: Literal['minecraft:warped_spore', 'warped_spore'] = 'minecraft:warped_spore'


class ParticleWaxOff(GeneratedModel):
    type: Literal['minecraft:wax_off', 'wax_off'] = 'minecraft:wax_off'


class ParticleWaxOn(GeneratedModel):
    type: Literal['minecraft:wax_on', 'wax_on'] = 'minecraft:wax_on'


class ParticleWhiteAsh(GeneratedModel):
    type: Literal['minecraft:white_ash', 'white_ash'] = 'minecraft:white_ash'


class ParticleWhiteSmoke(GeneratedModel):
    type: Literal['minecraft:white_smoke', 'white_smoke'] = 'minecraft:white_smoke'


class ParticleWitch(GeneratedModel):
    type: Literal['minecraft:witch', 'witch'] = 'minecraft:witch'


class ParticleYellowPoplarLeaves(GeneratedModel):
    type: Literal['minecraft:yellow_poplar_leaves', 'yellow_poplar_leaves'] = 'minecraft:yellow_poplar_leaves'


type Particle = ParticleDefault | ParticleBlock | ParticleBlockCrumble | ParticleBlockMarker | ParticleDragonBreath | ParticleDust | ParticleDustColorTransition | ParticleDustPillar | ParticleEffect | ParticleEntityEffect | ParticleFallingDust | ParticleFlash | ParticleGeyser | ParticleGeyserBase | ParticleGeyserPlume | ParticleGeyserPoof | ParticleInstantEffect | ParticleItem | ParticleSculkCharge | ParticleShriek | ParticleTintedLeaves | ParticleTrail | ParticleVibration | ParticleAngryVillager | ParticleAsh | ParticleBubble | ParticleBubbleColumnUp | ParticleBubblePop | ParticleCampfireCosySmoke | ParticleCampfireSignalSmoke | ParticleCherryLeaves | ParticleCloud | ParticleComposter | ParticleCopperFireFlame | ParticleCrimsonSpore | ParticleCrit | ParticleCurrentDown | ParticleDamageIndicator | ParticleDolphin | ParticleDrippingDripstoneLava | ParticleDrippingDripstoneWater | ParticleDrippingHoney | ParticleDrippingLava | ParticleDrippingObsidianTear | ParticleDrippingWater | ParticleDustPlume | ParticleEggCrack | ParticleElderGuardian | ParticleElectricSpark | ParticleEnchant | ParticleEnchantedHit | ParticleEndRod | ParticleExplosion | ParticleExplosionEmitter | ParticleFallingDripstoneLava | ParticleFallingDripstoneWater | ParticleFallingHoney | ParticleFallingLava | ParticleFallingNectar | ParticleFallingObsidianTear | ParticleFallingSporeBlossom | ParticleFallingWater | ParticleFirefly | ParticleFirework | ParticleFishing | ParticleFlame | ParticleFreezing | ParticleGlow | ParticleGlowSquidInk | ParticleGust | ParticleGustEmitterLarge | ParticleGustEmitterSmall | ParticleHappyVillager | ParticleHeart | ParticleInfested | ParticleItemCobweb | ParticleItemSlime | ParticleLandingHoney | ParticleLandingLava | ParticleLandingObsidianTear | ParticleLargeSmoke | ParticleLava | ParticleMycelium | ParticleNautilus | ParticleNote | ParticleNoxiousGas | ParticleNoxiousGasCloud | ParticleOminousSpawning | ParticleOrangePoplarLeaves | ParticlePaleOakLeaves | ParticlePauseMobGrowth | ParticlePoof | ParticlePortal | ParticleRaidOmen | ParticleRain | ParticleRedPoplarLeaves | ParticleResetMobGrowth | ParticleReversePortal | ParticleScrape | ParticleSculkChargePop | ParticleSculkSoul | ParticleSmallFlame | ParticleSmallGust | ParticleSmoke | ParticleSneeze | ParticleSnowflake | ParticleSonicBoom | ParticleSoul | ParticleSoulFireFlame | ParticleSpit | ParticleSplash | ParticleSporeBlossomAir | ParticleSquidInk | ParticleSulfurBubbles | ParticleSulfurCubeGoo | ParticleSweepAttack | ParticleTotemOfUndying | ParticleTrialOmen | ParticleTrialSpawnerDetection | ParticleTrialSpawnerDetectionOminous | ParticleUnderwater | ParticleVaultConnection | ParticleWarpedSpore | ParticleWaxOff | ParticleWaxOn | ParticleWhiteAsh | ParticleWhiteSmoke | ParticleWitch | ParticleYellowPoplarLeaves
