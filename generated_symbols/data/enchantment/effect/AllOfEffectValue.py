# Generated from symbols.json for ::java::data::enchantment::effect::AllOfEffectValue
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.ValueEffect import ValueEffect


@dataclass(kw_only=True)
class AllOfEffectValue:
    effects: Annotated[list[ValueEffect], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::AllOfEffectValue": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::enchantment::effect::ValueEffect"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 1
                    }
                }
            }
        ]
    }
}

