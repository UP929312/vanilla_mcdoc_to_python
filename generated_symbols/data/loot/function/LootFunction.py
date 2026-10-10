"""
Generated from symbols.json for ::java::data::loot::function::LootFunction
Local link to file: generated_symbols/data/loot/function/LootFunction.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from generated_symbols.data.loot.function.BinomialWithBonusCountFormula import BinomialWithBonusCountFormula
from generated_symbols.data.loot.function.Conditions import Conditions
from generated_symbols.data.loot.function.CopyComponents import CopyComponents
from generated_symbols.data.loot.function.CopyName import CopyName
from generated_symbols.data.loot.function.CopyNbt import CopyNbt
from generated_symbols.data.loot.function.CopyState import CopyState
from generated_symbols.data.loot.function.EnchantRandomly import EnchantRandomly
from generated_symbols.data.loot.function.EnchantWithLevels import EnchantWithLevels
from generated_symbols.data.loot.function.EnchantedCountIncrease import EnchantedCountIncrease
from generated_symbols.data.loot.function.ExplorationMap import ExplorationMap
from generated_symbols.data.loot.function.FillPlayerHead import FillPlayerHead
from generated_symbols.data.loot.function.Filtered import Filtered
from generated_symbols.data.loot.function.InsertListOperation import InsertListOperation
from generated_symbols.data.loot.function.LimitCount import LimitCount
from generated_symbols.data.loot.function.ModifyContents import ModifyContents
from generated_symbols.data.loot.function.ReplaceSectionListOperation import ReplaceSectionListOperation
from generated_symbols.data.loot.function.Sequence import Sequence
from generated_symbols.data.loot.function.SetAttributes import SetAttributes
from generated_symbols.data.loot.function.SetBannerPattern import SetBannerPattern
from generated_symbols.data.loot.function.SetBookCover import SetBookCover
from generated_symbols.data.loot.function.SetComponents import SetComponents
from generated_symbols.data.loot.function.SetContents import SetContents
from generated_symbols.data.loot.function.SetCount import SetCount
from generated_symbols.data.loot.function.SetCustomData import SetCustomData
from generated_symbols.data.loot.function.SetCustomModelData import SetCustomModelData
from generated_symbols.data.loot.function.SetDamage import SetDamage
from generated_symbols.data.loot.function.SetEnchantments import SetEnchantments
from generated_symbols.data.loot.function.SetFireworkExplosion import SetFireworkExplosion
from generated_symbols.data.loot.function.SetFireworks import SetFireworks
from generated_symbols.data.loot.function.SetInstrument import SetInstrument
from generated_symbols.data.loot.function.SetItem import SetItem
from generated_symbols.data.loot.function.SetLootTable import SetLootTable
from generated_symbols.data.loot.function.SetName import SetName
from generated_symbols.data.loot.function.SetOminousBottleAmplifier import SetOminousBottleAmplifier
from generated_symbols.data.loot.function.SetPotion import SetPotion
from generated_symbols.data.loot.function.SetRandomDyes import SetRandomDyes
from generated_symbols.data.loot.function.SetRandomPotion import SetRandomPotion
from generated_symbols.data.loot.function.SetStewEffect import SetStewEffect
from generated_symbols.data.loot.function.ToggleTooltips import ToggleTooltips
from generated_symbols.data.loot.function.UniformBonusFormula import UniformBonusFormula
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget
    from generated_symbols.util.Filterable import Filterable
    from generated_symbols.util.text.Text import Text


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
    LootFunctionApplyBonusBinomialWithBonusCount | LootFunctionApplyBonusOreDrops | LootFunctionApplyBonusUniformBonusCount,
    Field(discriminator='formula'),
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
    LootFunctionSetLoreAppend | LootFunctionSetLoreInsert | LootFunctionSetLoreReplaceAll | LootFunctionSetLoreReplaceSection,
    Field(discriminator='mode'),
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
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class LootFunctionSetWritableBookPagesInsert(Conditions, InsertListOperation):
    type: Literal['minecraft:set_writable_book_pages', 'set_writable_book_pages'] = 'minecraft:set_writable_book_pages'
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class LootFunctionSetWritableBookPagesReplaceAll(Conditions):
    type: Literal['minecraft:set_writable_book_pages', 'set_writable_book_pages'] = 'minecraft:set_writable_book_pages'
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class LootFunctionSetWritableBookPagesReplaceSection(Conditions, ReplaceSectionListOperation):
    type: Literal['minecraft:set_writable_book_pages', 'set_writable_book_pages'] = 'minecraft:set_writable_book_pages'
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type LootFunctionSetWritableBookPages = Annotated[
    LootFunctionSetWritableBookPagesAppend | LootFunctionSetWritableBookPagesInsert | LootFunctionSetWritableBookPagesReplaceAll | LootFunctionSetWritableBookPagesReplaceSection,
    Field(discriminator='mode'),
]

class LootFunctionSetWrittenBookPagesAppend(Conditions):
    type: Literal['minecraft:set_written_book_pages', 'set_written_book_pages'] = 'minecraft:set_written_book_pages'
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:append', 'append'] = 'minecraft:append'  # Determines how the existing list should be modified.


class LootFunctionSetWrittenBookPagesInsert(Conditions, InsertListOperation):
    type: Literal['minecraft:set_written_book_pages', 'set_written_book_pages'] = 'minecraft:set_written_book_pages'
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:insert', 'insert'] = 'minecraft:insert'  # Determines how the existing list should be modified.


class LootFunctionSetWrittenBookPagesReplaceAll(Conditions):
    type: Literal['minecraft:set_written_book_pages', 'set_written_book_pages'] = 'minecraft:set_written_book_pages'
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_all', 'replace_all'] = 'minecraft:replace_all'  # Determines how the existing list should be modified.


class LootFunctionSetWrittenBookPagesReplaceSection(Conditions, ReplaceSectionListOperation):
    type: Literal['minecraft:set_written_book_pages', 'set_written_book_pages'] = 'minecraft:set_written_book_pages'
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_section', 'replace_section'] = 'minecraft:replace_section'  # Determines how the existing list should be modified.


type LootFunctionSetWrittenBookPages = Annotated[
    LootFunctionSetWrittenBookPagesAppend | LootFunctionSetWrittenBookPagesInsert | LootFunctionSetWrittenBookPagesReplaceAll | LootFunctionSetWrittenBookPagesReplaceSection,
    Field(discriminator='mode'),
]

class LootFunctionToggleTooltips(ToggleTooltips):
    type: Literal['minecraft:toggle_tooltips', 'toggle_tooltips'] = 'minecraft:toggle_tooltips'


type LootFunction = Annotated[
    LootFunctionApplyBonus | LootFunctionCopyComponents | LootFunctionCopyCustomData | LootFunctionCopyName | LootFunctionCopyState | LootFunctionDiscard | LootFunctionEnchantRandomly | LootFunctionEnchantWithLevels | LootFunctionEnchantedCountIncrease | LootFunctionExplorationMap | LootFunctionExplosionDecay | LootFunctionFillPlayerHead | LootFunctionFiltered | LootFunctionFurnaceSmelt | LootFunctionLimitCount | LootFunctionModifyContents | LootFunctionSequence | LootFunctionSetAttributes | LootFunctionSetBannerPattern | LootFunctionSetBookCover | LootFunctionSetComponents | LootFunctionSetContents | LootFunctionSetCount | LootFunctionSetCustomData | LootFunctionSetCustomModelData | LootFunctionSetDamage | LootFunctionSetEnchantments | LootFunctionSetFireworkExplosion | LootFunctionSetFireworks | LootFunctionSetInstrument | LootFunctionSetItem | LootFunctionSetLootTable | LootFunctionSetLore | LootFunctionSetName | LootFunctionSetOminousBottleAmplifier | LootFunctionSetPotion | LootFunctionSetRandomDyes | LootFunctionSetRandomPotion | LootFunctionSetStewEffect | LootFunctionSetWritableBookPages | LootFunctionSetWrittenBookPages | LootFunctionToggleTooltips,
    Field(discriminator='type'),
]


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

