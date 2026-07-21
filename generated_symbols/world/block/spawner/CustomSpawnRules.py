# Generated from symbols.json for ::java::world::block::spawner::CustomSpawnRules
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.util.InclusiveRange import InclusiveRange


@dataclass(kw_only=True)
class CustomSpawnRules:
    block_light_limit: InclusiveRange[Annotated[int, 'Range | `0`-`15` | both inclusive']] | Annotated[int, 'Range | `0`-`15` | both inclusive'] | None = None  # Range of block light level required for the entity to spawn.
    sky_light_limit: InclusiveRange[Annotated[int, 'Range | `0`-`15` | both inclusive']] | Annotated[int, 'Range | `0`-`15` | both inclusive'] | None = None  # Range of sky light level required for the entity to spawn.


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

