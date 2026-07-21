# Generated from symbols.json for ::java::data::enchantment::effect_component::AttackTarget
from enum import Enum


class AttackTarget(Enum):
    ATTACKER = "attacker"
    DAMAGINGENTITY = "damaging_entity"
    VICTIM = "victim"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::enchantment::effect_component::AttackTarget": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Attacker",
                "value": "attacker"
            },
            {
                "identifier": "DamagingEntity",
                "value": "damaging_entity"
            },
            {
                "identifier": "Victim",
                "value": "victim"
            }
        ]
    }
}

