# Generated from symbols.json for ::java::util::particle::TranslucentParticle
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGBA import RGBA


type TranslucentParticle = RGBA


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::particle::TranslucentParticle": {
        "kind": "union",
        "members": [
            {
                "kind": "reference",
                "path": "::java::util::particle::LegacyTranslucentParticle",
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
                "path": "::java::util::color::RGBA",
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

