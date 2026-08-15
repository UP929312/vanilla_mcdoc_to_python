"""
Generated from symbols.json for ::java::assets::model::ModelRef
Local link to file: generated_symbols/assets/model/ModelRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from minecraft_registry import IdSpec


type ModelRef = Annotated[str, IdSpec(registry='model', exclude=('builtin/generated', 'builtin/entity'))]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ModelRef": {
        "kind": "string",
        "attributes": [
            {
                "name": "id",
                "value": {
                    "kind": "tree",
                    "values": {
                        "registry": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "model"
                            }
                        },
                        "exclude": {
                            "kind": "tree",
                            "values": {
                                "0": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "builtin/generated"
                                    }
                                },
                                "1": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "builtin/entity"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        ]
    }
}

