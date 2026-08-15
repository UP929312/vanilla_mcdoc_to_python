"""
Generated from symbols.json for ::java::data::worldgen::template_pool::TemplatePool
Local link to file: generated_symbols/data/worldgen/template_pool/TemplatePool.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.template_pool.WeightedElement import WeightedElement


@dataclass(kw_only=True)
class TemplatePool:
    name: str | None = None
    fallback: Annotated[str, IdSpec(registry='worldgen/template_pool')]
    elements: list[WeightedElement]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::template_pool::TemplatePool": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "name",
                            "type": {
                                "kind": "string"
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.19.3"
                            }
                        }
                    }
                ],
                "type": {
                    "kind": "struct",
                    "fields": [
                        {
                            "kind": "pair",
                            "key": "name",
                            "type": {
                                "kind": "string"
                            },
                            "optional": True
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "fallback",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/template_pool"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "key": "elements",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::worldgen::template_pool::WeightedElement"
                    }
                }
            }
        ]
    }
}

