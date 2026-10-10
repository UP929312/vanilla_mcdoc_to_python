"""
Generated from symbols.json for ::java::world::item::ItemBase
Local link to file: vanilla_mcdoc/world/item/ItemBase.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Any

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.world.component.item.Trim import Trim
    from vanilla_mcdoc.world.item.AttributeModifier import AttributeModifier
    from vanilla_mcdoc.world.item.Display import Display
    from vanilla_mcdoc.world.item.Enchantment import Enchantment


class ItemBase(GeneratedModel):
    Damage: int | None = None  # Damage that an item has. Only used for tools, armor, etc.
    Unbreakable: bool | None = None  # Whether the item should be unbreakable. Only used for tools, armor, etc.
    CanDestroy: list[str] | None = None  # List of the block states that can be destroyed by this item when holding it in adventure mode.
    CanPlaceOn: list[str] | None = None  # List of blockstates that this block item can be placed on.
    CustomModelData: int | None = None  # Tag that describes the custom model an item will take. Used by the `custom_model_data` model overrides predicate. Has certain restrictions due to float conversion.
    Enchantments: list[Enchantment] | None = None  # List of enchantments that are on the item.
    RepairCost: int | None = None  # Number of experience levels to add to the base level cost when repairing, combining, or renaming this item with an anvil.
    AttributeModifiers: list[AttributeModifier] | None = None  # Applied to an entity that has equipped the item.
    display: Display | None = None  # Display settings.
    HideFlags: int | None = None  # Bitfield for which flags to hide on an item.
    Trim_: Trim | None = Field(default=None, alias='Trim')  # Trim to apply to the item & armor when worn.
    key_name: Any  # Custom item NBT tags
