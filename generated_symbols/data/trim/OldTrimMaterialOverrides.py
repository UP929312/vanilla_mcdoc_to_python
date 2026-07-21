# Generated from symbols.json for ::java::data::trim::OldTrimMaterialOverrides
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.trim.ArmorMaterial import ArmorMaterial


type OldTrimMaterialOverrides = dict[ArmorMaterial, str]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::trim::OldTrimMaterialOverrides": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::data::trim::ArmorMaterial",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                },
                "type": {
                    "kind": "string"
                }
            }
        ]
    }
}

