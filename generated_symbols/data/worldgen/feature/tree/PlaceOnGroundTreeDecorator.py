# Generated from symbols.json for ::java::data::worldgen::feature::tree::PlaceOnGroundTreeDecorator
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider


@dataclass(kw_only=True)
class PlaceOnGroundTreeDecorator:
    block_state_provider: BlockStateProvider  # The block to place on the ground.
    tries: Annotated[int, 'Range | Min `1` and above | inclusive'] | None = None  # Defaults to `128`.
    radius: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to `2`.
    height: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Defaults to `1`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::PlaceOnGroundTreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Defaults to `128`.",
                "key": "tries",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 1
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `2`.",
                "key": "radius",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `1`.",
                "key": "height",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The block to place on the ground.",
                "key": "block_state_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            }
        ]
    }
}

