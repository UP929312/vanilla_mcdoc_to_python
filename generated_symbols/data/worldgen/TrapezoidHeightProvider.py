# Generated from symbols.json for ::java::data::worldgen::TrapezoidHeightProvider
from dataclasses import dataclass
from generated_symbols.data.worldgen.UniformHeightProvider import UniformHeightProvider


@dataclass(kw_only=True)
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

