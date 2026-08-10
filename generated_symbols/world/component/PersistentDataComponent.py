"""
Generated from symbols.json for ::java::world::component::PersistentDataComponent
Local link to file: generated_symbols/world/component/PersistentDataComponent.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from runtime_metadata import IdSpec


type PersistentDataComponent = Annotated[str, IdSpec(registry='data_component_type', exclude=('additional_trade_cost', 'creative_slot_lock', 'map_post_processing'))]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::PersistentDataComponent": {
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
                                "value": "data_component_type"
                            }
                        },
                        "exclude": {
                            "kind": "tree",
                            "values": {
                                "0": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "additional_trade_cost"
                                    }
                                },
                                "1": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "creative_slot_lock"
                                    }
                                },
                                "2": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "map_post_processing"
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

