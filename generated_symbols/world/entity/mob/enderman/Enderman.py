# Generated from symbols.json for ::java::world::entity::mob::enderman::Enderman
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.entity.mob.MobBase import MobBase
from generated_symbols.world.entity.mob.NeutralMob import NeutralMob

if TYPE_CHECKING:
    from generated_symbols.util.BlockState import BlockState


@dataclass(kw_only=True)
class Enderman(MobBase, NeutralMob):
    carriedBlockState: BlockState | None = None  # Block it is carrying.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::entity::mob::enderman::Enderman": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::MobBase"
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.16"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "reference",
                    "path": "::java::world::entity::mob::NeutralMob"
                }
            },
            {
                "kind": "pair",
                "desc": "Block it is carrying.",
                "key": "carriedBlockState",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::BlockState"
                },
                "optional": True
            }
        ]
    }
}

