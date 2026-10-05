# ~~~ WHAT ARE WE TESTING ~~~

# This has the weird `...::tag::E` thing, ensure it's working properly.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::tag::ExplicitTagEntry
Local link to file: generated_symbols/data/tag/ExplicitTagEntry.py
"""
# ~~~ CODE ~~~
from typing import Generic, TypeVar

from generated_symbols.base import GeneratedModel


E = TypeVar('E')

class ExplicitTagEntry(GeneratedModel, Generic[E]):
    id: E
    required: bool | None = None
