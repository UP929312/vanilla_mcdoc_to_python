# Generated from symbols.json for ::java::pack::PackOverlays
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.pack.PackOverlay import PackOverlay


@dataclass(kw_only=True)
class PackOverlays:
    entries: list[PackOverlay]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::pack::PackOverlays": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "entries",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::pack::PackOverlay"
                    }
                }
            }
        ]
    }
}

