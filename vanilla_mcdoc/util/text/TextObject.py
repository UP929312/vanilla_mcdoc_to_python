"""
Generated from symbols.json for ::java::util::text::TextObject
Local link to file: vanilla_mcdoc/util/text/TextObject.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec
from vanilla_mcdoc.util.text.ObjectTextConfig import ObjectTextConfig
from vanilla_mcdoc.util.text.TextBase import TextBase
from vanilla_mcdoc.util.text.TextNbtBase import TextNbtBase

if TYPE_CHECKING:
    from vanilla_mcdoc.util.avatar.Profile import Profile
    from vanilla_mcdoc.util.text.Keybind import Keybind
    from vanilla_mcdoc.util.text.Text import Text
    from vanilla_mcdoc.util.text.TranslationArg import TranslationArg


class ScoreStruct(GeneratedModel):
    objective: str
    name: str


class TextObjectStruct1(TextBase):
    text: str
    type: Literal['text'] | None = 'text'


class TextObjectStruct2(TextBase):
    translate: str
    fallback: str | None = None
    with_: Annotated[list[TranslationArg], Field(min_length=1)] | None = Field(default=None, alias='with')
    type: Literal['translatable'] | None = 'translatable'


class TextObjectStruct3(TextBase):
    score: ScoreStruct
    type: Literal['score'] | None = 'score'


class TextObjectStruct4(TextBase):
    selector: str
    separator: Text | None = None
    type: Literal['selector'] | None = 'selector'


class TextObjectStruct5(TextBase):
    keybind: Keybind
    type: Literal['keybind'] | None = 'keybind'


class TextObjectStruct6(TextNbtBase):
    block: str
    nbt: str
    source: Literal['block'] | None = 'block'
    type: Literal['nbt'] | None = 'nbt'


class TextObjectStruct7(TextNbtBase):
    entity: str
    nbt: str
    source: Literal['entity'] | None = 'entity'
    type: Literal['nbt'] | None = 'nbt'


class TextObjectStruct8(TextNbtBase):
    storage: Annotated[str, IdSpec(registry='storage')]
    nbt: str
    source: Literal['storage'] | None = 'storage'
    type: Literal['nbt'] | None = 'nbt'


class TextObjectStruct9(ObjectTextConfig, TextBase):
    atlas: Annotated[str, IdSpec(registry='atlas')] | None = None  # Defaults to `minecraft:blocks`.
    sprite: Annotated[str, IdSpec(registry='texture')]
    object: Literal['atlas'] | None = 'atlas'
    type: Literal['object'] | None = 'object'


class TextObjectStruct10(ObjectTextConfig, TextBase):
    player: Profile
    hat: bool | None = None  # Whether the head layer is rendered. Defaults to `true`.
    object: Literal['player'] | None = 'player'
    type: Literal['object'] | None = 'object'


type TextObject = TextObjectStruct1 | TextObjectStruct2 | TextObjectStruct3 | TextObjectStruct4 | TextObjectStruct5 | TextObjectStruct6 | TextObjectStruct7 | TextObjectStruct8 | TextObjectStruct9 | TextObjectStruct10
