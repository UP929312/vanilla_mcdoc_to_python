"""
Generated from symbols.json for ::java::pack::PackFeatures
Local link to file: generated_symbols/pack/PackFeatures.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.pack.FeatureFlag import FeatureFlag


class PackFeatures(GeneratedModel):
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
