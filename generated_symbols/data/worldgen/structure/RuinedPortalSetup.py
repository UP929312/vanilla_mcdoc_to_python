"""
Generated from symbols.json for ::java::data::worldgen::structure::RuinedPortalSetup
Local link to file: generated_symbols/data/worldgen/structure/RuinedPortalSetup.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from pydantic import Field

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.RuinedPortalPlacement import RuinedPortalPlacement


class RuinedPortalSetup(GeneratedModel):
    placement: RuinedPortalPlacement
    air_pocket_probability: Annotated[float, Field(ge=0, le=1)]
    mossiness: Annotated[float, Field(ge=0, le=1)]
    overgrown: bool
    vines: bool
    can_be_cold: bool
    replace_with_blackstone: bool
    weight: Annotated[float, Field(ge=0)]


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

