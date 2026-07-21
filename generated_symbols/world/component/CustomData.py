# Generated from symbols.json for ::java::world::component::CustomData
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.world.component.CustomDataMap import CustomDataMap


type CustomData = CustomDataMap | str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::CustomData": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::world::component::CustomDataMap",
                "attributes": [
                    {
                        "name": "canonical"
                    }
                ]
            },
            {
                "kind": "string",
                "attributes": [
                    {
                        "name": "nbt",
                        "value": {
                            "kind": "reference",
                            "path": "::java::world::component::CustomDataMap"
                        }
                    }
                ]
            }
        ]
    }
}

