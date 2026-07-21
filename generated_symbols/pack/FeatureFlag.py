# Generated from symbols.json for ::java::pack::FeatureFlag
from enum import Enum


class FeatureFlag(Enum):
    VANILLA = "vanilla"
    UPDATE120 = "update_1_20"
    BUNDLE = "bundle"
    TRADEREBALANCE = "trade_rebalance"
    UPDATE121 = "update_1_21"
    REDSTONEEXPERIMENTS = "redstone_experiments"
    MINECARTIMPROVEMENTS = "minecart_improvements"
    WINTERDROP = "winter_drop"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::FeatureFlag": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Vanilla",
                "value": "vanilla"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20"
                            }
                        }
                    }
                ],
                "identifier": "Update120",
                "value": "update_1_20"
            },
            {
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "identifier": "Bundle",
                "value": "bundle"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.2"
                            }
                        }
                    }
                ],
                "identifier": "TradeRebalance",
                "value": "trade_rebalance"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.3"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21"
                            }
                        }
                    }
                ],
                "identifier": "Update121",
                "value": "update_1_21"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "identifier": "RedstoneExperiments",
                "value": "redstone_experiments"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ],
                "identifier": "MinecartImprovements",
                "value": "minecart_improvements"
            },
            {
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    },
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.4"
                            }
                        }
                    }
                ],
                "identifier": "WinterDrop",
                "value": "winter_drop"
            }
        ]
    }
}

