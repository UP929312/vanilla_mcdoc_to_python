"""
Generated from symbols.json for ::java::util::text::PlayerHeadText
Local link to file: vanilla_mcdoc/util/text/PlayerHeadText.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Literal

from vanilla_mcdoc.util.text.ObjectTextConfig import ObjectTextConfig
from vanilla_mcdoc.util.text.TextBase import TextBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.avatar.Profile import Profile


class PlayerHeadText(ObjectTextConfig, TextBase):
    player: Profile
    hat: bool | None = None  # Whether the head layer is rendered. Defaults to `true`.
    object: Literal['player'] | None = 'player'
    type: Literal['object'] | None = 'object'
