# Generated from symbols.json for ::java::assets::item_definition::Banner
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.BannerAttachment import BannerAttachment
    from generated_symbols.util.color.DyeColor import DyeColor


@dataclass(kw_only=True)
class Banner:
    color: DyeColor
    attachment: BannerAttachment | None = None  # Defaults to `ground`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Banner": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "color",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::DyeColor"
                }
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
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "Defaults to `ground`.",
                "key": "attachment",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::BannerAttachment"
                },
                "optional": True
            }
        ]
    }
}

