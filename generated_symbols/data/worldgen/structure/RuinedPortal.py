# Generated from symbols.json for ::java::data::worldgen::structure::RuinedPortal
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.structure.RuinedPortalSetup import RuinedPortalSetup


@dataclass(kw_only=True)
class RuinedPortal:
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

