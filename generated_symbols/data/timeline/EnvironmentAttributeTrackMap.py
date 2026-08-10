"""
Generated from symbols.json for ::java::data::timeline::EnvironmentAttributeTrackMap
Local link to file: generated_symbols/data/timeline/EnvironmentAttributeTrackMap.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any, Generic, Literal, TypeVar

from generated_symbols.data.timeline.AttributeTrackBase import AttributeTrackBase
from runtime_metadata import IdSpec

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
    from generated_symbols.util.color.StringARGB import StringARGB
    from generated_symbols.util.color.StringRGB import StringRGB
    from generated_symbols.util.particle.Particle import Particle


T = TypeVar('T')

@dataclass(kw_only=True)
class KeyframesStruct:
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: Any


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct1(AttributeTrackBase):
    keyframes: Annotated[list[KeyframesStruct], 'Length = 1 (inclusive) and above']
    modifier: Literal['override'] | None = None


@dataclass(kw_only=True)
class KeyframesStruct:
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: AmbientSounds


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct2(AttributeTrackBase):
    keyframes: Annotated[list[KeyframesStruct], 'Length = 1 (inclusive) and above']
    modifier: Literal['override'] | None = None


@dataclass(kw_only=True)
class KeyframesStruct:
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: BackgroundMusic


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct3(AttributeTrackBase):
    keyframes: Annotated[list[KeyframesStruct], 'Length = 1 (inclusive) and above']
    modifier: Literal['override'] | None = None


@dataclass(kw_only=True)
class KeyframesStruct:
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: bool


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct4(AttributeTrackBase):
    keyframes: Annotated[list[KeyframesStruct], 'Length = 1 (inclusive) and above']
    modifier: BooleanModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: T | float | FloatWithAlpha[Annotated[float, 'Range | `0`-`1` | both inclusive']] | Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct5(AttributeTrackBase):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: FloatModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: Annotated[str, IdSpec(registry='activity')]


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct6(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: Literal['override'] | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: BedRule


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct7(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: Literal['override'] | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: T | float | FloatWithAlpha[Annotated[float, 'Range | `0`-`0.9999999` | both inclusive']] | Annotated[float, 'Range | `0`-`0.9999999` | both inclusive']


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct8(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: FloatModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: TriState


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct9(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: Literal['override'] | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: NaturalMobSpawns


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct10(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: MergeableModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: T | float | FloatWithAlpha[Annotated[float, 'Range | `0`-`15` | both inclusive']] | Annotated[float, 'Range | `0`-`15` | both inclusive']


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct11(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: FloatModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: StringRGB | StringARGB | BlendToGray


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct12(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: ColorModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: list[AmbientParticle]


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct13(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: ListModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: StringARGB | StringRGB | BlendToGray | StringRGB | StringARGB


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct14(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: ColorModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: T | float | FloatWithAlpha[Annotated[float, 'Range | Min `0` and above | inclusive']] | Annotated[float, 'Range | Min `0` and above | inclusive']


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct15(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: FloatModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: T | float | FloatWithAlpha[float] | float


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct16(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: FloatModifierType | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: Particle


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct17(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: Literal['override'] | None = None


@dataclass(kw_only=True)
class KeyframesStruct(Generic[T]):
    ticks: Annotated[int, 'Range | Min `0` and above | inclusive']
    value: MoonPhase


@dataclass(kw_only=True)
class EnvironmentAttributeTrackMapValueStruct18(AttributeTrackBase, Generic[T]):
    keyframes: Annotated[list[KeyframesStruct[T]], 'Length = 1 (inclusive) and above']
    modifier: Literal['override'] | None = None


type EnvironmentAttributeTrackMap[T] = dict[Annotated[str, IdSpec(registry='environment_attribute')], EnvironmentAttributeTrackMapValueStruct1 | EnvironmentAttributeTrackMapValueStruct2 | EnvironmentAttributeTrackMapValueStruct3 | EnvironmentAttributeTrackMapValueStruct4 | EnvironmentAttributeTrackMapValueStruct5[T] | EnvironmentAttributeTrackMapValueStruct6[T] | EnvironmentAttributeTrackMapValueStruct7[T] | EnvironmentAttributeTrackMapValueStruct8[T] | EnvironmentAttributeTrackMapValueStruct9[T] | EnvironmentAttributeTrackMapValueStruct10[T] | EnvironmentAttributeTrackMapValueStruct11[T] | EnvironmentAttributeTrackMapValueStruct12[T] | EnvironmentAttributeTrackMapValueStruct13[T] | EnvironmentAttributeTrackMapValueStruct14[T] | EnvironmentAttributeTrackMapValueStruct15[T] | EnvironmentAttributeTrackMapValueStruct16[T] | EnvironmentAttributeTrackMapValueStruct17[T] | EnvironmentAttributeTrackMapValueStruct18[T]]


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

