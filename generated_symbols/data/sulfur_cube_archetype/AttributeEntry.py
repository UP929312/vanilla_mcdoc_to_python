# Generated from symbols.json for ::java::data::sulfur_cube_archetype::AttributeEntry
from dataclasses import dataclass
from generated_symbols.world.entity.mob.ModernAttributeModifier import ModernAttributeModifier


@dataclass(kw_only=True)
class AttributeEntry(ModernAttributeModifier):
    attribute: str  # Attribute type to modify.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::sulfur_cube_archetype::AttributeEntry": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Attribute type to modify.",
                "key": "attribute",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "attribute"
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
                    "path": "::java::world::entity::mob::ModernAttributeModifier"
                }
            }
        ]
    }
}

