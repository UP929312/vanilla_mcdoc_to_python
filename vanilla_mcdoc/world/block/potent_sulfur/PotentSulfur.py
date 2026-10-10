"""
Generated from symbols.json for ::java::world::block::potent_sulfur::PotentSulfur
Local link to file: vanilla_mcdoc/world/block/potent_sulfur/PotentSulfur.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.world.block.BlockEntity import BlockEntity


class PotentSulfur(BlockEntity):
    countdown: int | None = None  # Time in seconds until the next state switch (between dormant and erupting).  The timer only counts down when the potent sulfur creates a valid geyser.  Negative values will be replaced with a new duration of the current state.
