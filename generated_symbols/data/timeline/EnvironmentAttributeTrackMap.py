"""
Generated from symbols.json for ::java::data::timeline::EnvironmentAttributeTrackMap
Local link to file: generated_symbols/data/timeline/EnvironmentAttributeTrackMap.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any, Literal

from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase
from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.util.MoonPhase import MoonPhase
    from generated_symbols.data.worldgen.attribute.AmbientParticle import AmbientParticle
    from generated_symbols.data.worldgen.attribute.AmbientSounds import AmbientSounds
    from generated_symbols.data.worldgen.attribute.BackgroundMusic import BackgroundMusic
    from generated_symbols.data.worldgen.attribute.BedRule import BedRule
    from generated_symbols.data.worldgen.attribute.TriState import TriState
    from generated_symbols.data.worldgen.attribute.modifier.BlendToGray import BlendToGray
    from generated_symbols.data.worldgen.attribute.modifier.BooleanModifierType import BooleanModifierType
    from generated_symbols.data.worldgen.attribute.modifier.ColorModifierType import ColorModifierType
    from generated_symbols.data.worldgen.attribute.modifier.FloatModifierType import FloatModifierType
    from generated_symbols.data.worldgen.attribute.modifier.FloatWithAlpha import FloatWithAlpha
    from generated_symbols.data.worldgen.attribute.modifier.ListModifierType import ListModifierType
    from generated_symbols.data.worldgen.attribute.modifier.MergeableModifierType import MergeableModifierType
    from generated_symbols.data.worldgen.biome.NaturalMobSpawns import NaturalMobSpawns
    from generated_symbols.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId
    from generated_symbols.util.color.StringARGB import StringARGB
    from generated_symbols.util.color.StringRGB import StringRGB
    from generated_symbols.util.particle.Particle import Particle


@dataclass(kw_only=True)
class KeyframesStruct:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: Any


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct1(AttributeTrackBase):
    modifier: Literal['override'] = 'override'
    keyframes: Annotated[list[KeyframesStruct], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct2:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: AmbientSounds


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct2(AttributeTrackBase):
    modifier: Literal['override'] = 'override'
    keyframes: Annotated[list[KeyframesStruct2], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct3:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: BackgroundMusic


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct3(AttributeTrackBase):
    modifier: Literal['override'] = 'override'
    keyframes: Annotated[list[KeyframesStruct3], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct4:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: bool


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct4(AttributeTrackBase):
    modifier: BooleanModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct4], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct5:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: Annotated[float, 'Range | `0`-`1` | both inclusive'] | float | FloatWithAlpha | Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct5(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct5], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct6:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: Annotated[str, IdSpec(registry='activity')]


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct6(AttributeTrackBase):
    modifier: Literal['override'] = 'override'
    keyframes: Annotated[list[KeyframesStruct6], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct7:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: BedRule


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct7(AttributeTrackBase):
    modifier: Literal['override'] = 'override'
    keyframes: Annotated[list[KeyframesStruct7], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct8:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: Annotated[float, 'Range | `0`-`0.9999999` | both inclusive'] | float | FloatWithAlpha | Annotated[float, 'Range | `0`-`0.9999999` | both inclusive']


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct8(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct8], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct9:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: TriState


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct9(AttributeTrackBase):
    modifier: Literal['override'] = 'override'
    keyframes: Annotated[list[KeyframesStruct9], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct10:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: NaturalMobSpawns


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct10(AttributeTrackBase):
    modifier: MergeableModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct10], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct11:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: Annotated[float, 'Range | `0`-`15` | both inclusive'] | float | FloatWithAlpha | Annotated[float, 'Range | `0`-`15` | both inclusive']


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct11(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct11], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct12:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: StringRGB | StringARGB | BlendToGray


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct12(AttributeTrackBase):
    modifier: ColorModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct12], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct13:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: list[AmbientParticle]


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct13(AttributeTrackBase):
    modifier: ListModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct13], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct14:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: StringARGB | StringRGB | BlendToGray | StringRGB | StringARGB


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct14(AttributeTrackBase):
    modifier: ColorModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct14], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct15:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: Annotated[float, 'Range | `0` and above | inclusive'] | float | FloatWithAlpha | Annotated[float, 'Range | `0` and above | inclusive']


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct15(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct15], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct16:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: float | FloatWithAlpha | float


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct16(AttributeTrackBase):
    modifier: FloatModifierType | None = None
    keyframes: Annotated[list[KeyframesStruct16], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct17:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: Particle


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct17(AttributeTrackBase):
    modifier: Literal['override'] = 'override'
    keyframes: Annotated[list[KeyframesStruct17], 'Length = 1 (inclusive) and above']


@dataclass(kw_only=True)
class KeyframesStruct18:
    ticks: Annotated[int, 'Range | `0` and above | inclusive']
    value: MoonPhase


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct18(AttributeTrackBase):
    modifier: Literal['override'] = 'override'
    keyframes: Annotated[list[KeyframesStruct18], 'Length = 1 (inclusive) and above']


type EnvironmentAttributeTrackMap = dict[Annotated[str, IdSpec(registry='environment_attribute')] | KnownEnvironmentAttributeId, EnvironmentAttributeTrackMapValueStruct1 | EnvironmentAttributeTrackMapValueStruct2 | EnvironmentAttributeTrackMapValueStruct3 | EnvironmentAttributeTrackMapValueStruct4 | EnvironmentAttributeTrackMapValueStruct5 | EnvironmentAttributeTrackMapValueStruct6 | EnvironmentAttributeTrackMapValueStruct7 | EnvironmentAttributeTrackMapValueStruct8 | EnvironmentAttributeTrackMapValueStruct9 | EnvironmentAttributeTrackMapValueStruct10 | EnvironmentAttributeTrackMapValueStruct11 | EnvironmentAttributeTrackMapValueStruct12 | EnvironmentAttributeTrackMapValueStruct13 | EnvironmentAttributeTrackMapValueStruct14 | EnvironmentAttributeTrackMapValueStruct15 | EnvironmentAttributeTrackMapValueStruct16 | EnvironmentAttributeTrackMapValueStruct17 | EnvironmentAttributeTrackMapValueStruct18]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::timeline::EnvironmentAttributeTrackMap": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "environment_attribute"
                                }
                            }
                        }
                    ]
                },
                "type": {
                    "kind": "indexed",
                    "child": {
                        "kind": "dispatcher",
                        "parallelIndices": [
                            {
                                "kind": "dynamic",
                                "accessor": [
                                    {
                                        "keyword": "key"
                                    }
                                ]
                            }
                        ],
                        "registry": "minecraft:environment_attribute"
                    },
                    "parallelIndices": [
                        {
                            "kind": "static",
                            "value": "attribute_track"
                        }
                    ]
                }
            }
        ]
    }
}

