# Generated from symbols.json for ::java::data::enchantment::effect::AllOfLocationBasedEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.LocationBasedEffect import LocationBasedEffect


@dataclass(kw_only=True)
class AllOfLocationBasedEffect:
    effects: Annotated[list[LocationBasedEffect], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::AllOfLocationBasedEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::enchantment::effect::LocationBasedEffect"
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

