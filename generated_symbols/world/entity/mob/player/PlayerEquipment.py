# Generated from symbols.json for ::java::world::entity::mob::player::PlayerEquipment
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.entity.mob.player.PlayerEquipmentSlot import PlayerEquipmentSlot
    from generated_symbols.world.item.ItemStack import ItemStack


type PlayerEquipment = dict[PlayerEquipmentSlot, ItemStack]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::player::PlayerEquipment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::player::PlayerEquipmentSlot"
                },
                "type": {
                    "kind": "reference",
                    "path": "::java::world::item::ItemStack"
                }
            }
        ]
    }
}

