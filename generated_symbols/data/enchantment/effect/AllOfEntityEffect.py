# Generated from symbols.json for ::java::data::enchantment::effect::AllOfEntityEffect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.enchantment.effect.EntityEffect import EntityEffect


@dataclass(kw_only=True)
class AllOfEntityEffect:
    effects: Annotated[list[EntityEffect], 'Length = 1 (inclusive) and above']


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect::AllOfEntityEffect": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "effects",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::enchantment::effect::EntityEffect"
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

