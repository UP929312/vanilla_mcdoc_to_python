"""
Generated from symbols.json for ::java::world::block::conduit::TargetUuid
Local link to file: vanilla_mcdoc/world/block/conduit/TargetUuid.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class TargetUuid(GeneratedModel):
    M: int | None = None  # Upper bits of the target's UUID
    L: int | None = None  # Lower bits of the target's UUID
