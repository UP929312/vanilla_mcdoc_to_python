# Generated from symbols.json for ::java::data::advancement::predicate::MobEffectPredicate
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.util.MinMaxBounds import MinMaxBounds


@dataclass(kw_only=True)
class MobEffectPredicate:
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

