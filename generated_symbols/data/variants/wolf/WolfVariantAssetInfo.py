# Generated from symbols.json for ::java::data::variants::wolf::WolfVariantAssetInfo
from dataclasses import dataclass


@dataclass(kw_only=True)
class WolfVariantAssetInfo:
    wild: str
    tame: str
    angry: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::wolf::WolfVariantAssetInfo": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "wild",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "texture"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "tame",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "texture"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "angry",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "texture"
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

