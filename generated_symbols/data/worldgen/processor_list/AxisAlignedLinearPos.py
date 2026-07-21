# Generated from symbols.json for ::java::data::worldgen::processor_list::AxisAlignedLinearPos
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.data.worldgen.processor_list.LinearPos import LinearPos

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.Axis import Axis


@dataclass(kw_only=True)
class AxisAlignedLinearPos(LinearPos):
    axis: Axis


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::processor_list::AxisAlignedLinearPos": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "axis",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::Axis"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::LinearPos"
                }
            }
        ]
    }
}

