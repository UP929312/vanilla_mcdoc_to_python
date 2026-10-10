"""
Generated from symbols.json for ::java::util::memory::ExpirableValue
Local link to file: vanilla_mcdoc/util/memory/ExpirableValue.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class ExpirableValue(GeneratedModel):
    ttl: int | None = None  # If present, ticks before this memory is automatically removed.
