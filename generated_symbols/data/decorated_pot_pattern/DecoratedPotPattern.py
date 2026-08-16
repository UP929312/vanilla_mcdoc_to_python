"""
Generated from symbols.json for ::java::data::decorated_pot_pattern::DecoratedPotPattern
Local link to file: generated_symbols/data/decorated_pot_pattern/DecoratedPotPattern.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class DecoratedPotPattern:
    __resource_dir__: ClassVar[str] = 'decorated_pot_pattern'

    asset_id: Annotated[str, IdSpec(registry='texture', path='entity/decorated_pot/')]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::decorated_pot_pattern::DecoratedPotPattern": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "asset_id",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "tree",
                                "values": {
                                    "registry": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "texture"
                                        }
                                    },
                                    "path": {
                                        "kind": "literal",
                                        "value": {
                                            "kind": "string",
                                            "value": "entity/decorated_pot/"
                                        }
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        ]
    }
}

