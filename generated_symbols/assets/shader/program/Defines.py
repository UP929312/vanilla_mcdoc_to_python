# Generated from symbols.json for ::java::assets::shader::program::Defines
from dataclasses import dataclass


@dataclass(kw_only=True)
class Defines:
    values: dict[str, str] | None = None  # Values that will be injected as `#define <key> <value>` at the top of the file.
    flags: list[str] | None = None  # Flags that will be injected as `#define <key>` at the top of the file.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::shader::program::Defines": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Values that will be injected as `#define <key> <value>` at the top of the file.",
                "key": "values",
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": {
                                "kind": "string"
                            },
                            "type": {
                                "kind": "string"
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Flags that will be injected as `#define <key>` at the top of the file.",
                "key": "flags",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string"
                    }
                },
                "optional": True
            }
        ]
    }
}

