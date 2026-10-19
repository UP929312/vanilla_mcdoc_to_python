"""
Generated from symbols.json for ::java::assets::item_definition::ItemModel
Local link to file: vanilla_mcdoc/assets/item_definition/ItemModel.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.assets.item_definition.BlockState import BlockState
from vanilla_mcdoc.assets.item_definition.ChargeType import ChargeType
from vanilla_mcdoc.assets.item_definition.Compass import Compass
from vanilla_mcdoc.assets.item_definition.ComponentStrings import ComponentStrings
from vanilla_mcdoc.assets.item_definition.Composite import Composite
from vanilla_mcdoc.assets.item_definition.ContextDimension import ContextDimension
from vanilla_mcdoc.assets.item_definition.ContextEntityType import ContextEntityType
from vanilla_mcdoc.assets.item_definition.Count import Count
from vanilla_mcdoc.assets.item_definition.CustomModelDataFlags import CustomModelDataFlags
from vanilla_mcdoc.assets.item_definition.CustomModelDataFloats import CustomModelDataFloats
from vanilla_mcdoc.assets.item_definition.CustomModelDataStrings import CustomModelDataStrings
from vanilla_mcdoc.assets.item_definition.Damage import Damage
from vanilla_mcdoc.assets.item_definition.DisplayContext import DisplayContext
from vanilla_mcdoc.assets.item_definition.HasComponent import HasComponent
from vanilla_mcdoc.assets.item_definition.KeybindDown import KeybindDown
from vanilla_mcdoc.assets.item_definition.LocalTime import LocalTime
from vanilla_mcdoc.assets.item_definition.MainHand import MainHand
from vanilla_mcdoc.assets.item_definition.Model import Model
from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases
from vanilla_mcdoc.assets.item_definition.Special import Special
from vanilla_mcdoc.assets.item_definition.Time import Time
from vanilla_mcdoc.assets.item_definition.TrimMaterial import TrimMaterial
from vanilla_mcdoc.assets.item_definition.UseCycle import UseCycle
from vanilla_mcdoc.assets.item_definition.UseDuration import UseDuration
from vanilla_mcdoc.assets.item_definition.ViewEntity import ViewEntity
from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.minecraft_types import IdSpec, NamespacedId

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.ConditionalPropertyType import ConditionalPropertyType
    from vanilla_mcdoc.assets.item_definition.NumericPropertyType import NumericPropertyType
    from vanilla_mcdoc.assets.item_definition.SelectPropertyType import SelectPropertyType
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


class EntriesStruct(GeneratedModel):
    threshold: float
    model: ItemModel


class ItemModelBundleSelectedItem(GeneratedModel):
    type: Literal['minecraft:bundle/selected_item', 'bundle/selected_item'] = 'minecraft:bundle/selected_item'


class ItemModelComposite(Composite):
    type: Literal['minecraft:composite', 'composite'] = 'minecraft:composite'


class ItemModelConditionUnknown(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: NamespacedId[ConditionalPropertyType]
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionComponentAttributeModifiers(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:attribute_modifiers', 'attribute_modifiers'] = 'minecraft:attribute_modifiers'  # The component predicate to check.
    value: AttributeModifiersPredicate  # The predicate-specific value.


class ItemModelConditionComponentBundleContents(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:bundle_contents', 'bundle_contents'] = 'minecraft:bundle_contents'  # The component predicate to check.
    value: BundleContentsPredicate  # The predicate-specific value.


class ItemModelConditionComponentContainer(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:container', 'container'] = 'minecraft:container'  # The component predicate to check.
    value: ContainerPredicate  # The predicate-specific value.


class ItemModelConditionComponentCustomData(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:custom_data', 'custom_data'] = 'minecraft:custom_data'  # The component predicate to check.
    value: CustomData  # The predicate-specific value.


class ItemModelConditionComponentDamage(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:damage', 'damage'] = 'minecraft:damage'  # The component predicate to check.
    value: ItemDamagePredicate  # The predicate-specific value.


class ItemModelConditionComponentEnchantments(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:enchantments', 'enchantments'] = 'minecraft:enchantments'  # The component predicate to check.
    value: list[EnchantmentPredicate]  # The predicate-specific value.


class ItemModelConditionComponentFireworkExplosion(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:firework_explosion', 'firework_explosion'] = 'minecraft:firework_explosion'  # The component predicate to check.
    value: FireworkExplosionPredicate  # The predicate-specific value.


class ItemModelConditionComponentFireworks(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:fireworks', 'fireworks'] = 'minecraft:fireworks'  # The component predicate to check.
    value: FireworksPredicate  # The predicate-specific value.


class ItemModelConditionComponentJukeboxPlayable(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:jukebox_playable', 'jukebox_playable'] = 'minecraft:jukebox_playable'  # The component predicate to check.
    value: JukeboxPlayablePredicate  # The predicate-specific value.


class ItemModelConditionComponentPotionContents(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:potion_contents', 'potion_contents'] = 'minecraft:potion_contents'  # The component predicate to check.
    value: PotionsPredicate  # The predicate-specific value.


class ItemModelConditionComponentStoredEnchantments(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:stored_enchantments', 'stored_enchantments'] = 'minecraft:stored_enchantments'  # The component predicate to check.
    value: list[EnchantmentPredicate]  # The predicate-specific value.


class ItemModelConditionComponentTrim(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:trim', 'trim'] = 'minecraft:trim'  # The component predicate to check.
    value: TrimPredicate  # The predicate-specific value.


class ItemModelConditionComponentVillagerVariant(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:villager/variant', 'villager/variant'] = 'minecraft:villager/variant'  # The component predicate to check.
    value: Annotated[str, IdSpec(registry='villager_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_type')]]  # The predicate-specific value.


class ItemModelConditionComponentWritableBookContent(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:writable_book_content', 'writable_book_content'] = 'minecraft:writable_book_content'  # The component predicate to check.
    value: WritableBookPredicate  # The predicate-specific value.


class ItemModelConditionComponentWrittenBookContent(GeneratedModel):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None
    predicate: Literal['minecraft:written_book_content', 'written_book_content'] = 'minecraft:written_book_content'  # The component predicate to check.
    value: WrittenBookPredicate  # The predicate-specific value.


type ItemModelConditionComponent = Annotated[
    Annotated[ItemModelConditionComponentAttributeModifiers, Tag('minecraft:attribute_modifiers')]
    | Annotated[ItemModelConditionComponentBundleContents, Tag('minecraft:bundle_contents')]
    | Annotated[ItemModelConditionComponentContainer, Tag('minecraft:container')]
    | Annotated[ItemModelConditionComponentCustomData, Tag('minecraft:custom_data')]
    | Annotated[ItemModelConditionComponentDamage, Tag('minecraft:damage')]
    | Annotated[ItemModelConditionComponentEnchantments, Tag('minecraft:enchantments')]
    | Annotated[ItemModelConditionComponentFireworkExplosion, Tag('minecraft:firework_explosion')]
    | Annotated[ItemModelConditionComponentFireworks, Tag('minecraft:fireworks')]
    | Annotated[ItemModelConditionComponentJukeboxPlayable, Tag('minecraft:jukebox_playable')]
    | Annotated[ItemModelConditionComponentPotionContents, Tag('minecraft:potion_contents')]
    | Annotated[ItemModelConditionComponentStoredEnchantments, Tag('minecraft:stored_enchantments')]
    | Annotated[ItemModelConditionComponentTrim, Tag('minecraft:trim')]
    | Annotated[ItemModelConditionComponentVillagerVariant, Tag('minecraft:villager/variant')]
    | Annotated[ItemModelConditionComponentWritableBookContent, Tag('minecraft:writable_book_content')]
    | Annotated[ItemModelConditionComponentWrittenBookContent, Tag('minecraft:written_book_content')],
    Discriminator(tag_of('predicate')),
]


class ItemModelConditionCustomModelData(CustomModelDataFlags):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionHasComponent(HasComponent):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:has_component', 'has_component'] = 'minecraft:has_component'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionKeybindDown(KeybindDown):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:keybind_down', 'keybind_down'] = 'minecraft:keybind_down'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


class ItemModelConditionViewEntity(ViewEntity):
    type: Literal['minecraft:condition', 'condition'] = 'minecraft:condition'
    property: Literal['minecraft:view_entity', 'view_entity'] = 'minecraft:view_entity'
    on_true: ItemModel
    on_false: ItemModel
    transformation: Transformation | None = None


type ItemModelCondition = ItemModelConditionUnknown | ItemModelConditionComponent | ItemModelConditionCustomModelData | ItemModelConditionHasComponent | ItemModelConditionKeybindDown | ItemModelConditionViewEntity


class ItemModelModel(Model):
    type: Literal['minecraft:model', 'model'] = 'minecraft:model'


class ItemModelRangeDispatchUnknown(GeneratedModel):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: NamespacedId[NumericPropertyType]
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchCompass(Compass):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:compass', 'compass'] = 'minecraft:compass'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchCount(Count):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:count', 'count'] = 'minecraft:count'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchCustomModelData(CustomModelDataFloats):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchDamage(Damage):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:damage', 'damage'] = 'minecraft:damage'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchTime(Time):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:time', 'time'] = 'minecraft:time'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchUseCycle(UseCycle):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:use_cycle', 'use_cycle'] = 'minecraft:use_cycle'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


class ItemModelRangeDispatchUseDuration(UseDuration):
    type: Literal['minecraft:range_dispatch', 'range_dispatch'] = 'minecraft:range_dispatch'
    property: Literal['minecraft:use_duration', 'use_duration'] = 'minecraft:use_duration'
    scale: float | None = None  # Factor to multiply the property value with. Defaults to 1.
    entries: list[EntriesStruct]  # List of ranges. Will select last entry with threshold less or equal to value. Order does not matter, list will be sorted by threshold in ascending order.
    fallback: ItemModel | None = None  # Item model to render if no entries were less or equal to the value.
    transformation: Transformation | None = None


type ItemModelRangeDispatch = ItemModelRangeDispatchUnknown | ItemModelRangeDispatchCompass | ItemModelRangeDispatchCount | ItemModelRangeDispatchCustomModelData | ItemModelRangeDispatchDamage | ItemModelRangeDispatchTime | ItemModelRangeDispatchUseCycle | ItemModelRangeDispatchUseDuration


class ItemModelSelectUnknown(SelectCases[str]):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: NamespacedId[SelectPropertyType]
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectBlockState(BlockState):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:block_state', 'block_state'] = 'minecraft:block_state'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectChargeType(ChargeType):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:charge_type', 'charge_type'] = 'minecraft:charge_type'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectComponent(ComponentStrings):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:component', 'component'] = 'minecraft:component'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectContextDimension(ContextDimension):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:context_dimension', 'context_dimension'] = 'minecraft:context_dimension'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectContextEntityType(ContextEntityType):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:context_entity_type', 'context_entity_type'] = 'minecraft:context_entity_type'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectCustomModelData(CustomModelDataStrings):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:custom_model_data', 'custom_model_data'] = 'minecraft:custom_model_data'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectDisplayContext(DisplayContext):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:display_context', 'display_context'] = 'minecraft:display_context'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectLocalTime(LocalTime):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:local_time', 'local_time'] = 'minecraft:local_time'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectMainHand(MainHand):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:main_hand', 'main_hand'] = 'minecraft:main_hand'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


class ItemModelSelectTrimMaterial(TrimMaterial):
    type: Literal['minecraft:select', 'select'] = 'minecraft:select'
    property: Literal['minecraft:trim_material', 'trim_material'] = 'minecraft:trim_material'
    fallback: ItemModel | None = None  # Item model to render if none of the cases matched the value.
    transformation: Transformation | None = None


type ItemModelSelect = ItemModelSelectUnknown | ItemModelSelectBlockState | ItemModelSelectChargeType | ItemModelSelectComponent | ItemModelSelectContextDimension | ItemModelSelectContextEntityType | ItemModelSelectCustomModelData | ItemModelSelectDisplayContext | ItemModelSelectLocalTime | ItemModelSelectMainHand | ItemModelSelectTrimMaterial


class ItemModelSpecial(Special):
    type: Literal['minecraft:special', 'special'] = 'minecraft:special'


type ItemModel = Annotated[
    Annotated[ItemModelBundleSelectedItem, Tag('minecraft:bundle/selected_item')]
    | Annotated[ItemModelComposite, Tag('minecraft:composite')]
    | Annotated[ItemModelCondition, Tag('minecraft:condition')]
    | Annotated[ItemModelModel, Tag('minecraft:model')]
    | Annotated[ItemModelRangeDispatch, Tag('minecraft:range_dispatch')]
    | Annotated[ItemModelSelect, Tag('minecraft:select')]
    | Annotated[ItemModelSpecial, Tag('minecraft:special')],
    Discriminator(tag_of('type')),
]
