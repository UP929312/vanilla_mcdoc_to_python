# Generated from symbols.json for ::java::data::variants::zombie_nautilus::ZombieNautilusVariant
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.variants.SpawnPrioritySelectors import SpawnPrioritySelectors

if TYPE_CHECKING:
    from generated_symbols.data.variants.zombie_nautilus.ZombieNautilusModelType import ZombieNautilusModelType


@dataclass(kw_only=True)
class ZombieNautilusVariant(SpawnPrioritySelectors):
    asset_id: str  # The zombie nautilus texture to use for this variant.
    model: ZombieNautilusModelType | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::zombie_nautilus::ZombieNautilusVariant": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "model",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::variants::zombie_nautilus::ZombieNautilusModelType"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "The zombie nautilus texture to use for this variant.",
                "key": "asset_id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "texture"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::variants::SpawnPrioritySelectors"
                }
            }
        ]
    }
}

