# Generated from symbols.json for ::java::data::worldgen::feature::EndSpikeConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.feature.EndSpike import EndSpike


@dataclass(kw_only=True)
class EndSpikeConfig:
    spikes: list[EndSpike]
    crystal_invulnerable: bool | None = None
    crystal_beam_target: tuple[int, int, int] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::EndSpikeConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "spikes",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::feature::EndSpike"
                    }
                }
            },
            {
                "kind": "pair",
                "key": "crystal_invulnerable",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "crystal_beam_target",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "int"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            }
        ]
    }
}

