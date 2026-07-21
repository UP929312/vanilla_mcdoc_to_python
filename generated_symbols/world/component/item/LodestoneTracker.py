# Generated from symbols.json for ::java::world::component::item::LodestoneTracker
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.GlobalPos import GlobalPos


@dataclass(kw_only=True)
class LodestoneTracker:
    target: GlobalPos | None = None  # Location of the lodestone. Optional. If not set, the compass will spin randomly.
    tracked: bool | None = None  # When `true`, the component is removed when the lodestone is broken. When `false`, the component is kept. Defaults to true.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::component::item::LodestoneTracker": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Location of the lodestone. Optional. If not set, the compass will spin randomly.",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::GlobalPos"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "When `True`, the component is removed when the lodestone is broken. When `False`, the component is kept. Defaults to True.",
                "key": "tracked",
                "type": {
                    "kind": "boolean"
                },
                "optional": True
            }
        ]
    }
}

