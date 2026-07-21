# Generated from symbols.json for ::java::util::particle::VibrationParticleData
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.particle.SafePositionSource import SafePositionSource


@dataclass(kw_only=True)
class VibrationParticleData:
    arrival_in_ticks: int  # Ticks in which to interpolate the particle's initial position to the destination.
    destination: SafePositionSource


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::VibrationParticleData": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Ticks in which to interpolate the particle's initial position to the destination.",
                "key": "arrival_in_ticks",
                "type": {
                    "kind": "int"
                }
            },
            {
                "kind": "pair",
                "key": "destination",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::particle::SafePositionSource"
                }
            }
        ]
    }
}

