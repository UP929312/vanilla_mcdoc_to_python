"""
Generated from symbols.json for ::java::assets::item_definition::Banner
Local link to file: vanilla_mcdoc/assets/item_definition/Banner.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.item_definition.BannerAttachment import BannerAttachment
    from vanilla_mcdoc.util.color.DyeColor import DyeColor


class Banner(GeneratedModel):
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
