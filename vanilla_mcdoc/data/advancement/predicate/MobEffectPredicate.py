"""
Generated from symbols.json for ::java::data::advancement::predicate::MobEffectPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/MobEffectPredicate.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds


class MobEffectPredicate(GeneratedModel):
    amplifier: MinMaxBounds[int] | int | None = None
    duration: MinMaxBounds[int] | int | None = None
    ambient: bool | None = None
    visible: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::MobEffectPredicate": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "amplifier",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "duration",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::util::MinMaxBounds"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "ambient",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "visible",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}
