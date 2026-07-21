# Generated from symbols.json for ::java::assets::atlas::Directory
from dataclasses import dataclass


@dataclass(kw_only=True)
class Directory:
    source: str  # Directory of texture locations to include, relative to the `textures` folder, not including the trailing `/`.
    prefix: str  # The sprite name prefix, usually ending with `/`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::atlas::Directory": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Directory of texture locations to include, relative to the `textures` folder, not including the trailing `/`.",
                "key": "source",
                "type": {
                    "kind": "string"
                }
            },
            {
                "kind": "pair",
                "desc": "The sprite name prefix, usually ending with `/`.",
                "key": "prefix",
                "type": {
                    "kind": "string"
                }
            }
        ]
    }
}

