"""
Generated from symbols.json for ::java::data::enchantment::provider::SingleProvider
Local link to file: generated_symbols/data/enchantment/provider/SingleProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, ClassVar

from generated_symbols.base import GeneratedModel
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.IntProvider import IntProvider


class SingleProvider(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'enchantment_provider'

    enchantment: Annotated[str, IdSpec(registry='enchantment')]
    level: IntProvider[int] | int


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::provider::SingleProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "enchantment",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "enchantment"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "level",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::IntProvider"
                    },
                    "typeArgs": [
                        {
                            "kind": "int"
                        }
                    ]
                }
            }
        ]
    }
}
