# Generated from symbols.json for ::java::world::block::comparator::Comparator
from dataclasses import dataclass
from generated_symbols.world.block.BlockEntity import BlockEntity


@dataclass(kw_only=True)
class Comparator(BlockEntity):
    OutputSignal: int | None = None  # Strength of the redstone output.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::comparator::Comparator": {
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
                "desc": "Strength of the redstone output.",
                "key": "OutputSignal",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}

