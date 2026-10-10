"""
Generated from symbols.json for ::java::data::advancement::predicate::DamageSourceFlags
Local link to file: vanilla_mcdoc/data/advancement/predicate/DamageSourceFlags.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class DamageSourceFlags(GeneratedModel):
    is_explosion: bool | None = None
    is_fire: bool | None = None
    is_magic: bool | None = None
    is_projectile: bool | None = None
    is_lightning: bool | None = None
    bypasses_armor: bool | None = None
    bypasses_invulnerability: bool | None = None
    bypasses_magic: bool | None = None
