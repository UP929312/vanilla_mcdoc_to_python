# Generated from symbols.json for ::java::data::worldgen::carver::CarverRef
from typing import TYPE_CHECKING, Annotated

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.carver.ConfiguredCarver import ConfiguredCarver


type CarverRef = ConfiguredCarver | Annotated[str, IdSpec(registry='worldgen/carver')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::carver::CarverRef": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::worldgen::carver::ConfiguredCarver"
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/configured_carver"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.3"
                            }
                        }
                    },
                    {
                        "name": "id",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "worldgen/carver"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

