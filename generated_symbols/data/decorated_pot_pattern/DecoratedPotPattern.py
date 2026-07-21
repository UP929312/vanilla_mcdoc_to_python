# Generated from symbols.json for ::java::data::decorated_pot_pattern::DecoratedPotPattern
from dataclasses import dataclass


@dataclass(kw_only=True)
class DecoratedPotPattern:
    asset_id: str


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::decorated_pot_pattern::DecoratedPotPattern": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "asset_id",
                "type": {
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
                                            "value": "texture"
                                        }
                                    },
                                    "path": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "entity/decorated_pot/"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

