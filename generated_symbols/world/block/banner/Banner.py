# Generated from symbols.json for ::java::world::block::banner::Banner
from dataclasses import dataclass
from typing import TYPE_CHECKING
from generated_symbols.world.block.BlockEntity import BlockEntity
from generated_symbols.world.block.Nameable import Nameable

if TYPE_CHECKING:
    from generated_symbols.world.block.banner.BannerPatternLayer import BannerPatternLayer


@dataclass(kw_only=True)
class Banner(BlockEntity, Nameable):
    patterns: list[BannerPatternLayer] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::banner::Banner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::BlockEntity"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::world::block::Nameable"
                }
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "until",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "Patterns",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::block::banner::BannerPatternLayer"
                    }
                },
                "optional": True
            },
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "1.20.5"
                            }
                        }
                    }
                ],
                "key": "patterns",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::world::block::banner::BannerPatternLayer"
                    }
                },
                "optional": True
            }
        ]
    }
}

