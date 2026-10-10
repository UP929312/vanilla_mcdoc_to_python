"""
Generated from symbols.json for ::java::util::text::ScoreText
Local link to file: vanilla_mcdoc/util/text/ScoreText.py
"""
# ~~~ CODE ~~~
from typing import Literal

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.util.text.TextBase import TextBase


class ScoreStruct(GeneratedModel):
    objective: str
    name: str


class ScoreText(TextBase):
    score: ScoreStruct
    type: Literal['score'] | None = 'score'
