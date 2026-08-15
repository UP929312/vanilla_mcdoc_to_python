"""
Generated from symbols.json for ::java::assets::item_definition::ModelTint
Local link to file: generated_symbols/assets/item_definition/ModelTint.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

if TYPE_CHECKING:
    from generated_symbols.assets.item_definition.ActuallyTranslucentRGB import ActuallyTranslucentRGB
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class ModelTintConstant:
    type: Literal['minecraft:constant']
    value: RGB  # Constant tint color to apply.


@dataclass(kw_only=True)
class ModelTintCustomModelData:
    type: Literal['minecraft:custom_model_data']
    index: Annotated[int, 'Range | Min `0` and above | inclusive'] | None = None  # The index of the `colors` list in the `custom_model_data` component. Defaults to 0.
    default: RGB  # Tint to apply when the `custom_model_data` component is not present, or when it doesn't have a color in the specified index.


@dataclass(kw_only=True)
class ModelTintDye:
    type: Literal['minecraft:dye']
    default: ActuallyTranslucentRGB  # Tint to apply when the `dyed_color` component is not present.


@dataclass(kw_only=True)
class ModelTintFirework:
    type: Literal['minecraft:firework']
    default: ActuallyTranslucentRGB  # Tint to apply when the `firework_explosion` component is not present.


@dataclass(kw_only=True)
class ModelTintGrass:
    type: Literal['minecraft:grass']
    temperature: Annotated[float, 'Range | `0`-`1` | both inclusive']
    downfall: Annotated[float, 'Range | `0`-`1` | both inclusive']


@dataclass(kw_only=True)
class ModelTintMapColor:
    type: Literal['minecraft:map_color']
    default: RGB  # Tint to apply when the `map_color` component is not present.


@dataclass(kw_only=True)
class ModelTintPotion:
    type: Literal['minecraft:potion']
    default: RGB  # Tint to apply when the `potion_contents` component is not present, or it has no effects and no `custom_color` is set.


@dataclass(kw_only=True)
class ModelTintTeam:
    type: Literal['minecraft:team']
    default: RGB  # Tint to apply when there is no context entity, entity is not in a team or the team has no color.


type ModelTint = ModelTintConstant | ModelTintCustomModelData | ModelTintDye | ModelTintFirework | ModelTintGrass | ModelTintMapColor | ModelTintPotion | ModelTintTeam


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::ModelTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "reference",
                    "path": "::java::assets::item_definition::TintSourceType",
                    "attributes": [
                        {
                            "name": "id"
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:tint_source"
                }
            }
        ]
    }
}

