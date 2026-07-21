# Generated from symbols.json for ::java::util::fluid_state::FluidState
from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class FluidState:
    Name: str
    Properties: Any | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::fluid_state::FluidState": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "Name",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "fluid"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "Properties",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "Name"
                            ]
                        }
                    ],
                    "registry": "mcdoc:fluid_states"
                },
                "optional": True
            }
        ]
    }
}

