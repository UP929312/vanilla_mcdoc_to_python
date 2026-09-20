# ~~~ WHAT ARE WE TESTING ~~~

# This has the weird `...::tag::E` thing, ensure it's working properly.

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::data::tag::ExplicitTagEntry
Local link to file: generated_symbols/data/tag/ExplicitTagEntry.py
"""
# ~~~ CODE ~~~
from pydantic import BaseModel
from typing import Generic, TypeVar


E = TypeVar('E')

class ExplicitTagEntry(BaseModel, Generic[E]):
    id: E
    required: bool | None = None


