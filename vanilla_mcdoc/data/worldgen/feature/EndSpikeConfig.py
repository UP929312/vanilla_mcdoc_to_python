"""
Generated from symbols.json for ::java::data::worldgen::feature::EndSpikeConfig
Local link to file: vanilla_mcdoc/data/worldgen/feature/EndSpikeConfig.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, ClassVar

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.worldgen.feature.EndSpike import EndSpike


class EndSpikeConfig(GeneratedModel):
    __resource_dir__: ClassVar[str] = 'worldgen/feature'

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
