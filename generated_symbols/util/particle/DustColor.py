"""
Generated from symbols.json for ::java::util::particle::DustColor
Local link to file: generated_symbols/util/particle/DustColor.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


type DustColor = RGB


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::DustColor": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::util::particle::LegacyDustColor",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ]
            },
            {
                "kind": "reference",
                "path": "::java::util::color::RGB",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.21.2"
                            }
                        }
                    }
                ]
            }
        ]
    }
}

