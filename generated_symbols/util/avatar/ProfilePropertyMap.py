"""
Generated from symbols.json for ::java::util::avatar::ProfilePropertyMap
Local link to file: generated_symbols/util/avatar/ProfilePropertyMap.py
"""
# ~~~ CODE ~~~


type ProfilePropertyMap = dict[str, list[str]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::avatar::ProfilePropertyMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The key is usually `textures`.\nBase64 encoded JSON value of the texture index.",
                "key": {
                    "kind": "string"
                },
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string"
                    }
                }
            }
        ]
    }
}

