"""
Generated from symbols.json for ::java::assets::equipment::Layers
Local link to file: vanilla_mcdoc/assets/equipment/Layers.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING, Annotated

from vanilla_mcdoc.base import GeneratedModel
from vanilla_mcdoc.minecraft_types import IdSpec

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.equipment.Layer import Layer
    from vanilla_mcdoc.assets.equipment.WingsLayer import WingsLayer


class Layers(GeneratedModel):
    humanoid: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/humanoid/')]]] | None = None
    humanoid_leggings: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/humanoid_leggings/')]]] | None = None
    humanoid_baby: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/humanoid_baby/')]]] | None = None
    wings: list[WingsLayer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/wings/')]]] | None = None
    wolf_body: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/wolf_body/')]]] | None = None
    horse_body: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/horse_body/')]]] | None = None
    llama_body: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/llama_body/')]]] | None = None
    happy_ghast_body: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/happy_ghast_body/')]]] | None = None
    nautilus_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/nautilus_saddle/')]]] | None = None
    nautilus_body: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/nautilus_body/')]]] | None = None
    pig_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/pig_saddle/')]]] | None = None
    strider_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/strider_saddle/')]]] | None = None
    camel_husk_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/camel_husk_saddle/')]]] | None = None
    camel_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/camel_saddle/')]]] | None = None
    horse_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/horse_saddle/')]]] | None = None
    donkey_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/donkey_saddle/')]]] | None = None
    mule_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/mule_saddle/')]]] | None = None
    zombie_horse_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/zombie_horse_saddle/')]]] | None = None
    skeleton_horse_saddle: list[Layer[Annotated[str, IdSpec(registry='texture', path='entity/equipment/skeleton_horse_saddle/')]]] | None = None
