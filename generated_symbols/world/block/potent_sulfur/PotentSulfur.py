# Generated from symbols.json for ::java::world::block::potent_sulfur::PotentSulfur
from dataclasses import dataclass
from generated_symbols.world.block.BlockEntity import BlockEntity


@dataclass(kw_only=True)
class PotentSulfur(BlockEntity):
    countdown: int | None = None  # Time in seconds until the next state switch (between dormant and erupting).  The timer only counts down when the potent sulfur creates a valid geyser.  Negative values will be replaced with a new duration of the current state.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::potent_sulfur::PotentSulfur": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "pair",
                "desc": "Time in seconds until the next state switch (between dormant and erupting). \\\nThe timer only counts down when the potent sulfur creates a valid geyser. \\\nNegative values will be replaced with a new duration of the current state.",
                "key": "countdown",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

