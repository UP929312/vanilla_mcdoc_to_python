"""
Generated from symbols.json for ::java::world::block::end_gateway::EndGateway
Local link to file: vanilla_mcdoc/world/block/end_gateway/EndGateway.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity


class EndGateway(BlockEntity):
    Age: int | None = None  # In game ticks.
    ExactTeleport: bool | None = None  # Whether to teleport to the exact location.
    exit_portal: tuple[int, int, int] | None = None  # Coordinates of where to teleport entities to.
