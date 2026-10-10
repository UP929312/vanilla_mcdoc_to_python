"""
Generated from symbols.json for ::java::assets::item_definition::ComponentFlags
Local link to file: vanilla_mcdoc/assets/item_definition/ComponentFlags.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
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


class ComponentFlags(GeneratedModel):
    predicate: Annotated[str, IdSpec(registry='data_component_predicate_type')]  # The component predicate to check.
    value: None | AttributeModifiersPredicate | BundleContentsPredicate | ContainerPredicate | CustomData | ItemDamagePredicate | list[EnchantmentPredicate] | FireworkExplosionPredicate | FireworksPredicate | JukeboxPlayablePredicate | PotionsPredicate | TrimPredicate | Annotated[str, IdSpec(registry='villager_type', tags='allowed')] | list[Annotated[str, IdSpec(registry='villager_type')]] | WritableBookPredicate | WrittenBookPredicate  # The predicate-specific value.
