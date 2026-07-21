# Generated from symbols.json for ::java::pack::PackFeatures
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.pack.FeatureFlag import FeatureFlag


@dataclass(kw_only=True)
class PackFeatures:
    enabled: list[FeatureFlag]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::PackFeatures": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "enabled",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::pack::FeatureFlag",
                        "attributes": [
                            {
                                "name": "id"
                            }
                        ]
                    }
                }
            }
        ]
    }
}

