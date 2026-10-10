"""
Generated from symbols.json for ::java::data::timeline::EnvironmentAttributeTrackMap
Local link to file: vanilla_mcdoc/data/timeline/EnvironmentAttributeTrackMap.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated, Any, Literal

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.data.timeline.AttributeTrackBase import AttributeTrackBase
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.data.util.MoonPhase import MoonPhase
    from vanilla_mcdoc.data.worldgen.attribute.AmbientParticle import AmbientParticle
    from vanilla_mcdoc.data.worldgen.attribute.AmbientSounds import AmbientSounds
    from vanilla_mcdoc.data.worldgen.attribute.BackgroundMusic import BackgroundMusic
    from vanilla_mcdoc.data.worldgen.attribute.BedRule import BedRule
    from vanilla_mcdoc.data.worldgen.attribute.TriState import TriState
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatModifierType import FloatModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.FloatWithAlpha import FloatWithAlpha
    from vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifierType import ListModifierType
    from vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType
    from vanilla_mcdoc.data.worldgen.biome.NaturalMobSpawns import NaturalMobSpawns
    from vanilla_mcdoc.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId
    from vanilla_mcdoc.util.color.StringARGB import StringARGB
    from vanilla_mcdoc.util.color.StringRGB import StringRGB
    from vanilla_mcdoc.util.particle.Particle import Particle


class KeyframesStruct(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: Any


class EnvironmentAttributeTrackMapValueStruct1(AttributeTrackBase):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct], Field(min_length=1)]


class KeyframesStruct2(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: AmbientSounds


class EnvironmentAttributeTrackMapValueStruct2(AttributeTrackBase):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct2], Field(min_length=1)]


class KeyframesStruct3(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: BackgroundMusic


class EnvironmentAttributeTrackMapValueStruct3(AttributeTrackBase):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct3], Field(min_length=1)]


class KeyframesStruct4(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: bool


class EnvironmentAttributeTrackMapValueStruct4(AttributeTrackBase):
    modifier: BooleanModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct4], Field(min_length=1)]


class KeyframesStruct5(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: Annotated[float, Field(ge=0, le=1)] | float | FloatWithAlpha | Annotated[float, Field(ge=0, le=1)]


class EnvironmentAttributeTrackMapValueStruct5(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct5], Field(min_length=1)]


class KeyframesStruct6(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: Annotated[str, IdSpec(registry='activity')]


class EnvironmentAttributeTrackMapValueStruct6(AttributeTrackBase):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct6], Field(min_length=1)]


class KeyframesStruct7(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: BedRule


class EnvironmentAttributeTrackMapValueStruct7(AttributeTrackBase):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct7], Field(min_length=1)]


class KeyframesStruct8(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: Annotated[float, Field(ge=0, le=0.9999999)] | float | FloatWithAlpha | Annotated[float, Field(ge=0, le=0.9999999)]


class EnvironmentAttributeTrackMapValueStruct8(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct8], Field(min_length=1)]


class KeyframesStruct9(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: TriState


class EnvironmentAttributeTrackMapValueStruct9(AttributeTrackBase):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct9], Field(min_length=1)]


class KeyframesStruct10(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: NaturalMobSpawns


class EnvironmentAttributeTrackMapValueStruct10(AttributeTrackBase):
    modifier: MergeableModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct10], Field(min_length=1)]


class KeyframesStruct11(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: Annotated[float, Field(ge=0, le=15)] | float | FloatWithAlpha | Annotated[float, Field(ge=0, le=15)]


class EnvironmentAttributeTrackMapValueStruct11(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct11], Field(min_length=1)]


class KeyframesStruct12(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: StringRGB | StringARGB | BlendToGray


class EnvironmentAttributeTrackMapValueStruct12(AttributeTrackBase):
    modifier: ColorModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct12], Field(min_length=1)]


class KeyframesStruct13(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: list[AmbientParticle]


class EnvironmentAttributeTrackMapValueStruct13(AttributeTrackBase):
    modifier: ListModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct13], Field(min_length=1)]


class KeyframesStruct14(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: StringARGB | StringRGB | BlendToGray | StringRGB | StringARGB


class EnvironmentAttributeTrackMapValueStruct14(AttributeTrackBase):
    modifier: ColorModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct14], Field(min_length=1)]


class KeyframesStruct15(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: Annotated[float, Field(ge=0)] | float | FloatWithAlpha | Annotated[float, Field(ge=0)]


class EnvironmentAttributeTrackMapValueStruct15(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct15], Field(min_length=1)]


class KeyframesStruct16(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: float | FloatWithAlpha | float


class EnvironmentAttributeTrackMapValueStruct16(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct16], Field(min_length=1)]


class KeyframesStruct17(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: Particle


class EnvironmentAttributeTrackMapValueStruct17(AttributeTrackBase):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct17], Field(min_length=1)]


class KeyframesStruct18(GeneratedModel):
    ticks: Annotated[int, Field(ge=0)]
    value: MoonPhase


class EnvironmentAttributeTrackMapValueStruct18(AttributeTrackBase):
    modifier: Literal['override'] | None = 'override'
    keyframes: Annotated[list[KeyframesStruct18], Field(min_length=1)]


type EnvironmentAttributeTrackMap = dict[Annotated[str, IdSpec(registry='environment_attribute')] | KnownEnvironmentAttributeId, EnvironmentAttributeTrackMapValueStruct1 | EnvironmentAttributeTrackMapValueStruct2 | EnvironmentAttributeTrackMapValueStruct3 | EnvironmentAttributeTrackMapValueStruct4 | EnvironmentAttributeTrackMapValueStruct5 | EnvironmentAttributeTrackMapValueStruct6 | EnvironmentAttributeTrackMapValueStruct7 | EnvironmentAttributeTrackMapValueStruct8 | EnvironmentAttributeTrackMapValueStruct9 | EnvironmentAttributeTrackMapValueStruct10 | EnvironmentAttributeTrackMapValueStruct11 | EnvironmentAttributeTrackMapValueStruct12 | EnvironmentAttributeTrackMapValueStruct13 | EnvironmentAttributeTrackMapValueStruct14 | EnvironmentAttributeTrackMapValueStruct15 | EnvironmentAttributeTrackMapValueStruct16 | EnvironmentAttributeTrackMapValueStruct17 | EnvironmentAttributeTrackMapValueStruct18]
