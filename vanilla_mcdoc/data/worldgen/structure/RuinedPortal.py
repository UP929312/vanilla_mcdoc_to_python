"""
Generated from symbols.json for ::java::data::worldgen::structure::RuinedPortal
Local link to file: vanilla_mcdoc/data/worldgen/structure/RuinedPortal.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.structure.RuinedPortalSetup import RuinedPortalSetup


class RuinedPortal(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/structure'

    setups: list[RuinedPortalSetup]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::structure::RuinedPortal": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "portal_type",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::structure::RuinedPortalType"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19"
                            }
                        }
                    }
                ],
                "key": "setups",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::structure::RuinedPortalSetup"
                    }
                }
            }
        ]
    }
}
