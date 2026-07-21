# Generated from symbols.json for ::java::data::advancement::predicate::DamageSourceFlags
from dataclasses import dataclass


@dataclass(kw_only=True)
class DamageSourceFlags:
    is_explosion: bool | None = None
    is_fire: bool | None = None
    is_magic: bool | None = None
    is_projectile: bool | None = None
    is_lightning: bool | None = None
    bypasses_armor: bool | None = None
    bypasses_invulnerability: bool | None = None
    bypasses_magic: bool | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::advancement::predicate::DamageSourceFlags": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "is_explosion",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_fire",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_magic",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_projectile",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "is_lightning",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "bypasses_armor",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "bypasses_invulnerability",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "bypasses_magic",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

