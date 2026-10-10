"""
Generated from symbols.json for ::java::world::component::item::KineticWeaponEffectCondition
Local link to file: vanilla_mcdoc/world/component/item/KineticWeaponEffectCondition.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class KineticWeaponEffectCondition(GeneratedModel):
    max_duration_ticks: int  # The duration in ticks this condition can pass. Starts counting after charged.
    min_speed: float | None = None  # The minimum attacker speed required. Defaults to 0.0
    min_relative_speed: float | None = None  # The minimum relative speed required. Defaults to 0.0
