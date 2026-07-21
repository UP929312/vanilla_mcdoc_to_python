# Generated from symbols.json for ::java::assets::model::ItemTransform
from dataclasses import dataclass
from typing import Annotated


@dataclass(kw_only=True)
class ItemTransform:
    rotation: tuple[float, float, float] | None = None
    translation: tuple[Annotated[float, 'Range | `-80`-`80` | both inclusive'], Annotated[float, 'Range | `-80`-`80` | both inclusive'], Annotated[float, 'Range | `-80`-`80` | both inclusive']] | None = None
    scale: tuple[Annotated[float, 'Range | `-4`-`4` | both inclusive'], Annotated[float, 'Range | `-4`-`4` | both inclusive'], Annotated[float, 'Range | `-4`-`4` | both inclusive']] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::model::ItemTransform": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "rotation",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float"
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "translation",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float",
                        "valueRange": {
                            "kind": 0,
                            "min": -80,
                            "max": 80
                        }
                    },
                    "lengthRange": {
                        "kind": 0,
                        "min": 3,
                        "max": 3
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "scale",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "float",
                        "valueRange": {
                            "kind": 0,
                            "min": -4,
                            "max": 4
                        }
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

