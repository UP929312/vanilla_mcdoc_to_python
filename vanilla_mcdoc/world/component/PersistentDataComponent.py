"""
Generated from symbols.json for ::java::world::component::PersistentDataComponent
Local link to file: vanilla_mcdoc/world/component/PersistentDataComponent.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type PersistentDataComponent = Annotated[str, IdSpec(registry='data_component_type', exclude=('additional_trade_cost', 'creative_slot_lock', 'map_post_processing'))]
