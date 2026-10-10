"""
Generated from symbols.json for ::java::world::block::spawner::CustomSpawnRules
Local link to file: vanilla_mcdoc/world/block/spawner/CustomSpawnRules.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.InclusiveRange import InclusiveRange


class CustomSpawnRules(GeneratedModel):
    block_light_limit: InclusiveRange[Annotated[int, Field(ge=0, le=15)]] | Annotated[int, Field(ge=0, le=15)] | None = None  # Range of block light level required for the entity to spawn.
    sky_light_limit: InclusiveRange[Annotated[int, Field(ge=0, le=15)]] | Annotated[int, Field(ge=0, le=15)] | None = None  # Range of sky light level required for the entity to spawn.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::spawner::CustomSpawnRules": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Range of block light level required for the entity to spawn.",
                "key": "block_light_limit",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::InclusiveRange"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 15
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Range of sky light level required for the entity to spawn.",
                "key": "sky_light_limit",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::util::InclusiveRange"
                    },
                    "typeArgs": [
                        {
                            "kind": "int",
                            "valueRange": {
                                "kind": 0,
                                "min": 0,
                                "max": 15
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}
