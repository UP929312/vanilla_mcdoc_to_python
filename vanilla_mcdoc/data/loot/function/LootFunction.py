"""
Generated from symbols.json for ::java::data::loot::function::LootFunction
Local link to file: vanilla_mcdoc/data/loot/function/LootFunction.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import tag_of
from vanilla_mcdoc.data.loot.function.BinomialWithBonusCountFormula import BinomialWithBonusCountFormula
from vanilla_mcdoc.data.loot.function.Conditions import Conditions
from vanilla_mcdoc.data.loot.function.CopyComponents import CopyComponents
from vanilla_mcdoc.data.loot.function.CopyName import CopyName
from vanilla_mcdoc.data.loot.function.CopyNbt import CopyNbt
from vanilla_mcdoc.data.loot.function.CopyState import CopyState
from vanilla_mcdoc.data.loot.function.EnchantRandomly import EnchantRandomly
from vanilla_mcdoc.data.loot.function.EnchantWithLevels import EnchantWithLevels
from vanilla_mcdoc.data.loot.function.EnchantedCountIncrease import EnchantedCountIncrease
from vanilla_mcdoc.data.loot.function.ExplorationMap import ExplorationMap
from vanilla_mcdoc.data.loot.function.FillPlayerHead import FillPlayerHead
from vanilla_mcdoc.data.loot.function.Filtered import Filtered
from vanilla_mcdoc.data.loot.function.InsertListOperation import InsertListOperation
from vanilla_mcdoc.data.loot.function.LimitCount import LimitCount
from vanilla_mcdoc.data.loot.function.ModifyContents import ModifyContents
from vanilla_mcdoc.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation
from vanilla_mcdoc.data.loot.function.Sequence import Sequence
from vanilla_mcdoc.data.loot.function.SetAttributes import SetAttributes
from vanilla_mcdoc.data.loot.function.SetBannerPattern import SetBannerPattern
from vanilla_mcdoc.data.loot.function.SetBookCover import SetBookCover
from vanilla_mcdoc.data.loot.function.SetComponents import SetComponents
from vanilla_mcdoc.data.loot.function.SetContents import SetContents
from vanilla_mcdoc.data.loot.function.SetCount import SetCount
from vanilla_mcdoc.data.loot.function.SetCustomData import SetCustomData
from vanilla_mcdoc.data.loot.function.SetCustomModelData import SetCustomModelData
from vanilla_mcdoc.data.loot.function.SetDamage import SetDamage
from vanilla_mcdoc.data.loot.function.SetEnchantments import SetEnchantments
from vanilla_mcdoc.data.loot.function.SetFireworkExplosion import SetFireworkExplosion
from vanilla_mcdoc.data.loot.function.SetFireworks import SetFireworks
from vanilla_mcdoc.data.loot.function.SetInstrument import SetInstrument
from vanilla_mcdoc.data.loot.function.SetItem import SetItem
from vanilla_mcdoc.data.loot.function.SetLootTable import SetLootTable
from vanilla_mcdoc.data.loot.function.SetName import SetName
from vanilla_mcdoc.data.loot.function.SetOminousBottleAmplifier import SetOminousBottleAmplifier
from vanilla_mcdoc.data.loot.function.SetPotion import SetPotion
from vanilla_mcdoc.data.loot.function.SetRandomDyes import SetRandomDyes
from vanilla_mcdoc.data.loot.function.SetRandomPotion import SetRandomPotion
from vanilla_mcdoc.data.loot.function.SetStewEffect import SetStewEffect
from vanilla_mcdoc.data.loot.function.ToggleTooltips import ToggleTooltips
from vanilla_mcdoc.data.loot.function.UniformBonusFormula import UniformBonusFormula
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
    from vanilla_mcdoc.util.Filterable import Filterable
    from vanilla_mcdoc.util.text.Text import Text


class LootFunctionApplyBonusBinomialWithBonusCount(BinomialWithBonusCountFormula, Conditions):
    type: Literal['minecraft:apply_bonus', 'apply_bonus'] = 'minecraft:apply_bonus'
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:binomial_with_bonus_count', 'binomial_with_bonus_count'] = 'minecraft:binomial_with_bonus_count'


class LootFunctionApplyBonusOreDrops(Conditions):
    type: Literal['minecraft:apply_bonus', 'apply_bonus'] = 'minecraft:apply_bonus'
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:ore_drops', 'ore_drops'] = 'minecraft:ore_drops'


class LootFunctionApplyBonusUniformBonusCount(Conditions, UniformBonusFormula):
    type: Literal['minecraft:apply_bonus', 'apply_bonus'] = 'minecraft:apply_bonus'
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:uniform_bonus_count', 'uniform_bonus_count'] = 'minecraft:uniform_bonus_count'


type LootFunctionApplyBonus = Annotated[
    Annotated[LootFunctionApplyBonusBinomialWithBonusCount, Tag('minecraft:binomial_with_bonus_count')]
    | Annotated[LootFunctionApplyBonusOreDrops, Tag('minecraft:ore_drops')]
    | Annotated[LootFunctionApplyBonusUniformBonusCount, Tag('minecraft:uniform_bonus_count')],
    Discriminator(tag_of('formula')),
]


class LootFunctionCopyComponents(CopyComponents):
    type: Literal['minecraft:copy_components', 'copy_components'] = 'minecraft:copy_components'


class LootFunctionCopyCustomData(CopyNbt):
    type: Literal['minecraft:copy_custom_data', 'copy_custom_data'] = 'minecraft:copy_custom_data'


class LootFunctionCopyName(CopyName):
    type: Literal['minecraft:copy_name', 'copy_name'] = 'minecraft:copy_name'


class LootFunctionCopyState(CopyState):
    type: Literal['minecraft:copy_state', 'copy_state'] = 'minecraft:copy_state'


class LootFunctionDiscard(Conditions):
    type: Literal['minecraft:discard', 'discard'] = 'minecraft:discard'


class LootFunctionEnchantRandomly(EnchantRandomly):
    type: Literal['minecraft:enchant_randomly', 'enchant_randomly'] = 'minecraft:enchant_randomly'


class LootFunctionEnchantWithLevels(EnchantWithLevels):
    type: Literal['minecraft:enchant_with_levels', 'enchant_with_levels'] = 'minecraft:enchant_with_levels'


class LootFunctionEnchantedCountIncrease(EnchantedCountIncrease):
    type: Literal['minecraft:enchanted_count_increase', 'enchanted_count_increase'] = 'minecraft:enchanted_count_increase'


class LootFunctionExplorationMap(ExplorationMap):
    type: Literal['minecraft:exploration_map', 'exploration_map'] = 'minecraft:exploration_map'


class LootFunctionExplosionDecay(Conditions):
    type: Literal['minecraft:explosion_decay', 'explosion_decay'] = 'minecraft:explosion_decay'


class LootFunctionFillPlayerHead(FillPlayerHead):
    type: Literal['minecraft:fill_player_head', 'fill_player_head'] = 'minecraft:fill_player_head'


class LootFunctionFiltered(Filtered):
    type: Literal['minecraft:filtered', 'filtered'] = 'minecraft:filtered'


class LootFunctionFurnaceSmelt(Conditions):
    type: Literal['minecraft:furnace_smelt', 'furnace_smelt'] = 'minecraft:furnace_smelt'


class LootFunctionLimitCount(LimitCount):
    type: Literal['minecraft:limit_count', 'limit_count'] = 'minecraft:limit_count'


class LootFunctionModifyContents(ModifyContents):
    type: Literal['minecraft:modify_contents', 'modify_contents'] = 'minecraft:modify_contents'


class LootFunctionSequence(Sequence):
    type: Literal['minecraft:sequence', 'sequence'] = 'minecraft:sequence'


class LootFunctionSetAttributes(SetAttributes):
    type: Literal['minecraft:set_attributes', 'set_attributes'] = 'minecraft:set_attributes'


class LootFunctionSetBannerPattern(SetBannerPattern):
    type: Literal['minecraft:set_banner_pattern', 'set_banner_pattern'] = 'minecraft:set_banner_pattern'


class LootFunctionSetBookCover(SetBookCover):
    type: Literal['minecraft:set_book_cover', 'set_book_cover'] = 'minecraft:set_book_cover'


class LootFunctionSetComponents(SetComponents):
    type: Literal['minecraft:set_components', 'set_components'] = 'minecraft:set_components'


class LootFunctionSetContents(SetContents):
    type: Literal['minecraft:set_contents', 'set_contents'] = 'minecraft:set_contents'


class LootFunctionSetCount(SetCount):
    type: Literal['minecraft:set_count', 'set_count'] = 'minecraft:set_count'


class LootFunctionSetCustomData(SetCustomData):
    type: Literal['minecraft:set_custom_data', 'set_custom_data'] = 'minecraft:set_custom_data'


class LootFunctionSetCustomModelData(SetCustomModelData):
    type: Literal['minecraft:set_custom_model_data', 'set_custom_model_data'] = 'minecraft:set_custom_model_data'


class LootFunctionSetDamage(SetDamage):
    type: Literal['minecraft:set_damage', 'set_damage'] = 'minecraft:set_damage'


class LootFunctionSetEnchantments(SetEnchantments):
    type: Literal['minecraft:set_enchantments', 'set_enchantments'] = 'minecraft:set_enchantments'


class LootFunctionSetFireworkExplosion(SetFireworkExplosion):
    type: Literal['minecraft:set_firework_explosion', 'set_firework_explosion'] = 'minecraft:set_firework_explosion'


class LootFunctionSetFireworks(SetFireworks):
    type: Literal['minecraft:set_fireworks', 'set_fireworks'] = 'minecraft:set_fireworks'


class LootFunctionSetInstrument(SetInstrument):
    type: Literal['minecraft:set_instrument', 'set_instrument'] = 'minecraft:set_instrument'


class LootFunctionSetItem(SetItem):
    type: Literal['minecraft:set_item', 'set_item'] = 'minecraft:set_item'


class LootFunctionSetLootTable(SetLootTable):
    type: Literal['minecraft:set_loot_table', 'set_loot_table'] = 'minecraft:set_loot_table'


class LootFunctionSetLoreAppend(Conditions):
    type: Literal['minecraft:set_lore', 'set_lore'] = 'minecraft:set_lore'
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class LootFunctionSetLoreInsert(Conditions, InsertListOperation):
    type: Literal['minecraft:set_lore', 'set_lore'] = 'minecraft:set_lore'
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class LootFunctionSetLoreReplaceAll(Conditions):
    type: Literal['minecraft:set_lore', 'set_lore'] = 'minecraft:set_lore'
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class LootFunctionSetLoreReplaceSection(Conditions, ReplaceSectionListOperation):
    type: Literal['minecraft:set_lore', 'set_lore'] = 'minecraft:set_lore'
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type LootFunctionSetLore = Annotated[
    Annotated[LootFunctionSetLoreAppend, Tag('minecraft:append')]
    | Annotated[LootFunctionSetLoreInsert, Tag('minecraft:insert')]
    | Annotated[LootFunctionSetLoreReplaceAll, Tag('minecraft:replace_all')]
    | Annotated[LootFunctionSetLoreReplaceSection, Tag('minecraft:replace_section')],
    Discriminator(tag_of('mode')),
]


class LootFunctionSetName(SetName):
    type: Literal['minecraft:set_name', 'set_name'] = 'minecraft:set_name'


class LootFunctionSetOminousBottleAmplifier(SetOminousBottleAmplifier):
    type: Literal['minecraft:set_ominous_bottle_amplifier', 'set_ominous_bottle_amplifier'] = 'minecraft:set_ominous_bottle_amplifier'


class LootFunctionSetPotion(SetPotion):
    type: Literal['minecraft:set_potion', 'set_potion'] = 'minecraft:set_potion'


class LootFunctionSetRandomDyes(SetRandomDyes):
    type: Literal['minecraft:set_random_dyes', 'set_random_dyes'] = 'minecraft:set_random_dyes'


class LootFunctionSetRandomPotion(SetRandomPotion):
    type: Literal['minecraft:set_random_potion', 'set_random_potion'] = 'minecraft:set_random_potion'


class LootFunctionSetStewEffect(SetStewEffect):
    type: Literal['minecraft:set_stew_effect', 'set_stew_effect'] = 'minecraft:set_stew_effect'


class LootFunctionSetWritableBookPagesAppend(Conditions):
    type: Literal['minecraft:set_writable_book_pages', 'set_writable_book_pages'] = 'minecraft:set_writable_book_pages'
    pages: list[Filterable[str] | str]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class LootFunctionSetWritableBookPagesInsert(Conditions, InsertListOperation):
    type: Literal['minecraft:set_writable_book_pages', 'set_writable_book_pages'] = 'minecraft:set_writable_book_pages'
    pages: list[Filterable[str] | str]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class LootFunctionSetWritableBookPagesReplaceAll(Conditions):
    type: Literal['minecraft:set_writable_book_pages', 'set_writable_book_pages'] = 'minecraft:set_writable_book_pages'
    pages: list[Filterable[str] | str]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class LootFunctionSetWritableBookPagesReplaceSection(Conditions, ReplaceSectionListOperation):
    type: Literal['minecraft:set_writable_book_pages', 'set_writable_book_pages'] = 'minecraft:set_writable_book_pages'
    pages: list[Filterable[str] | str]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type LootFunctionSetWritableBookPages = Annotated[
    Annotated[LootFunctionSetWritableBookPagesAppend, Tag('minecraft:append')]
    | Annotated[LootFunctionSetWritableBookPagesInsert, Tag('minecraft:insert')]
    | Annotated[LootFunctionSetWritableBookPagesReplaceAll, Tag('minecraft:replace_all')]
    | Annotated[LootFunctionSetWritableBookPagesReplaceSection, Tag('minecraft:replace_section')],
    Discriminator(tag_of('mode')),
]


class LootFunctionSetWrittenBookPagesAppend(Conditions):
    type: Literal['minecraft:set_written_book_pages', 'set_written_book_pages'] = 'minecraft:set_written_book_pages'
    pages: list[Filterable[Text] | Text]  # Sets the pages of a written book.
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class LootFunctionSetWrittenBookPagesInsert(Conditions, InsertListOperation):
    type: Literal['minecraft:set_written_book_pages', 'set_written_book_pages'] = 'minecraft:set_written_book_pages'
    pages: list[Filterable[Text] | Text]  # Sets the pages of a written book.
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class LootFunctionSetWrittenBookPagesReplaceAll(Conditions):
    type: Literal['minecraft:set_written_book_pages', 'set_written_book_pages'] = 'minecraft:set_written_book_pages'
    pages: list[Filterable[Text] | Text]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class LootFunctionSetWrittenBookPagesReplaceSection(Conditions, ReplaceSectionListOperation):
    type: Literal['minecraft:set_written_book_pages', 'set_written_book_pages'] = 'minecraft:set_written_book_pages'
    pages: list[Filterable[Text] | Text]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type LootFunctionSetWrittenBookPages = Annotated[
    Annotated[LootFunctionSetWrittenBookPagesAppend, Tag('minecraft:append')]
    | Annotated[LootFunctionSetWrittenBookPagesInsert, Tag('minecraft:insert')]
    | Annotated[LootFunctionSetWrittenBookPagesReplaceAll, Tag('minecraft:replace_all')]
    | Annotated[LootFunctionSetWrittenBookPagesReplaceSection, Tag('minecraft:replace_section')],
    Discriminator(tag_of('mode')),
]


class LootFunctionToggleTooltips(ToggleTooltips):
    type: Literal['minecraft:toggle_tooltips', 'toggle_tooltips'] = 'minecraft:toggle_tooltips'


type LootFunction = Annotated[
    Annotated[LootFunctionApplyBonus, Tag('minecraft:apply_bonus')]
    | Annotated[LootFunctionCopyComponents, Tag('minecraft:copy_components')]
    | Annotated[LootFunctionCopyCustomData, Tag('minecraft:copy_custom_data')]
    | Annotated[LootFunctionCopyName, Tag('minecraft:copy_name')]
    | Annotated[LootFunctionCopyState, Tag('minecraft:copy_state')]
    | Annotated[LootFunctionDiscard, Tag('minecraft:discard')]
    | Annotated[LootFunctionEnchantRandomly, Tag('minecraft:enchant_randomly')]
    | Annotated[LootFunctionEnchantWithLevels, Tag('minecraft:enchant_with_levels')]
    | Annotated[LootFunctionEnchantedCountIncrease, Tag('minecraft:enchanted_count_increase')]
    | Annotated[LootFunctionExplorationMap, Tag('minecraft:exploration_map')]
    | Annotated[LootFunctionExplosionDecay, Tag('minecraft:explosion_decay')]
    | Annotated[LootFunctionFillPlayerHead, Tag('minecraft:fill_player_head')]
    | Annotated[LootFunctionFiltered, Tag('minecraft:filtered')]
    | Annotated[LootFunctionFurnaceSmelt, Tag('minecraft:furnace_smelt')]
    | Annotated[LootFunctionLimitCount, Tag('minecraft:limit_count')]
    | Annotated[LootFunctionModifyContents, Tag('minecraft:modify_contents')]
    | Annotated[LootFunctionSequence, Tag('minecraft:sequence')]
    | Annotated[LootFunctionSetAttributes, Tag('minecraft:set_attributes')]
    | Annotated[LootFunctionSetBannerPattern, Tag('minecraft:set_banner_pattern')]
    | Annotated[LootFunctionSetBookCover, Tag('minecraft:set_book_cover')]
    | Annotated[LootFunctionSetComponents, Tag('minecraft:set_components')]
    | Annotated[LootFunctionSetContents, Tag('minecraft:set_contents')]
    | Annotated[LootFunctionSetCount, Tag('minecraft:set_count')]
    | Annotated[LootFunctionSetCustomData, Tag('minecraft:set_custom_data')]
    | Annotated[LootFunctionSetCustomModelData, Tag('minecraft:set_custom_model_data')]
    | Annotated[LootFunctionSetDamage, Tag('minecraft:set_damage')]
    | Annotated[LootFunctionSetEnchantments, Tag('minecraft:set_enchantments')]
    | Annotated[LootFunctionSetFireworkExplosion, Tag('minecraft:set_firework_explosion')]
    | Annotated[LootFunctionSetFireworks, Tag('minecraft:set_fireworks')]
    | Annotated[LootFunctionSetInstrument, Tag('minecraft:set_instrument')]
    | Annotated[LootFunctionSetItem, Tag('minecraft:set_item')]
    | Annotated[LootFunctionSetLootTable, Tag('minecraft:set_loot_table')]
    | Annotated[LootFunctionSetLore, Tag('minecraft:set_lore')]
    | Annotated[LootFunctionSetName, Tag('minecraft:set_name')]
    | Annotated[LootFunctionSetOminousBottleAmplifier, Tag('minecraft:set_ominous_bottle_amplifier')]
    | Annotated[LootFunctionSetPotion, Tag('minecraft:set_potion')]
    | Annotated[LootFunctionSetRandomDyes, Tag('minecraft:set_random_dyes')]
    | Annotated[LootFunctionSetRandomPotion, Tag('minecraft:set_random_potion')]
    | Annotated[LootFunctionSetStewEffect, Tag('minecraft:set_stew_effect')]
    | Annotated[LootFunctionSetWritableBookPages, Tag('minecraft:set_writable_book_pages')]
    | Annotated[LootFunctionSetWrittenBookPages, Tag('minecraft:set_written_book_pages')]
    | Annotated[LootFunctionToggleTooltips, Tag('minecraft:toggle_tooltips')],
    Discriminator(tag_of('type')),
]
