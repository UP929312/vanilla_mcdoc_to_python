# Generated from symbols.json for ::java::world::component::item::BlockTransformer
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.util.SoundEventRef import SoundEventRef
    from generated_symbols.data.worldgen.feature.block_state_provider.BlockStateProvider import BlockStateProvider
    from generated_symbols.util.direction.Direction import Direction
    from generated_symbols.world.component.item.BlockTransformDropStrategy import BlockTransformDropStrategy
    from generated_symbols.world.component.item.BlockTransformParticle import BlockTransformParticle
    from generated_symbols.world.component.item.BlockTransformType import BlockTransformType


@dataclass(kw_only=True)
class BlockTransformer:
    block_state_provider: BlockStateProvider  # If the provider returns no result, the next transformer will be attempted.
    sound: SoundEventRef | None = None  # Defaults to not playing sound.
    particle: BlockTransformParticle | None = None  # Defaults to `none`.
    disallowed_faces: list[Direction] | None = None  # If a disallowed face is interacted with, the next transformer will be attempted.  Defaults to empty (allowing all faces).
    loot: str | None = None  # The loot to drop on a successful transformation.  Defaults to drop nothing.
    drop_strategy: BlockTransformDropStrategy | None = None  # Where the `loot` should drop.  Defaults to `from_middle`.
    transform_type: BlockTransformType | None = None  # How nearby blocks are affected by the transformation.  Defaults to `single_block`.
    update_from_neighbors: bool | None = None  # Whether the transformed block should update based on neighboring blocks.  Defaults to `true`.
    consume_on_use: bool | None = None  # Only has effect on stackable items.  Defaults to `true`.
    item_damage_per_use: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # Only has effect on unstackable items.  Defauls to 1.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::BlockTransformer": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If the provider returns no result, the next transformer will be attempted.",
                "key": "block_state_provider",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::feature::block_state_provider::BlockStateProvider"
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to not playing sound.",
                "key": "sound",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::util::SoundEventRef"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to `none`.",
                "key": "particle",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::BlockTransformParticle"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "If a disallowed face is interacted with, the next transformer will be attempted. \\\nDefaults to empty (allowing all faces).",
                "key": "disallowed_faces",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::util::direction::Direction"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The loot to drop on a successful transformation. \\\nDefaults to drop nothing.",
                "key": "loot",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "loot_table"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Where the `loot` should drop. \\\nDefaults to `from_middle`.",
                "key": "drop_strategy",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::BlockTransformDropStrategy"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "How nearby blocks are affected by the transformation. \\\nDefaults to `single_block`.",
                "key": "transform_type",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::component::item::BlockTransformType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Whether the transformed block should update based on neighboring blocks. \\\nDefaults to `True`.",
                "key": "update_from_neighbors",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Only has effect on stackable items. \\\nDefaults to `True`.",
                "key": "consume_on_use",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Only has effect on unstackable items. \\\nDefauls to 1.",
                "key": "item_damage_per_use",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                },
                "optional": True
            }
        ]
    }
}

