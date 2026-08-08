# Generated from symbols.json for ::java::data::advancement::predicate::PlayerAdvancements


type PlayerAdvancementsValueStruct = dict[str, bool]


type PlayerAdvancements = dict[str, bool | PlayerAdvancementsValueStruct]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::PlayerAdvancements": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "advancement"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "union",
                    "members": [
                        {
                            "kind": "boolean"
                        },
                        {
                            "kind": "struct",
                            "fields": [
                                {
                                    "kind": "pair",
                                    "key": {
                                        "kind": "string"
                                    },
                                    "type": {
                                        "kind": "boolean"
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

