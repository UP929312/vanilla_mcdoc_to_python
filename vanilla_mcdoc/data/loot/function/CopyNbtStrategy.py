"""
Generated from symbols.json for ::java::data::loot::function::CopyNbtStrategy
Local link to file: vanilla_mcdoc/data/loot/function/CopyNbtStrategy.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class CopyNbtStrategy(StrEnum):
    REPLACE = "replace"  # Replace any existing contents of the target.
    APPEND = "append"  # Append to a list.
    MERGE = "merge"  # Merge into a compound tag.
