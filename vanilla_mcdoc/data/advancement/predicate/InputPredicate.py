"""
Generated from symbols.json for ::java::data::advancement::predicate::InputPredicate
Local link to file: vanilla_mcdoc/data/advancement/predicate/InputPredicate.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class InputPredicate(GeneratedModel):
    forward: bool | None = None
    backward: bool | None = None
    left: bool | None = None
    right: bool | None = None
    jump: bool | None = None
    sneak: bool | None = None
    sprint: bool | None = None
