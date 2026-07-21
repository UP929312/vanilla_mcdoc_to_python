# Generated from symbols.json for ::java::data::worldgen::structure::RuinedPortalSetup
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.RuinedPortalPlacement import RuinedPortalPlacement


@dataclass(kw_only=True)
class RuinedPortalSetup:
    placement: RuinedPortalPlacement
    air_pocket_probability: Annotated[float, 'Range | `0`-`1` | both inclusive']
    mossiness: Annotated[float, 'Range | `0`-`1` | both inclusive']
    overgrown: bool
    vines: bool
    can_be_cold: bool
    replace_with_blackstone: bool
    weight: Annotated[float, 'Range | Min `0` and above | inclusive']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::RuinedPortalSetup": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "placement",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::RuinedPortalPlacement"
                }
            },
            {
                "kind": "pair",
                "key": "air_pocket_probability",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "mossiness",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 1
                    }
                }
            },
            {
                "kind": "pair",
                "key": "overgrown",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "vines",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "can_be_cold",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "replace_with_blackstone",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "weight",
                "type": {
                    "kind": "float",
                    "valueRange": {
                        "kind": 0,
                        "min": 0
                    }
                }
            }
        ]
    }
}

