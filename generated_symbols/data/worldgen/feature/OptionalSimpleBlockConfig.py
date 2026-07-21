# Generated from symbols.json for ::java::data::worldgen::feature::OptionalSimpleBlockConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.block_state.BlockState import BlockState


@dataclass(kw_only=True)
class OptionalSimpleBlockConfig:
    place_on: list[BlockState] | None = None
    place_in: list[BlockState] | None = None
    place_under: list[BlockState] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::OptionalSimpleBlockConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "place_on",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "place_in",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "place_under",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::block_state::BlockState"
                    }
                },
                "optional": True
            }
        ]
    }
}

