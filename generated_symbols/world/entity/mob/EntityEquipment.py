# Generated from symbols.json for ::java::world::entity::mob::EntityEquipment
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.slot.EquipmentSlot import EquipmentSlot
    from generated_symbols.world.item.ItemStack import ItemStack


type EntityEquipment = dict[EquipmentSlot, ItemStack]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::EntityEquipment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::util::slot::EquipmentSlot"
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                }
            }
        ]
    }
}

