# Generated from symbols.json for ::java::data::util::NbtContextTarget
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.BlockEntityTarget import BlockEntityTarget
    from generated_symbols.data.loot.EntityTarget import EntityTarget


type NbtContextTarget = EntityTarget | BlockEntityTarget


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::NbtContextTarget": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::data::util::NbtProviderSource",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.9"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::loot::EntityTarget",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.9"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::data::loot::BlockEntityTarget",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.9"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

