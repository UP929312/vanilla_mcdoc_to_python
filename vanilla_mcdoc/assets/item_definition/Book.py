"""
Generated from symbols.json for ::java::assets::item_definition::Book
Local link to file: vanilla_mcdoc/assets/item_definition/Book.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Book(GeneratedModel):
    open_angle: float  # Angle in degrees between book cover and book centerline.  `0.0` for closed, `90.0` for open flat.
    page1: float  # The position of the first page inside the book.  `0.0` for leftmost, `1.0` for rightmost.
    page2: float  # The position of the second page inside the book.  `0.0` for leftmost, `1.0` for rightmost.
