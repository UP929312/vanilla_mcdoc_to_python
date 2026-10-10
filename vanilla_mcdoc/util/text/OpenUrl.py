"""
Generated from symbols.json for ::java::util::text::OpenUrl
Local link to file: vanilla_mcdoc/util/text/OpenUrl.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import MinecraftURL


class OpenUrl(GeneratedModel):
    url: MinecraftURL


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::OpenUrl": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "value",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "url"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.5"
                            }
                        }
                    }
                ],
                "key": "url",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "url"
                        }
                    ]
                }
            }
        ]
    }
}
