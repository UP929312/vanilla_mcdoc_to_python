"""
Generated from symbols.json for ::java::assets::model::ModelRef
Local link to file: vanilla_mcdoc/assets/model/ModelRef.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from vanilla_mcdoc.minecraft_types import IdSpec


type ModelRef = Annotated[str, IdSpec(registry='model', exclude=('builtin/generated', 'builtin/entity'))]
