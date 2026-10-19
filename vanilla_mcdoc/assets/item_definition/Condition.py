"""
Generated from symbols.json for ::java::assets::item_definition::Condition
Local link to file: vanilla_mcdoc/assets/item_definition/Condition.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.assets.item_definition.CustomModelDataFlags import CustomModelDataFlags
from vanilla_mcdoc.assets.item_definition.HasComponent import HasComponent
from vanilla_mcdoc.assets.item_definition.KeybindDown import KeybindDown
from vanilla_mcdoc.assets.item_definition.ViewEntity import ViewEntity
from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.minecraft_types import IdSpec, NamespacedId

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from vanilla_mcdoc.assets.item_definition.ItemModel import ItemModel
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
    from vanilla_mcdoc.world.entity.display.Transformation import Transformation


class ConditionUnknown(GeneratedModel):
    property: NamespacedId[ConditionalPropertyType]
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionComponentAttributeModifiers(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:attribute_modifiers', 'attribute_modifiers'] = 'minecraft:attribute_modifiers'  # The component predicate to check.
    value: AttributeModifiersPredicate  # The predicate-specific value.


class ConditionComponentBundleContents(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:bundle_contents', 'bundle_contents'] = 'minecraft:bundle_contents'  # The component predicate to check.
    value: BundleContentsPredicate  # The predicate-specific value.


class ConditionComponentContainer(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:container', 'container'] = 'minecraft:container'  # The component predicate to check.
    value: ContainerPredicate  # The predicate-specific value.


class ConditionComponentCustomData(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:custom_data', 'custom_data'] = 'minecraft:custom_data'  # The component predicate to check.
    value: CustomData  # The predicate-specific value.


class ConditionComponentDamage(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:damage', 'damage'] = 'minecraft:damage'  # The component predicate to check.
    value: ItemDamagePredicate  # The predicate-specific value.


class ConditionComponentEnchantments(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:enchantments', 'enchantments'] = 'minecraft:enchantments'  # The component predicate to check.
    value: list[EnchantmentPredicate]  # The predicate-specific value.


class ConditionComponentFireworkExplosion(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:firework_explosion', 'firework_explosion'] = 'minecraft:firework_explosion'  # The component predicate to check.
    value: FireworkExplosionPredicate  # The predicate-specific value.


class ConditionComponentFireworks(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:fireworks', 'fireworks'] = 'minecraft:fireworks'  # The component predicate to check.
    value: FireworksPredicate  # The predicate-specific value.


class ConditionComponentJukeboxPlayable(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:jukebox_playable', 'jukebox_playable'] = 'minecraft:jukebox_playable'  # The component predicate to check.
    value: JukeboxPlayablePredicate  # The predicate-specific value.


class ConditionComponentPotionContents(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:potion_contents', 'potion_contents'] = 'minecraft:potion_contents'  # The component predicate to check.
    value: PotionsPredicate  # The predicate-specific value.


class ConditionComponentStoredEnchantments(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:stored_enchantments', 'stored_enchantments'] = 'minecraft:stored_enchantments'  # The component predicate to check.
    value: list[EnchantmentPredicate]  # The predicate-specific value.


class ConditionComponentTrim(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:trim', 'trim'] = 'minecraft:trim'  # The component predicate to check.
    value: TrimPredicate  # The predicate-specific value.


class ConditionComponentVillagerVariant(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:villager/variant', 'villager/variant'] = 'minecraft:villager/variant'  # The component predicate to check.
    value: Annotated[str, IdSpec(registry='villager_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_type')]]  # The predicate-specific value.


class ConditionComponentWritableBookContent(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:writable_book_content', 'writable_book_content'] = 'minecraft:writable_book_content'  # The component predicate to check.
    value: WritableBookPredicate  # The predicate-specific value.


class ConditionComponentWrittenBookContent(GeneratedModel):
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:written_book_content', 'written_book_content'] = 'minecraft:written_book_content'  # The component predicate to check.
    value: WrittenBookPredicate  # The predicate-specific value.


type ConditionComponent = Annotated[
    Annotated[ConditionComponentAttributeModifiers, Tag('minecraft:attribute_modifiers')]
    | Annotated[ConditionComponentBundleContents, Tag('minecraft:bundle_contents')]
    | Annotated[ConditionComponentContainer, Tag('minecraft:container')]
    | Annotated[ConditionComponentCustomData, Tag('minecraft:custom_data')]
    | Annotated[ConditionComponentDamage, Tag('minecraft:damage')]
    | Annotated[ConditionComponentEnchantments, Tag('minecraft:enchantments')]
    | Annotated[ConditionComponentFireworkExplosion, Tag('minecraft:firework_explosion')]
    | Annotated[ConditionComponentFireworks, Tag('minecraft:fireworks')]
    | Annotated[ConditionComponentJukeboxPlayable, Tag('minecraft:jukebox_playable')]
    | Annotated[ConditionComponentPotionContents, Tag('minecraft:potion_contents')]
    | Annotated[ConditionComponentStoredEnchantments, Tag('minecraft:stored_enchantments')]
    | Annotated[ConditionComponentTrim, Tag('minecraft:trim')]
    | Annotated[ConditionComponentVillagerVariant, Tag('minecraft:villager/variant')]
    | Annotated[ConditionComponentWritableBookContent, Tag('minecraft:writable_book_content')]
    | Annotated[ConditionComponentWrittenBookContent, Tag('minecraft:written_book_content')],
    Discriminator(tag_of('predicate')),
]


class ConditionCustomModelData(CustomModelDataFlags):
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionHasComponent(HasComponent):
    property: Literal['minecraft:has_component', 'has_component'] = 'minecraft:has_component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionKeybindDown(KeybindDown):
    property: Literal['minecraft:keybind_down', 'keybind_down'] = 'minecraft:keybind_down'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ConditionViewEntity(ViewEntity):
    property: Literal['minecraft:view_entity', 'view_entity'] = 'minecraft:view_entity'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


type Condition = ConditionUnknown | ConditionComponent | ConditionCustomModelData | ConditionHasComponent | ConditionKeybindDown | ConditionViewEntity
