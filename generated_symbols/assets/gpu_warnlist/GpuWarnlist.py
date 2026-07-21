# Generated from symbols.json for ::java::assets::gpu_warnlist::GpuWarnlist
from dataclasses import dataclass


@dataclass(kw_only=True)
class GpuWarnlist:
    renderer: list[str] | None = None
    version: list[str] | None = None
    vendor: list[str] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::gpu_warnlist::GpuWarnlist": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "renderer",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "regex_pattern"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "version",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "regex_pattern"
                            }
                        ]
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "vendor",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "regex_pattern"
                            }
                        ]
                    }
                },
                "optional": True
            }
        ]
    }
}

