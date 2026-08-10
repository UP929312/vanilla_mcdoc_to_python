"""
Generated from symbols.json for ::java::world::block::BlockEntityData
Local link to file: generated_symbols/world/block/BlockEntityData.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.world.block.BlockEntity import BlockEntity
from generated_symbols.world.block.Lockable import Lockable
from generated_symbols.world.block.Nameable import Nameable
from generated_symbols.world.block.command_block.BaseCommandBlock import BaseCommandBlock
from generated_symbols.world.block.container.Container9 import Container9
from generated_symbols.world.block.container.ContainerBase import ContainerBase
from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.trial_spawner.TrialSpawnerConfig import TrialSpawnerConfig
    from generated_symbols.util.Rotation import Rotation
    from generated_symbols.util.avatar.Profile import Profile
    from generated_symbols.util.block_state.BlockState import BlockState
    from generated_symbols.util.direction.DirectionByte import DirectionByte
    from generated_symbols.util.game_event.VibrationListener import VibrationListener
    from generated_symbols.util.slot.SlottedItem import SlottedItem
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.block.banner.BannerPatternLayer import BannerPatternLayer
    from generated_symbols.world.block.beehive.Bee import Bee
    from generated_symbols.world.block.jigsaw.JointType import JointType
    from generated_symbols.world.block.sculk_catalyst.ChargeCursor import ChargeCursor
    from generated_symbols.world.block.spawner.SpawnPotential import SpawnPotential
    from generated_symbols.world.block.spawner.SpawnerEntry import SpawnerEntry
    from generated_symbols.world.block.structure_block.Mirror import Mirror
    from generated_symbols.world.block.structure_block.Mode import Mode
    from generated_symbols.world.block.structure_block.Rotation import Rotation
    from generated_symbols.world.block.test_block.TestBlockMode import TestBlockMode
    from generated_symbols.world.block.test_instance_block.TestInstanceBlockStatus import TestInstanceBlockStatus
    from generated_symbols.world.component.block.PotDecorations import PotDecorations
    from generated_symbols.world.item.ItemStack import ItemStack


@dataclass(kw_only=True)
class DataStruct:
    size: tuple[int, int, int]
    rotation: Rotation
    ignore_entities: bool
    status: TestInstanceBlockStatus
    test: Annotated[str, IdSpec(registry='test_instance')] | None = None
    error_message: Text | None = None


@dataclass(kw_only=True)
class ErrorsStruct:
    pos: tuple[int, int, int]
    text: Text


@dataclass(kw_only=True)
class ServerDataStruct:
    state_updating_resumes_at: int | None = None  # Ticks until the loot table is ran again to update the display item.
    rewarded_players: list[tuple[int, int, int, int]] | None = None  # When a player is in this list they can no longer open the vault, but other players can.
    items_to_eject: list[ItemStack] | None = None  # Items that are being ejected from the vault when it is opened. As each item is ejected, it is removed from this list, before ejection, it is previewed as the `display_item`.
    total_ejections_needed: int | None = None  # Number of items that the loot table started off the opening with, does not change while items are ejected.


@dataclass(kw_only=True)
class ConfigStruct:
    key_item: ItemStack | None = None  # Item required to open the vault.
    loot_table: Annotated[str, IdSpec(registry='loot_table')] | None = None  # Defaults to "minecraft:chests/trial_chambers/reward".
    override_loot_table_to_display: Annotated[str, IdSpec(registry='loot_table')] | None = None  # The loot table to display items in the vault. Defaults to use the value in `loot_table` field.
    activation_range: float | None = None  # The range when the vault should activate.
    deactivation_range: float | None = None  # The range when the vault should deactivate.


@dataclass(kw_only=True)
class SharedDataStruct:
    display_item: ItemStack | None = None  # Item that is displayed to players when they are in range of the vault.
    connected_players: list[tuple[int, int, int, int]] | None = None
    connected_particles_range: float | None = None


@dataclass(kw_only=True)
class BlockEntityDataBanner(BlockEntity, Nameable):
    id: Literal['minecraft:banner']
    patterns: list[BannerPatternLayer] | None = None


@dataclass(kw_only=True)
class BlockEntityDataBarrel(ContainerBase):
    id: Literal['minecraft:barrel']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class BlockEntityDataBeacon(BlockEntity, Nameable, Lockable):
    id: Literal['minecraft:beacon']
    Levels: int | None = None  # Number of levels from the pyramid.
    primary_effect: Annotated[str, IdSpec(registry='mob_effect')] | None = None
    secondary_effect: Annotated[str, IdSpec(registry='mob_effect')] | None = None


@dataclass(kw_only=True)
class BlockEntityDataBeehive(BlockEntity):
    id: Literal['minecraft:beehive']
    flower_pos: tuple[int, int, int] | None = None
    bees: list[Bee] | None = None


@dataclass(kw_only=True)
class BlockEntityDataBlastFurnace(BlockEntity, Nameable, Lockable):
    id: Literal['minecraft:blast_furnace']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`2` | both inclusive']]], 'Length = 0-3 (both inclusive)'] | None = None  # The items in this furnace, with slots: * 0: Item being smelted * 1: Fuel * 2: Output
    cooking_total_time: int | None = None  # The total amount of time the current cooking process will take. Defaults to `0`.
    cooking_time_spent: int | None = None  # The amount of time that the current cooking process has taken so far. Defaults to `0`.
    lit_time_remaining: int | None = None  # The amount of burn time remaining. Defaults to `0`.
    lit_total_time: int | None = None  # The total amount of burn time that was added in the last refuel. Defaults to `0`.
    speed_multiplier: float | None = None  # Used to speed up or slow down the next cooking process. Defaults to `1`.
    RecipesUsed: dict[Annotated[str, IdSpec(registry='recipe')], int] | None = None  # Recipes that have been used since the last time a result item was removed from the GUI. Used to calculate the experience to give to the player.


@dataclass(kw_only=True)
class BlockEntityDataBrewingStand(BlockEntity, Nameable, Lockable):
    id: Literal['minecraft:brewing_stand']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`4` | both inclusive']]], 'Length = 0-5 (both inclusive)'] | None = None  # * 0: left brewing slot * 1: middle brewing slot * 2: right brewing slot * 3: ingredient slot * 4: fuel slot
    BrewTime: int | None = None  # Number of ticks until the brewing is complete.
    Fuel: int | None = None  # Amount of fuel the brewing stand has left.
    total_brew_time: int | None = None  # The total amount of time the current brewing process will take. Defaults to `400`.
    total_fuel: int | None = None  # The amount of fuel that was added in the last refuel. Defaults to `20`.
    speed_multiplier: float | None = None  # Used to speed up or slow down the next brewing process. Defaults to `1`.


@dataclass(kw_only=True)
class BlockEntityDataBrushableBlock(BlockEntity):
    id: Literal['minecraft:brushable_block']
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will decide the brushed loot.
    LootTableSeed: int | None = None  # Seed of the loot table.
    item: ItemStack | None = None  # Item that was rolled from the loot table, which is currently peeking out.
    hit_direction: DirectionByte | None = None  # Direction of the block that was interacted with. Write-only, is not saved by the game.


@dataclass(kw_only=True)
class BlockEntityDataCalibratedSculkSensor:
    id: Literal['minecraft:calibrated_sculk_sensor']
    last_vibration_frequency: Annotated[int, 'Range | `1`-`15` | both inclusive'] | None = None
    listener: VibrationListener | None = None  # Vibration listener


@dataclass(kw_only=True)
class BlockEntityDataCampfire(BlockEntity):
    id: Literal['minecraft:campfire']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`3` | both inclusive']]], 'Length = 0-4 (both inclusive)'] | None = None
    CookingTimes: tuple[int, int, int, int] | None = None  # Ticks each item has been cooking. Index is according to item slot.
    CookingTotalTimes: tuple[int, int, int, int] | None = None  # Ticks each item still has to cook. Index is according to item slot.


@dataclass(kw_only=True)
class BlockEntityDataChest(ContainerBase):
    id: Literal['minecraft:chest']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class BlockEntityDataChiseledBookshelf(BlockEntity):
    id: Literal['minecraft:chiseled_bookshelf']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`5` | both inclusive']]], 'Length = 0-6 (both inclusive)'] | None = None  # Slots from 0 to 5.
    last_interacted_slot: Annotated[int, 'Range | `0`-`5` | both inclusive'] | None = None


@dataclass(kw_only=True)
class BlockEntityDataCommandBlock(BlockEntity, Nameable, BaseCommandBlock):
    id: Literal['minecraft:command_block']
    powered: bool | None = None  # Whether it is powered by redstone.
    auto: bool | None = None  # Whether it is automatically powered.
    conditionMet: bool | None = None  # Whether the previous command block was successful when the command block was executed. This is always true for non-conditional command blocks.


@dataclass(kw_only=True)
class BlockEntityDataComparator(BlockEntity):
    id: Literal['minecraft:comparator']
    OutputSignal: int | None = None  # Strength of the redstone output.


@dataclass(kw_only=True)
class BlockEntityDataConduit(BlockEntity):
    id: Literal['minecraft:conduit']
    Target: tuple[int, int, int, int] | None = None  # The hostile mob that the conduit is currently attacking.


@dataclass(kw_only=True)
class BlockEntityDataCrafter(Container9):
    id: Literal['minecraft:crafter']
    crafting_ticks_remaining: int | None = None
    disabled_slots: Annotated[list[Annotated[int, 'Range | `0`-`8` | both inclusive']], 'Length = up to 9 (inclusive)'] | None = None
    triggered: Literal[0] | Literal[1] | None = None


@dataclass(kw_only=True)
class BlockEntityDataCreakingHeart(BlockEntity):
    id: Literal['minecraft:creaking_heart']
    creaking: tuple[int, int, int, int] | None = None  # The creaking mob that is linked to this heart.


@dataclass(kw_only=True)
class BlockEntityDataDecoratedPot(BlockEntity):
    id: Literal['minecraft:decorated_pot']
    sherds: PotDecorations | None = None  # Item ID of what was used for each side of the pot.  Decoration textures are determined by `provides_pottery_pattern` component on the sherd items.
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will populate this container.
    LootTableSeed: int | None = None  # Seed of the loot table.
    item: ItemStack | None = None


@dataclass(kw_only=True)
class BlockEntityDataDispenser(ContainerBase):
    id: Literal['minecraft:dispenser']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`8` | both inclusive']]], 'Length = 0-9 (both inclusive)'] | None = None  # Slots from 0 to 8.


@dataclass(kw_only=True)
class BlockEntityDataDropper(ContainerBase):
    id: Literal['minecraft:dropper']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`8` | both inclusive']]], 'Length = 0-9 (both inclusive)'] | None = None  # Slots from 0 to 8.


@dataclass(kw_only=True)
class BlockEntityDataEnchantingTable(BlockEntity, Nameable):
    id: Literal['minecraft:enchanting_table']


@dataclass(kw_only=True)
class BlockEntityDataEndGateway(BlockEntity):
    id: Literal['minecraft:end_gateway']
    Age: int | None = None  # In game ticks.
    ExactTeleport: bool | None = None  # Whether to teleport to the exact location.
    exit_portal: tuple[int, int, int] | None = None  # Coordinates of where to teleport entities to.


@dataclass(kw_only=True)
class BlockEntityDataFurnace(BlockEntity, Nameable, Lockable):
    id: Literal['minecraft:furnace']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`2` | both inclusive']]], 'Length = 0-3 (both inclusive)'] | None = None  # The items in this furnace, with slots: * 0: Item being smelted * 1: Fuel * 2: Output
    cooking_total_time: int | None = None  # The total amount of time the current cooking process will take. Defaults to `0`.
    cooking_time_spent: int | None = None  # The amount of time that the current cooking process has taken so far. Defaults to `0`.
    lit_time_remaining: int | None = None  # The amount of burn time remaining. Defaults to `0`.
    lit_total_time: int | None = None  # The total amount of burn time that was added in the last refuel. Defaults to `0`.
    speed_multiplier: float | None = None  # Used to speed up or slow down the next cooking process. Defaults to `1`.
    RecipesUsed: dict[Annotated[str, IdSpec(registry='recipe')], int] | None = None  # Recipes that have been used since the last time a result item was removed from the GUI. Used to calculate the experience to give to the player.


@dataclass(kw_only=True)
class BlockEntityDataHangingSign:
    id: Literal['minecraft:hanging_sign']


@dataclass(kw_only=True)
class BlockEntityDataHopper(ContainerBase):
    id: Literal['minecraft:hopper']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`4` | both inclusive']]], 'Length = 0-5 (both inclusive)'] | None = None  # Slots from 0 to 4.
    TransferCooldown: int | None = None  # Ticks until an item can be transferred.


@dataclass(kw_only=True)
class BlockEntityDataJigsaw:
    id: Literal['minecraft:jigsaw']
    joint: JointType | None = None  # How the resultant structure can be transformed.
    pool: Annotated[str, IdSpec(registry='worldgen/template_pool')] | None = None  # Structure pool this will "spawn" in.
    name: str | None = None  # ID this will "spawn" in.
    target: str | None = None  # ID of the type of jigsaw this will be "spawned" from.
    final_state: str | None = None  # Final block state of the jigsaw.


@dataclass(kw_only=True)
class BlockEntityDataJukebox(BlockEntity):
    id: Literal['minecraft:jukebox']
    RecordItem: ItemStack | None = None
    ticks_since_song_started: int | None = None


@dataclass(kw_only=True)
class BlockEntityDataLectern(BlockEntity):
    id: Literal['minecraft:lectern']
    Book: ItemStack | None = None
    Page: int | None = None  # Current page the book is on.


@dataclass(kw_only=True)
class BlockEntityDataMobSpawner(BlockEntity):
    id: Literal['minecraft:mob_spawner']
    SpawnPotentials: list[SpawnPotential] | None = None  # Entities that can be placed.
    SpawnData: SpawnerEntry | None = None  # Data for the next mob to spawn. Overwritten by `SpawnPotentials`.
    SpawnCount: int | None = None  # Number of entities that will be placed.
    SpawnRange: int | None = None  # Range that the spawned entities will be placed.
    Delay: int | None = None  # Ticks until the next spawn.
    MinSpawnDelay: int | None = None  # Minimum random delay for the next spawn.
    MaxSpawnDelay: int | None = None  # Maximum random delay for the next spawn.
    MaxNearbyEntities: int | None = None  # Maximum number of entities nearby.
    RequiredPlayerRange: int | None = None  # Radius in blocks that a player has to be within to spawn entities.


@dataclass(kw_only=True)
class BlockEntityDataMovingPiston(BlockEntity):
    id: Literal['minecraft:moving_piston']
    blockState: BlockState | None = None  # Moving block represented by the moving piston.
    facing: DirectionByte | None = None  # The direction it is moving.
    progress: float | None = None  # How far it has moved.
    extending: bool | None = None
    source: bool | None = None  # Whether the moving piston is the piston head.


@dataclass(kw_only=True)
class BlockEntityDataPotentSulfur(BlockEntity):
    id: Literal['minecraft:potent_sulfur']
    countdown: int | None = None  # Time in seconds until the next state switch (between dormant and erupting).  The timer only counts down when the potent sulfur creates a valid geyser.  Negative values will be replaced with a new duration of the current state.


@dataclass(kw_only=True)
class BlockEntityDataSculkCatalyst(BlockEntity):
    id: Literal['minecraft:sculk_catalyst']
    cursors: list[ChargeCursor] | None = None


@dataclass(kw_only=True)
class BlockEntityDataSculkSensor:
    id: Literal['minecraft:sculk_sensor']
    last_vibration_frequency: Annotated[int, 'Range | `1`-`15` | both inclusive'] | None = None
    listener: VibrationListener | None = None  # Vibration listener


@dataclass(kw_only=True)
class BlockEntityDataSculkShrieker:
    id: Literal['minecraft:sculk_shrieker']
    warning_level: int | None = None
    listener: VibrationListener | None = None


@dataclass(kw_only=True)
class BlockEntityDataShelf(ContainerBase):
    id: Literal['minecraft:shelf']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`2` | both inclusive']]], 'Length = 0-3 (both inclusive)'] | None = None  # Slots from 0 to 2.
    align_items_to_bottom: bool | None = None  # Defaults to `false`.


@dataclass(kw_only=True)
class BlockEntityDataShulkerBox(ContainerBase):
    id: Literal['minecraft:shulker_box']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class BlockEntityDataSign:
    id: Literal['minecraft:sign']


@dataclass(kw_only=True)
class BlockEntityDataSkull(BlockEntity):
    id: Literal['minecraft:skull']
    ExtraType: str | None = None  # Name of the owner, if exists will be converted to SkullOwner.
    note_block_sound: Annotated[str, IdSpec(registry='weighed_sound_event')] | None = None  # Sound to play when played with a note block. Only works on player head.
    profile: Profile | None = None  # Only works on player head.
    custom_name: Text | None = None


@dataclass(kw_only=True)
class BlockEntityDataSmoker(BlockEntity, Nameable, Lockable):
    id: Literal['minecraft:smoker']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`2` | both inclusive']]], 'Length = 0-3 (both inclusive)'] | None = None  # The items in this furnace, with slots: * 0: Item being smelted * 1: Fuel * 2: Output
    cooking_total_time: int | None = None  # The total amount of time the current cooking process will take. Defaults to `0`.
    cooking_time_spent: int | None = None  # The amount of time that the current cooking process has taken so far. Defaults to `0`.
    lit_time_remaining: int | None = None  # The amount of burn time remaining. Defaults to `0`.
    lit_total_time: int | None = None  # The total amount of burn time that was added in the last refuel. Defaults to `0`.
    speed_multiplier: float | None = None  # Used to speed up or slow down the next cooking process. Defaults to `1`.
    RecipesUsed: dict[Annotated[str, IdSpec(registry='recipe')], int] | None = None  # Recipes that have been used since the last time a result item was removed from the GUI. Used to calculate the experience to give to the player.


@dataclass(kw_only=True)
class BlockEntityDataStructureBlock(BlockEntity):
    id: Literal['minecraft:structure_block']
    name: Annotated[str, IdSpec(registry='structure', empty='allowed')] | None = None
    author: str | None = None  # Author of the structure.
    metadata: str | None = None  # Custom data for the structure. Stores the data id for "DATA" mode.
    posX: int | None = None  # Relative offset.
    posY: int | None = None  # Relative offset.
    posZ: int | None = None  # Relative offset.
    sizeX: int | None = None
    sizeY: int | None = None
    sizeZ: int | None = None
    rotation: Rotation | None = None
    mirror: Mirror | None = None
    mode: Mode | None = None
    ignoreEntities: bool | None = None
    showboundingbox: bool | None = None  # Whether to show the bounding box.
    powered: bool | None = None  # Whether it has been powered by redstone.
    showair: bool | None = None  # Whether to show invisible blocks inside the bounding box.
    strict: bool | None = None  # If set to `true`, the blocks in the placed structure will trigger block (entity) updates and shape updates. Defaults to `false`.
    integrity: float | None = None  # Chance for each block to stay.
    seed: int | None = None  # Seed for the integrity random.


@dataclass(kw_only=True)
class BlockEntityDataSuspiciousSand(BlockEntity):
    id: Literal['minecraft:suspicious_sand']
    LootTable: Annotated[str, IdSpec(registry='loot_table', empty='allowed')] | None = None  # Loot table that will decide the brushed loot.
    LootTableSeed: int | None = None  # Seed of the loot table.
    item: ItemStack | None = None  # Item that was rolled from the loot table, which is currently peeking out.
    hit_direction: DirectionByte | None = None  # Direction of the block that was interacted with. Write-only, is not saved by the game.


@dataclass(kw_only=True)
class BlockEntityDataTestBlock(BlockEntity):
    id: Literal['minecraft:test_block']
    mode: TestBlockMode | None = None
    message: str | None = None
    powered: bool | None = None


@dataclass(kw_only=True)
class BlockEntityDataTestInstanceBlock(BlockEntity):
    id: Literal['minecraft:test_instance_block']
    data: DataStruct | None = None
    errors: list[ErrorsStruct] | None = None


@dataclass(kw_only=True)
class BlockEntityDataTrappedChest(ContainerBase):
    id: Literal['minecraft:trapped_chest']
    Items: Annotated[list[SlottedItem[Annotated[int, 'Range | `0`-`26` | both inclusive']]], 'Length = 0-27 (both inclusive)'] | None = None  # Slots from 0 to 26.


@dataclass(kw_only=True)
class BlockEntityDataTrialSpawner:
    id: Literal['minecraft:trial_spawner']
    normal_config: TrialSpawnerConfig | Annotated[str, IdSpec(registry='trial_spawner')] | None = None  # Spawning behavior when the player does not have the Bad Omen effect.
    ominous_config: TrialSpawnerConfig | Annotated[str, IdSpec(registry='trial_spawner')] | None = None  # Spawning behavior when the player has the Bad Omen effect.
    required_player_range: Annotated[int, 'Range | `1`-`128` | both inclusive'] | None = None  # Maximum distance for players to activate the trial spawner, or join a battle
    target_cooldown_length: int | None = None  # Time in ticks for the cooldown period. Included the time spend dispensing the reward.
    registered_players: list[tuple[int, int, int, int]] | None = None  # Players that are have been nearby during the current battle
    current_mobs: list[tuple[int, int, int, int]] | None = None  # All mobs that have been spawned by this trial spawner and are currently alive
    cooldown_ends_at: int | None = None  # Gametime in ticks when the cooldown ends
    next_mob_spawns_at: int | None = None  # Gametime in ticks when the next spawning attempt happens
    total_mobs_spawned: int | None = None
    spawn_data: SpawnerEntry | None = None  # The next entity to spawn, also controlls the entity displayed in the trial spawner
    ejecting_loot_table: Annotated[str, IdSpec(registry='loot_table')] | None = None  # The loot table selected to be used to determine the reward


@dataclass(kw_only=True)
class BlockEntityDataVault:
    id: Literal['minecraft:vault']
    server_data: ServerDataStruct | None = None
    config: ConfigStruct | None = None
    shared_data: SharedDataStruct | None = None  # When a player is in range of the vault, the same display item will be shown to all players. This is also used for the items that are being ejected from the vault.


type BlockEntityData = BlockEntityDataBanner | BlockEntityDataBarrel | BlockEntityDataBeacon | BlockEntityDataBeehive | BlockEntityDataBlastFurnace | BlockEntityDataBrewingStand | BlockEntityDataBrushableBlock | BlockEntityDataCalibratedSculkSensor | BlockEntityDataCampfire | BlockEntityDataChest | BlockEntityDataChiseledBookshelf | BlockEntityDataCommandBlock | BlockEntityDataComparator | BlockEntityDataConduit | BlockEntityDataCrafter | BlockEntityDataCreakingHeart | BlockEntityDataDecoratedPot | BlockEntityDataDispenser | BlockEntityDataDropper | BlockEntityDataEnchantingTable | BlockEntityDataEndGateway | BlockEntityDataFurnace | BlockEntityDataHangingSign | BlockEntityDataHopper | BlockEntityDataJigsaw | BlockEntityDataJukebox | BlockEntityDataLectern | BlockEntityDataMobSpawner | BlockEntityDataMovingPiston | BlockEntityDataPotentSulfur | BlockEntityDataSculkCatalyst | BlockEntityDataSculkSensor | BlockEntityDataSculkShrieker | BlockEntityDataShelf | BlockEntityDataShulkerBox | BlockEntityDataSign | BlockEntityDataSkull | BlockEntityDataSmoker | BlockEntityDataStructureBlock | BlockEntityDataSuspiciousSand | BlockEntityDataTestBlock | BlockEntityDataTestInstanceBlock | BlockEntityDataTrappedChest | BlockEntityDataTrialSpawner | BlockEntityDataVault


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::BlockEntityData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "block_entity_type"
                                }
                            }
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
                                "id"
                            ]
                        }
                    ],
                    "registry": "minecraft:block_entity"
                }
            }
        ]
    }
}

