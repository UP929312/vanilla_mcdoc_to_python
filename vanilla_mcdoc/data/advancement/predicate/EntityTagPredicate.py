"""
Generated from symbols.json for ::java::data::advancement::predicate::EntityTagPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/EntityTagPredicate.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class EntityTagPredicate(GeneratedModel):
    any_of: list[str] | None = None  # Must have at least one of the listed tags.
    all_of: list[str] | None = None  # Must have all the listed tags.
    none_of: list[str] | None = None  # Must have none of the listed tags.
