# Generated from symbols.json for ::java::world::component::item::Consumable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.world.component.item.ConsumeEffect import ConsumeEffect
    from generated_symbols.world.component.item.ItemUseAnimation import ItemUseAnimation


@dataclass(kw_only=True)
class Consumable:
    consume_seconds: Annotated[float, 'Range | Min `0` and above | inclusive'] | None = None  # Time taken for a player to consume the item. Defaults to 1.6.
    animation: ItemUseAnimation | None = None  # View model/arms animation used during consumption of the item. Defaults to `eat`.
    sound: SoundEventRef | None = None  # Sound played during and on completion of item consumption.
    has_consume_particles: bool | None = None  # Whether the `item` particle is emitted while consuming the item. Defaults to `true`.
    on_consume_effects: list[ConsumeEffect] | None = None  # Side effects which take place after consuming the item.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::Consumable": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Time taken for a player to consume the item. Defaults to 1.6.",
                "key": "consume_seconds",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "View model/arms animation used during consumption of the item. Defaults to `eat`.",
                "key": "animation",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::ItemUseAnimation"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Sound played during and on completion of item consumption.",
                "key": "sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the `item` particle is emitted while consuming the item. Defaults to `True`.",
                "key": "has_consume_particles",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Side effects which take place after consuming the item.",
                "key": "on_consume_effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::component::item::ConsumeEffect"
                    }
                },
                "optional": True
            }
        ]
    }
}

