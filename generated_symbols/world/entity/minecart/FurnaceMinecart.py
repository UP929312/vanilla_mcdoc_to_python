# Generated from symbols.json for ::java::world::entity::minecart::FurnaceMinecart
from dataclasses import dataclass
from generated_symbols.world.entity.minecart.Minecart import Minecart


@dataclass(kw_only=True)
class FurnaceMinecart(Minecart):
    PushX: float | None = None  # Acceleration in x axis.
    PushZ: float | None = None  # Acceleration in z axis.
    Fuel: int | None = None  # Ticks until the fuel runs out.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::minecart::FurnaceMinecart": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::minecart::Minecart"
                }
            },
            {
                "kind": "pair",
                "desc": "Acceleration in x axis.",
                "key": "PushX",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Acceleration in z axis.",
                "key": "PushZ",
                "type": {
                    "kind": "double"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Ticks until the fuel runs out.",
                "key": "Fuel",
                "type": {
                    "kind": "short"
                },
                "optional": True
            }
        ]
    }
}

