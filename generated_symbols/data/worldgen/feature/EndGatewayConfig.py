# Generated from symbols.json for ::java::data::worldgen::feature::EndGatewayConfig
from dataclasses import dataclass


@dataclass(kw_only=True)
class EndGatewayConfig:
    exact: bool
    exit: tuple[int, int, int] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::EndGatewayConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "exact",
                "type": {
                    "kind": "boolean"
                }
            },
            {
                "kind": "pair",
                "key": "exit",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

