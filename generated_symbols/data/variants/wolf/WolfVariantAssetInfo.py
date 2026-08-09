# Generated from symbols.json for ::java::data::variants::wolf::WolfVariantAssetInfo
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class WolfVariantAssetInfo:
    wild: Annotated[str, IdSpec(registry='texture')]
    tame: Annotated[str, IdSpec(registry='texture')]
    angry: Annotated[str, IdSpec(registry='texture')]


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

