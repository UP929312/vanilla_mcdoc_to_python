# Generated from symbols.json for ::java::assets::item_definition::Book
from dataclasses import dataclass


@dataclass(kw_only=True)
class Book:
    open_angle: float  # Angle in degrees between book cover and book centerline.  `0.0` for closed, `90.0` for open flat.
    page1: float  # The position of the first page inside the book.  `0.0` for leftmost, `1.0` for rightmost.
    page2: float  # The position of the second page inside the book.  `0.0` for leftmost, `1.0` for rightmost.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::Book": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Angle in degrees between book cover and book centerline. \\\n`0.0` for closed, `90.0` for open flat.",
                "key": "open_angle",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "The position of the first page inside the book. \\\n`0.0` for leftmost, `1.0` for rightmost.",
                "key": "page1",
                "type": {
                    "kind": "float"
                }
            },
            {
                "kind": "pair",
                "desc": "The position of the second page inside the book. \\\n`0.0` for leftmost, `1.0` for rightmost.",
                "key": "page2",
                "type": {
                    "kind": "float"
                }
            }
        ]
    }
}

