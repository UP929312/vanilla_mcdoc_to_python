# Generated from symbols.json for ::java::assets::item_definition::TrimMaterial
from dataclasses import dataclass
from generated_symbols.assets.item_definition.SelectCases import SelectCases


@dataclass(kw_only=True)
class TrimMaterial(SelectCases[str]):
    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::TrimMaterial": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::SelectCases"
                    },
                    "typeArgs": [
                        {
                            "kind": "string",
                            "attributes": [
                                {
                                    "name": "id",
                                    "value": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "trim_material"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}

