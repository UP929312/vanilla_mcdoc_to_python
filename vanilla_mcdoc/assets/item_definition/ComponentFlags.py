"""
Generated from symbols.json for ::java::assets::item_definition::ComponentFlags
Local link to file: vanilla_mcdoc/assets/item_definition/ComponentFlags.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
    from vanilla_mcdoc.world.component.CustomData import CustomData
    from vanilla_mcdoc.world.component.predicate.AttributeModifiersPredicate import AttributeModifiersPredicate
    from vanilla_mcdoc.world.component.predicate.BundleContentsPredicate import BundleContentsPredicate
    from vanilla_mcdoc.world.component.predicate.ContainerPredicate import ContainerPredicate
    from vanilla_mcdoc.world.component.predicate.FireworkExplosionPredicate import FireworkExplosionPredicate
    from vanilla_mcdoc.world.component.predicate.FireworksPredicate import FireworksPredicate
    from vanilla_mcdoc.world.component.predicate.ItemDamagePredicate import ItemDamagePredicate
    from vanilla_mcdoc.world.component.predicate.JukeboxPlayablePredicate import JukeboxPlayablePredicate
    from vanilla_mcdoc.world.component.predicate.PotionsPredicate import PotionsPredicate
    from vanilla_mcdoc.world.component.predicate.TrimPredicate import TrimPredicate
    from vanilla_mcdoc.world.component.predicate.WritableBookPredicate import WritableBookPredicate
    from vanilla_mcdoc.world.component.predicate.WrittenBookPredicate import WrittenBookPredicate


class ComponentFlagsAttributeModifiers(GeneratedModel):
    predicate: Literal['minecraft:attribute_modifiers', 'attribute_modifiers'] = 'minecraft:attribute_modifiers'  # The component predicate to check.
    value: AttributeModifiersPredicate  # The predicate-specific value.


class ComponentFlagsBundleContents(GeneratedModel):
    predicate: Literal['minecraft:bundle_contents', 'bundle_contents'] = 'minecraft:bundle_contents'  # The component predicate to check.
    value: BundleContentsPredicate  # The predicate-specific value.


class ComponentFlagsContainer(GeneratedModel):
    predicate: Literal['minecraft:container', 'container'] = 'minecraft:container'  # The component predicate to check.
    value: ContainerPredicate  # The predicate-specific value.


class ComponentFlagsCustomData(GeneratedModel):
    predicate: Literal['minecraft:custom_data', 'custom_data'] = 'minecraft:custom_data'  # The component predicate to check.
    value: CustomData  # The predicate-specific value.


class ComponentFlagsDamage(GeneratedModel):
    predicate: Literal['minecraft:damage', 'damage'] = 'minecraft:damage'  # The component predicate to check.
    value: ItemDamagePredicate  # The predicate-specific value.


class ComponentFlagsEnchantments(GeneratedModel):
    predicate: Literal['minecraft:enchantments', 'enchantments'] = 'minecraft:enchantments'  # The component predicate to check.
    value: list[EnchantmentPredicate]  # The predicate-specific value.


class ComponentFlagsFireworkExplosion(GeneratedModel):
    predicate: Literal['minecraft:firework_explosion', 'firework_explosion'] = 'minecraft:firework_explosion'  # The component predicate to check.
    value: FireworkExplosionPredicate  # The predicate-specific value.


class ComponentFlagsFireworks(GeneratedModel):
    predicate: Literal['minecraft:fireworks', 'fireworks'] = 'minecraft:fireworks'  # The component predicate to check.
    value: FireworksPredicate  # The predicate-specific value.


class ComponentFlagsJukeboxPlayable(GeneratedModel):
    predicate: Literal['minecraft:jukebox_playable', 'jukebox_playable'] = 'minecraft:jukebox_playable'  # The component predicate to check.
    value: JukeboxPlayablePredicate  # The predicate-specific value.


class ComponentFlagsPotionContents(GeneratedModel):
    predicate: Literal['minecraft:potion_contents', 'potion_contents'] = 'minecraft:potion_contents'  # The component predicate to check.
    value: PotionsPredicate  # The predicate-specific value.


class ComponentFlagsStoredEnchantments(GeneratedModel):
    predicate: Literal['minecraft:stored_enchantments', 'stored_enchantments'] = 'minecraft:stored_enchantments'  # The component predicate to check.
    value: list[EnchantmentPredicate]  # The predicate-specific value.


class ComponentFlagsTrim(GeneratedModel):
    predicate: Literal['minecraft:trim', 'trim'] = 'minecraft:trim'  # The component predicate to check.
    value: TrimPredicate  # The predicate-specific value.


class ComponentFlagsVillagerVariant(GeneratedModel):
    predicate: Literal['minecraft:villager/variant', 'villager/variant'] = 'minecraft:villager/variant'  # The component predicate to check.
    value: Annotated[str, IdSpec(registry='villager_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_type')]]  # The predicate-specific value.


class ComponentFlagsWritableBookContent(GeneratedModel):
    predicate: Literal['minecraft:writable_book_content', 'writable_book_content'] = 'minecraft:writable_book_content'  # The component predicate to check.
    value: WritableBookPredicate  # The predicate-specific value.


class ComponentFlagsWrittenBookContent(GeneratedModel):
    predicate: Literal['minecraft:written_book_content', 'written_book_content'] = 'minecraft:written_book_content'  # The component predicate to check.
    value: WrittenBookPredicate  # The predicate-specific value.


type ComponentFlags = Annotated[
    Annotated[ComponentFlagsAttributeModifiers, Tag('minecraft:attribute_modifiers')]
    | Annotated[ComponentFlagsBundleContents, Tag('minecraft:bundle_contents')]
    | Annotated[ComponentFlagsContainer, Tag('minecraft:container')]
    | Annotated[ComponentFlagsCustomData, Tag('minecraft:custom_data')]
    | Annotated[ComponentFlagsDamage, Tag('minecraft:damage')]
    | Annotated[ComponentFlagsEnchantments, Tag('minecraft:enchantments')]
    | Annotated[ComponentFlagsFireworkExplosion, Tag('minecraft:firework_explosion')]
    | Annotated[ComponentFlagsFireworks, Tag('minecraft:fireworks')]
    | Annotated[ComponentFlagsJukeboxPlayable, Tag('minecraft:jukebox_playable')]
    | Annotated[ComponentFlagsPotionContents, Tag('minecraft:potion_contents')]
    | Annotated[ComponentFlagsStoredEnchantments, Tag('minecraft:stored_enchantments')]
    | Annotated[ComponentFlagsTrim, Tag('minecraft:trim')]
    | Annotated[ComponentFlagsVillagerVariant, Tag('minecraft:villager/variant')]
    | Annotated[ComponentFlagsWritableBookContent, Tag('minecraft:writable_book_content')]
    | Annotated[ComponentFlagsWrittenBookContent, Tag('minecraft:written_book_content')],
    Discriminator(tag_of('predicate')),
]
