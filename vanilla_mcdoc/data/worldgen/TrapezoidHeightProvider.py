"""
Generated from symbols.json for ::java::data::worldgen::TrapezoidHeightProvider
Local link to file: vanilla_mcdoc/data/worldgen/TrapezoidHeightProvider.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.data.worldgen.UniformHeightProvider import UniformHeightProvider


class TrapezoidHeightProvider(UniformHeightProvider):
    plateau: int | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::TrapezoidHeightProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::UniformHeightProvider"
                }
            },
            {
                "kind": "pair",
                "key": "plateau",
                "type": {
                    "kind": "int"
                },
                "optional": True
            }
        ]
    }
}
