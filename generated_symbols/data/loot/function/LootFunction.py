"""
Generated from symbols.json for ::java::data::loot::function::LootFunction
Local link to file: generated_symbols/data/loot/function/LootFunction.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.EnchantedCountBase import EnchantedCountBase
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.advancement.predicate.ItemPredicate import ItemPredicate
    from generated_symbols.data.item_modifier.ItemModifier import ItemModifier
    from generated_symbols.data.loot.BlockEntityTarget import BlockEntityTarget
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.data.loot.ItemStackTarget import ItemStackTarget
    from generated_symbols.data.loot.LootPoolEntry import LootPoolEntry
    from generated_symbols.data.loot.function.AttributeModifier import AttributeModifier
    from generated_symbols.data.loot.function.BannerPatternLayer import BannerPatternLayer
    from generated_symbols.data.loot.function.ContainerComponents import ContainerComponents
    from generated_symbols.data.loot.function.CopyNbtStrategy import CopyNbtStrategy
    from generated_symbols.data.loot.function.SetNameTarget import SetNameTarget
    from generated_symbols.data.loot.function.StewEffect import StewEffect
    from generated_symbols.data.number_provider.NumberProviderRef import NumberProviderRef
    from generated_symbols.data.util.IntRange import IntRange
    from generated_symbols.data.util.NbtProvider import NbtProvider
    from generated_symbols.registry.KnownBlockId import KnownBlockId
    from generated_symbols.util.Filterable import Filterable
    from generated_symbols.util.color.RGB import RGB
    from generated_symbols.util.text.Text import Text
    from generated_symbols.world.component.CustomData import CustomData
    from generated_symbols.world.component.DataComponentPatch import DataComponentPatch
    from generated_symbols.world.component.item.Explosion import Explosion
    from generated_symbols.world.component.item.FireworkShape import FireworkShape


@dataclass(kw_only=True)
class ParametersStruct:
    extra: int
    probability: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class ParametersStruct2:
    bonusMultiplier: int


@dataclass(kw_only=True)
class OpsStruct:
    source: str
    target: str
    op: CopyNbtStrategy


@dataclass(kw_only=True)
class FloatsStructAppend:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FloatsStructInsert:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class FloatsStructReplaceAll:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FloatsStructReplaceSection:
    values: list[NumberProviderRef]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type FloatsStruct = FloatsStructAppend | FloatsStructInsert | FloatsStructReplaceAll | FloatsStructReplaceSection

@dataclass(kw_only=True)
class FlagsStructAppend:
    values: list[bool]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FlagsStructInsert:
    values: list[bool]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class FlagsStructReplaceAll:
    values: list[bool]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class FlagsStructReplaceSection:
    values: list[bool]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type FlagsStruct = FlagsStructAppend | FlagsStructInsert | FlagsStructReplaceAll | FlagsStructReplaceSection

@dataclass(kw_only=True)
class StringsStructAppend:
    values: list[str]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class StringsStructInsert:
    values: list[str]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class StringsStructReplaceAll:
    values: list[str]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class StringsStructReplaceSection:
    values: list[str]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type StringsStruct = StringsStructAppend | StringsStructInsert | StringsStructReplaceAll | StringsStructReplaceSection

@dataclass(kw_only=True)
class ColorsStructAppend:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ColorsStructInsert:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class ColorsStructReplaceAll:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ColorsStructReplaceSection:
    values: list[NumberProviderRef | RGB]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type ColorsStruct = ColorsStructAppend | ColorsStructInsert | ColorsStructReplaceAll | ColorsStructReplaceSection

@dataclass(kw_only=True)
class ExplosionsStructAppend:
    values: list[Explosion]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ExplosionsStructInsert:
    values: list[Explosion]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class ExplosionsStructReplaceAll:
    values: list[Explosion]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class ExplosionsStructReplaceSection:
    values: list[Explosion]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type ExplosionsStruct = ExplosionsStructAppend | ExplosionsStructInsert | ExplosionsStructReplaceAll | ExplosionsStructReplaceSection

@dataclass(kw_only=True)
class LootFunctionApplyBonusBinomialWithBonusCount(Conditions):
    type: Literal['minecraft:apply_bonus']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:binomial_with_bonus_count']
    parameters: ParametersStruct


@dataclass(kw_only=True)
class LootFunctionApplyBonusOreDrops(Conditions):
    type: Literal['minecraft:apply_bonus']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:ore_drops']


@dataclass(kw_only=True)
class LootFunctionApplyBonusUniformBonusCount(Conditions):
    type: Literal['minecraft:apply_bonus']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:uniform_bonus_count']
    parameters: ParametersStruct2


type LootFunctionApplyBonus = LootFunctionApplyBonusBinomialWithBonusCount | LootFunctionApplyBonusOreDrops | LootFunctionApplyBonusUniformBonusCount

@dataclass(kw_only=True)
class LootFunctionCopyComponents(Conditions):
    type: Literal['minecraft:copy_components']
    source: BlockEntityTarget | EntityTarget | ItemStackTarget
    include: list[Annotated[str, IdSpec(registry='data_component_type')]] | None = None  # If omitted, all components present are included
    exclude: list[Annotated[str, IdSpec(registry='data_component_type')]] | None = None  # Defaults to none.


@dataclass(kw_only=True)
class LootFunctionCopyCustomData(Conditions):
    type: Literal['minecraft:copy_custom_data']
    source: NbtProvider
    ops: list[OpsStruct]


@dataclass(kw_only=True)
class LootFunctionCopyName(Conditions):
    type: Literal['minecraft:copy_name']
    source: EntityTarget | BlockEntityTarget


@dataclass(kw_only=True)
class LootFunctionCopyNbt(Conditions):
    type: Literal['minecraft:copy_nbt']
    source: NbtProvider
    ops: list[OpsStruct]


@dataclass(kw_only=True)
class LootFunctionCopyState(Conditions):
    type: Literal['minecraft:copy_state']
    block: Annotated[str, IdSpec(registry='block')] | KnownBlockId
    properties: list[str]


@dataclass(kw_only=True)
class LootFunctionDiscard(Conditions):
    type: Literal['minecraft:discard']


@dataclass(kw_only=True)
class LootFunctionEnchantRandomly(Conditions):
    type: Literal['minecraft:enchant_randomly']
    options: Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | list[Annotated[str, IdSpec(registry='enchantment')]] | None = None  # The allowed enchantments. If omitted, all enchantments applicable to the item are possible.
    only_compatible: bool | None = None  # Whether to only enchant with item-compatible enchantments. Defaults to `true`.  Note: Books are considered compatible with all Enchantments.
    include_additional_cost_component: bool | None = None  # Whether to add `additional_trade_cost` component to the enchanted item. Additional cost value is determined by the enchantment level, with the formula `2 + random(0, 5 + level * 10) + 3 * level`. Defaults to `false`.


@dataclass(kw_only=True)
class LootFunctionEnchantWithLevels(Conditions):
    type: Literal['minecraft:enchant_with_levels']
    levels: NumberProviderRef  # The levels to enchant this item with.
    options: Annotated[str, IdSpec(registry='enchantment', tags='allowed')] | list[Annotated[str, IdSpec(registry='enchantment')]] | None = None  # The allowed enchantments. If omitted, all enchantments applicable to the item are possible.
    include_additional_cost_component: bool | None = None  # Whether to add `additional_trade_cost` component to the enchanted item. Additional cost value is equal to the level cost determined by `levels`. Defaults to `false`.


@dataclass(kw_only=True)
class LootFunctionEnchantedCountIncrease(Conditions, EnchantedCountBase):
    type: Literal['minecraft:enchanted_count_increase']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]  # Enchantment that increases yields.


@dataclass(kw_only=True)
class LootFunctionExplorationMap(Conditions):
    type: Literal['minecraft:exploration_map']
    destination: Annotated[str, IdSpec(registry='worldgen/structure', tags='allowed')] | list[Annotated[str, IdSpec(registry='worldgen/structure')]]  # Generated structure to locate. Accepts any of the structure types used by the `/locate` command.
    decoration: Annotated[str, IdSpec(registry='map_decoration_type')] | None = None  # The icon used to mark the destination on the map.
    zoom: int | None = None  # Defaults to 2.
    search_radius: int | None = None  # The size, in chunks, of the area to search for structures. The area checked is square, not circular. Radius `0` causes only the current chunk to be searched, radius `1` causes the current chunk and eight adjacent chunks to be searched, and so on. Defaults to `50`.
    skip_existing_chunks: bool | None = None  # Whether to not search in chunks that have already been generated. Defaults to `true`.


@dataclass(kw_only=True)
class LootFunctionExplosionDecay(Conditions):
    type: Literal['minecraft:explosion_decay']


@dataclass(kw_only=True)
class LootFunctionFillPlayerHead(Conditions):
    type: Literal['minecraft:fill_player_head']
    entity: EntityTarget  # `this` to use the entity that died or the player that gained the advancement, opened the container, or broke the block.


@dataclass(kw_only=True)
class LootFunctionFiltered(Conditions):
    type: Literal['minecraft:filtered']
    item_filter: ItemPredicate  # Item predicate to select items to modify.
    on_pass: ItemModifier | None = None  # Loot function to apply to the item when `item_filter` passes.
    on_fail: ItemModifier | None = None  # Loot function to apply to the item when `item_filter` fails.


@dataclass(kw_only=True)
class LootFunctionFurnaceSmelt(Conditions):
    type: Literal['minecraft:furnace_smelt']


@dataclass(kw_only=True)
class LootFunctionLimitCount(Conditions):
    type: Literal['minecraft:limit_count']
    limit: IntRange  # Limits the count of the item to a range.


@dataclass(kw_only=True)
class LootFunctionLootingEnchant(Conditions, EnchantedCountBase):
    type: Literal['minecraft:looting_enchant']


@dataclass(kw_only=True)
class LootFunctionModifyContents(Conditions):
    type: Literal['minecraft:modify_contents']
    component: ContainerComponents  # Describes target component's items to modify.
    modifier: ItemModifier  # Applied to every item inside container.


@dataclass(kw_only=True)
class LootFunctionReference(Conditions):
    type: Literal['minecraft:reference']
    name: Annotated[str, IdSpec(registry='item_modifier')]  # Item modifier to reference.


@dataclass(kw_only=True)
class LootFunctionSequence(Conditions):
    type: Literal['minecraft:sequence']
    functions: ItemModifier  # List of functions to apply to this item.


@dataclass(kw_only=True)
class LootFunctionSetAttributes(Conditions):
    type: Literal['minecraft:set_attributes']
    modifiers: list[AttributeModifier]  # List of attribute modifiers to apply to this item.
    replace: bool | None = None  # Whether to replace existing attributes (otherwise append to existing). Defaults to `true`.


@dataclass(kw_only=True)
class LootFunctionSetBannerPattern(Conditions):
    type: Literal['minecraft:set_banner_pattern']
    patterns: list[BannerPatternLayer]  # List of banner pattern layers.
    append: bool  # Whether to add to the banner pattern list.


@dataclass(kw_only=True)
class LootFunctionSetBookCover(Conditions):
    type: Literal['minecraft:set_book_cover']
    title: Filterable[Annotated[str, 'Length = 0-32 (both inclusive)']] | None = None  # If omitted, the original title is kept (or an empty string is used if there was no component)
    author: str | None = None  # If omitted, the original author is kept (or an empty string is used if there was no component)
    generation: Annotated[int, 'Range | `0`-`3` | both inclusive'] | None = None  # If omitted, the original generation is kept (or 0 is used if there was no component)


@dataclass(kw_only=True)
class LootFunctionSetComponents(Conditions):
    type: Literal['minecraft:set_components']
    components: DataComponentPatch


@dataclass(kw_only=True)
class LootFunctionSetContents(Conditions):
    type: Literal['minecraft:set_contents']
    component: ContainerComponents  # Describes target component to be filled with items.
    entries: list[LootPoolEntry]


@dataclass(kw_only=True)
class LootFunctionSetCount(Conditions):
    type: Literal['minecraft:set_count']
    count: NumberProviderRef
    add: bool | None = None  # Whether to add to the existing count. Defaults to `false`.


@dataclass(kw_only=True)
class LootFunctionSetCustomData(Conditions):
    type: Literal['minecraft:set_custom_data']
    tag: CustomData


@dataclass(kw_only=True)
class LootFunctionSetCustomModelData(Conditions):
    type: Literal['minecraft:set_custom_model_data']
    floats: FloatsStruct | None = None
    flags: FlagsStruct | None = None
    strings: StringsStruct | None = None
    colors: ColorsStruct | None = None


@dataclass(kw_only=True)
class LootFunctionSetDamage(Conditions):
    type: Literal['minecraft:set_damage']
    damage: NumberProviderRef  # Decimal percentage. Can be negative when used in combination with `add`.  Clamps to a float between `-1` & `1` (inclusive).
    add: bool | None = None  # Whether to add to the existing damage of the item. Defaults to `false`.


@dataclass(kw_only=True)
class LootFunctionSetEnchantments(Conditions):
    type: Literal['minecraft:set_enchantments']
    enchantments: dict[Annotated[str, IdSpec(registry='enchantment')], NumberProviderRef]  # A map of enchantments to levels. Setting an enchantment to `0` removes it from the item.  Each level is clamped to a positive integer.
    add: bool | None = None  # Whether to add to the level of each enchantment. Defaults to `false`.


@dataclass(kw_only=True)
class LootFunctionSetFireworkExplosion(Conditions):
    type: Literal['minecraft:set_firework_explosion']
    shape: FireworkShape | None = None  # If omitted, the original shape is kept (or `small_ball` is used if there was no component).
    colors: list[int] | None = None  # If omitted, the original colors are kept (or `[]` is used if there was no component). Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    fade_colors: list[int] | None = None  # If omitted, the original fade colors are kept (or `[]` is used if there was no component). Calculated as `RED << 16 | GREEN << 8 | BLUE`. Each of these fields must be between 0 and 255, inclusive.
    trail: bool | None = None  # If omitted, the original `has_trail` value is kept (or `false` is used if there was no component).
    twinkle: bool | None = None  # If omitted, the original `has_twinkle` value is kept (or `false` is used if there was no component).


@dataclass(kw_only=True)
class LootFunctionSetFireworks(Conditions):
    type: Literal['minecraft:set_fireworks']
    flight_duration: Annotated[int, 'Range | `0`-`255` | both inclusive'] | None = None  # If omitted, the flight duration of the item is left untouched - or set to 0 if the component did not exist before.
    explosions: ExplosionsStruct | None = None


@dataclass(kw_only=True)
class LootFunctionSetInstrument(Conditions):
    type: Literal['minecraft:set_instrument']
    options: Annotated[str, IdSpec(registry='instrument', tags='allowed')] | list[Annotated[str, IdSpec(registry='instrument')]]  # Sets the instrument tag for a goat horn.


@dataclass(kw_only=True)
class LootFunctionSetItem(Conditions):
    type: Literal['minecraft:set_item']
    item: Annotated[str, IdSpec(registry='item', exclude=('air',))]


@dataclass(kw_only=True)
class LootFunctionSetLootTable(Conditions):
    type: Literal['minecraft:set_loot_table']
    type_2: Annotated[str, IdSpec(registry='block_entity_type')]  # The block entity type of the container.
    tag: Annotated[str, IdSpec(registry='loot_table')]  # The loot table to set to the container block item.
    seed: int | None = None  # The container seed to use. Defaults to a random seed.


@dataclass(kw_only=True)
class LootFunctionSetLoreAppend(Conditions):
    type: Literal['minecraft:set_lore']
    lore: list[Text]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.
    entity: EntityTarget | None = None  # The entity used to resolve the text components.


@dataclass(kw_only=True)
class LootFunctionSetLoreInsert(Conditions):
    type: Literal['minecraft:set_lore']
    lore: list[Text]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class LootFunctionSetLoreReplaceAll(Conditions):
    type: Literal['minecraft:set_lore']
    lore: list[Text]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.
    entity: EntityTarget | None = None  # The entity used to resolve the text components.


@dataclass(kw_only=True)
class LootFunctionSetLoreReplaceSection(Conditions):
    type: Literal['minecraft:set_lore']
    lore: list[Text]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type LootFunctionSetLore = LootFunctionSetLoreAppend | LootFunctionSetLoreInsert | LootFunctionSetLoreReplaceAll | LootFunctionSetLoreReplaceSection

@dataclass(kw_only=True)
class LootFunctionSetName(Conditions):
    type: Literal['minecraft:set_name']
    name: Text
    entity: EntityTarget | None = None  # Specifies the entity to act as the target `@s` in the JSON text component.
    target: SetNameTarget | None = None  # Which name component to set. Defaults to `custom_name`.


@dataclass(kw_only=True)
class LootFunctionSetNbt(Conditions):
    type: Literal['minecraft:set_nbt']
    tag: str


@dataclass(kw_only=True)
class LootFunctionSetOminousBottleAmplifier(Conditions):
    type: Literal['minecraft:set_ominous_bottle_amplifier']
    amplifier: NumberProviderRef


@dataclass(kw_only=True)
class LootFunctionSetPotion(Conditions):
    type: Literal['minecraft:set_potion']
    id: Annotated[str, IdSpec(registry='potion')]  # The potion identifier.


@dataclass(kw_only=True)
class LootFunctionSetRandomDyes(Conditions):
    type: Literal['minecraft:set_random_dyes']
    number_of_dyes: NumberProviderRef  # Applies specified number of random dyes to the item.  For example, one possible outcome of `"number_of_dyes": 2` is `#2C3065`, which is the combination of a blue dye and a black dye.  The same dye color can be selected multiple times.


@dataclass(kw_only=True)
class LootFunctionSetRandomPotion(Conditions):
    type: Literal['minecraft:set_random_potion']
    options: Annotated[str, IdSpec(registry='potion', tags='allowed')] | Annotated[str, IdSpec(registry='potion')] | None = None  # Possible potions to select from. Defaults to all potions.


@dataclass(kw_only=True)
class LootFunctionSetStewEffect(Conditions):
    type: Literal['minecraft:set_stew_effect']
    effects: list[StewEffect] | None = None  # Sets the status effects for suspicious stew.


@dataclass(kw_only=True)
class LootFunctionSetWritableBookPagesAppend(Conditions):
    type: Literal['minecraft:set_writable_book_pages']
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWritableBookPagesInsert(Conditions):
    type: Literal['minecraft:set_writable_book_pages']
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class LootFunctionSetWritableBookPagesReplaceAll(Conditions):
    type: Literal['minecraft:set_writable_book_pages']
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWritableBookPagesReplaceSection(Conditions):
    type: Literal['minecraft:set_writable_book_pages']
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type LootFunctionSetWritableBookPages = LootFunctionSetWritableBookPagesAppend | LootFunctionSetWritableBookPagesInsert | LootFunctionSetWritableBookPagesReplaceAll | LootFunctionSetWritableBookPagesReplaceSection

@dataclass(kw_only=True)
class LootFunctionSetWrittenBookPagesAppend(Conditions):
    type: Literal['minecraft:set_written_book_pages']
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWrittenBookPagesInsert(Conditions):
    type: Literal['minecraft:set_written_book_pages']
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset in the list to insert into. Defaults to 0.


@dataclass(kw_only=True)
class LootFunctionSetWrittenBookPagesReplaceAll(Conditions):
    type: Literal['minecraft:set_written_book_pages']
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWrittenBookPagesReplaceSection(Conditions):
    type: Literal['minecraft:set_written_book_pages']
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.
    offset: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The offset of the section to replace. Defaults to 0.
    size: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The size of the section to replace. Defaults to size of the new list.


type LootFunctionSetWrittenBookPages = LootFunctionSetWrittenBookPagesAppend | LootFunctionSetWrittenBookPagesInsert | LootFunctionSetWrittenBookPagesReplaceAll | LootFunctionSetWrittenBookPagesReplaceSection

@dataclass(kw_only=True)
class LootFunctionToggleTooltips(Conditions):
    type: Literal['minecraft:toggle_tooltips']
    toggles: dict[Annotated[str, IdSpec(registry='data_component_type')], bool]  # Toggles which tooltips are shown.


type LootFunction = LootFunctionApplyBonus | LootFunctionCopyComponents | LootFunctionCopyCustomData | LootFunctionCopyName | LootFunctionCopyNbt | LootFunctionCopyState | LootFunctionDiscard | LootFunctionEnchantRandomly | LootFunctionEnchantWithLevels | LootFunctionEnchantedCountIncrease | LootFunctionExplorationMap | LootFunctionExplosionDecay | LootFunctionFillPlayerHead | LootFunctionFiltered | LootFunctionFurnaceSmelt | LootFunctionLimitCount | LootFunctionLootingEnchant | LootFunctionModifyContents | LootFunctionReference | LootFunctionSequence | LootFunctionSetAttributes | LootFunctionSetBannerPattern | LootFunctionSetBookCover | LootFunctionSetComponents | LootFunctionSetContents | LootFunctionSetCount | LootFunctionSetCustomData | LootFunctionSetCustomModelData | LootFunctionSetDamage | LootFunctionSetEnchantments | LootFunctionSetFireworkExplosion | LootFunctionSetFireworks | LootFunctionSetInstrument | LootFunctionSetItem | LootFunctionSetLootTable | LootFunctionSetLore | LootFunctionSetName | LootFunctionSetNbt | LootFunctionSetOminousBottleAmplifier | LootFunctionSetPotion | LootFunctionSetRandomDyes | LootFunctionSetRandomPotion | LootFunctionSetStewEffect | LootFunctionSetWritableBookPages | LootFunctionSetWrittenBookPages | LootFunctionToggleTooltips


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::loot::function::LootFunction": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "function",
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "reference",
                            "path": "::java::data::loot::LootFunctionType",
                            "attributes": [
                                {
                                    "name": "until",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id"
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
                                            "value": "1.16"
                                        }
                                    }
                                },
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "loot_function_type"
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
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "function"
                            ]
                        }
                    ],
                    "registry": "minecraft:loot_function"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "loot_function_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    }
                ],
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
                    "registry": "minecraft:loot_function"
                }
            }
        ]
    }
}

