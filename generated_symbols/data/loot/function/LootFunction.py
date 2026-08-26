"""
Generated from symbols.json for ::java::data::loot::function::LootFunction
Local link to file: generated_symbols/data/loot/function/LootFunction.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

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


@dataclass(kw_only=True)
class LootFunctionApplyBonusBinomialWithBonusCount(BinomialWithBonusCountFormula, Conditions):
    type: Literal['minecraft:apply_bonus']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:binomial_with_bonus_count']


@dataclass(kw_only=True)
class LootFunctionApplyBonusOreDrops(Conditions):
    type: Literal['minecraft:apply_bonus']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:ore_drops']


@dataclass(kw_only=True)
class LootFunctionApplyBonusUniformBonusCount(Conditions, UniformBonusFormula):
    type: Literal['minecraft:apply_bonus']
    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    formula: Literal['minecraft:uniform_bonus_count']


type LootFunctionApplyBonus = LootFunctionApplyBonusBinomialWithBonusCount | LootFunctionApplyBonusOreDrops | LootFunctionApplyBonusUniformBonusCount

@dataclass(kw_only=True)
class LootFunctionCopyComponents(CopyComponents):
    type: Literal['minecraft:copy_components']


@dataclass(kw_only=True)
class LootFunctionCopyCustomData(CopyNbt):
    type: Literal['minecraft:copy_custom_data']


@dataclass(kw_only=True)
class LootFunctionCopyName(CopyName):
    type: Literal['minecraft:copy_name']


@dataclass(kw_only=True)
class LootFunctionCopyState(CopyState):
    type: Literal['minecraft:copy_state']


@dataclass(kw_only=True)
class LootFunctionDiscard(Conditions):
    type: Literal['minecraft:discard']


@dataclass(kw_only=True)
class LootFunctionEnchantRandomly(EnchantRandomly):
    type: Literal['minecraft:enchant_randomly']


@dataclass(kw_only=True)
class LootFunctionEnchantWithLevels(EnchantWithLevels):
    type: Literal['minecraft:enchant_with_levels']


@dataclass(kw_only=True)
class LootFunctionEnchantedCountIncrease(EnchantedCountIncrease):
    type: Literal['minecraft:enchanted_count_increase']


@dataclass(kw_only=True)
class LootFunctionExplorationMap(ExplorationMap):
    type: Literal['minecraft:exploration_map']


@dataclass(kw_only=True)
class LootFunctionExplosionDecay(Conditions):
    type: Literal['minecraft:explosion_decay']


@dataclass(kw_only=True)
class LootFunctionFillPlayerHead(FillPlayerHead):
    type: Literal['minecraft:fill_player_head']


@dataclass(kw_only=True)
class LootFunctionFiltered(Filtered):
    type: Literal['minecraft:filtered']


@dataclass(kw_only=True)
class LootFunctionFurnaceSmelt(Conditions):
    type: Literal['minecraft:furnace_smelt']


@dataclass(kw_only=True)
class LootFunctionLimitCount(LimitCount):
    type: Literal['minecraft:limit_count']


@dataclass(kw_only=True)
class LootFunctionModifyContents(ModifyContents):
    type: Literal['minecraft:modify_contents']


@dataclass(kw_only=True)
class LootFunctionSequence(Sequence):
    type: Literal['minecraft:sequence']


@dataclass(kw_only=True)
class LootFunctionSetAttributes(SetAttributes):
    type: Literal['minecraft:set_attributes']


@dataclass(kw_only=True)
class LootFunctionSetBannerPattern(SetBannerPattern):
    type: Literal['minecraft:set_banner_pattern']


@dataclass(kw_only=True)
class LootFunctionSetBookCover(SetBookCover):
    type: Literal['minecraft:set_book_cover']


@dataclass(kw_only=True)
class LootFunctionSetComponents(SetComponents):
    type: Literal['minecraft:set_components']


@dataclass(kw_only=True)
class LootFunctionSetContents(SetContents):
    type: Literal['minecraft:set_contents']


@dataclass(kw_only=True)
class LootFunctionSetCount(SetCount):
    type: Literal['minecraft:set_count']


@dataclass(kw_only=True)
class LootFunctionSetCustomData(SetCustomData):
    type: Literal['minecraft:set_custom_data']


@dataclass(kw_only=True)
class LootFunctionSetCustomModelData(SetCustomModelData):
    type: Literal['minecraft:set_custom_model_data']


@dataclass(kw_only=True)
class LootFunctionSetDamage(SetDamage):
    type: Literal['minecraft:set_damage']


@dataclass(kw_only=True)
class LootFunctionSetEnchantments(SetEnchantments):
    type: Literal['minecraft:set_enchantments']


@dataclass(kw_only=True)
class LootFunctionSetFireworkExplosion(SetFireworkExplosion):
    type: Literal['minecraft:set_firework_explosion']


@dataclass(kw_only=True)
class LootFunctionSetFireworks(SetFireworks):
    type: Literal['minecraft:set_fireworks']


@dataclass(kw_only=True)
class LootFunctionSetInstrument(SetInstrument):
    type: Literal['minecraft:set_instrument']


@dataclass(kw_only=True)
class LootFunctionSetItem(SetItem):
    type: Literal['minecraft:set_item']


@dataclass(kw_only=True)
class LootFunctionSetLootTable(SetLootTable):
    type: Literal['minecraft:set_loot_table']


@dataclass(kw_only=True)
class LootFunctionSetLoreAppend(Conditions):
    type: Literal['minecraft:set_lore']
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetLoreInsert(Conditions, InsertListOperation):
    type: Literal['minecraft:set_lore']
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetLoreReplaceAll(Conditions):
    type: Literal['minecraft:set_lore']
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetLoreReplaceSection(Conditions, ReplaceSectionListOperation):
    type: Literal['minecraft:set_lore']
    entity: EntityTarget | None = None  # The entity used to resolve the text components.
    lore: list[Text]
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.


type LootFunctionSetLore = LootFunctionSetLoreAppend | LootFunctionSetLoreInsert | LootFunctionSetLoreReplaceAll | LootFunctionSetLoreReplaceSection

@dataclass(kw_only=True)
class LootFunctionSetName(SetName):
    type: Literal['minecraft:set_name']


@dataclass(kw_only=True)
class LootFunctionSetOminousBottleAmplifier(SetOminousBottleAmplifier):
    type: Literal['minecraft:set_ominous_bottle_amplifier']


@dataclass(kw_only=True)
class LootFunctionSetPotion(SetPotion):
    type: Literal['minecraft:set_potion']


@dataclass(kw_only=True)
class LootFunctionSetRandomDyes(SetRandomDyes):
    type: Literal['minecraft:set_random_dyes']


@dataclass(kw_only=True)
class LootFunctionSetRandomPotion(SetRandomPotion):
    type: Literal['minecraft:set_random_potion']


@dataclass(kw_only=True)
class LootFunctionSetStewEffect(SetStewEffect):
    type: Literal['minecraft:set_stew_effect']


@dataclass(kw_only=True)
class LootFunctionSetWritableBookPagesAppend(Conditions):
    type: Literal['minecraft:set_writable_book_pages']
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWritableBookPagesInsert(Conditions, InsertListOperation):
    type: Literal['minecraft:set_writable_book_pages']
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWritableBookPagesReplaceAll(Conditions):
    type: Literal['minecraft:set_writable_book_pages']
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWritableBookPagesReplaceSection(Conditions, ReplaceSectionListOperation):
    type: Literal['minecraft:set_writable_book_pages']
    pages: list[Filterable[str]]  # Sets the pages of a book and quill.
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.


type LootFunctionSetWritableBookPages = LootFunctionSetWritableBookPagesAppend | LootFunctionSetWritableBookPagesInsert | LootFunctionSetWritableBookPagesReplaceAll | LootFunctionSetWritableBookPagesReplaceSection

@dataclass(kw_only=True)
class LootFunctionSetWrittenBookPagesAppend(Conditions):
    type: Literal['minecraft:set_written_book_pages']
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:append']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWrittenBookPagesInsert(Conditions, InsertListOperation):
    type: Literal['minecraft:set_written_book_pages']
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:insert']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWrittenBookPagesReplaceAll(Conditions):
    type: Literal['minecraft:set_written_book_pages']
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_all']  # Determines how the existing list should be modified.


@dataclass(kw_only=True)
class LootFunctionSetWrittenBookPagesReplaceSection(Conditions, ReplaceSectionListOperation):
    type: Literal['minecraft:set_written_book_pages']
    pages: list[Filterable[Text]]  # Sets the pages of a written book.
    mode: Literal['minecraft:replace_section']  # Determines how the existing list should be modified.


type LootFunctionSetWrittenBookPages = LootFunctionSetWrittenBookPagesAppend | LootFunctionSetWrittenBookPagesInsert | LootFunctionSetWrittenBookPagesReplaceAll | LootFunctionSetWrittenBookPagesReplaceSection

@dataclass(kw_only=True)
class LootFunctionToggleTooltips(ToggleTooltips):
    type: Literal['minecraft:toggle_tooltips']


type LootFunction = LootFunctionApplyBonus | LootFunctionCopyComponents | LootFunctionCopyCustomData | LootFunctionCopyName | LootFunctionCopyState | LootFunctionDiscard | LootFunctionEnchantRandomly | LootFunctionEnchantWithLevels | LootFunctionEnchantedCountIncrease | LootFunctionExplorationMap | LootFunctionExplosionDecay | LootFunctionFillPlayerHead | LootFunctionFiltered | LootFunctionFurnaceSmelt | LootFunctionLimitCount | LootFunctionModifyContents | LootFunctionSequence | LootFunctionSetAttributes | LootFunctionSetBannerPattern | LootFunctionSetBookCover | LootFunctionSetComponents | LootFunctionSetContents | LootFunctionSetCount | LootFunctionSetCustomData | LootFunctionSetCustomModelData | LootFunctionSetDamage | LootFunctionSetEnchantments | LootFunctionSetFireworkExplosion | LootFunctionSetFireworks | LootFunctionSetInstrument | LootFunctionSetItem | LootFunctionSetLootTable | LootFunctionSetLore | LootFunctionSetName | LootFunctionSetOminousBottleAmplifier | LootFunctionSetPotion | LootFunctionSetRandomDyes | LootFunctionSetRandomPotion | LootFunctionSetStewEffect | LootFunctionSetWritableBookPages | LootFunctionSetWrittenBookPages | LootFunctionToggleTooltips


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

