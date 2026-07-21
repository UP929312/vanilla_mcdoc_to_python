# Generated from symbols.json for ::java::world::component::item::DeathProtection
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.item.ConsumeEffect import ConsumeEffect


@dataclass(kw_only=True)
class DeathProtection:
    death_effects: list[ConsumeEffect] | None = None  # Effects applied when the item protects the holder.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::DeathProtection": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Effects applied when the item protects the holder.",
                "key": "death_effects",
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

