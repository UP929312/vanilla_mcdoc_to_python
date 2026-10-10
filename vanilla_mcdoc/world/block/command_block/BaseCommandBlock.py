"""
Generated from symbols.json for ::java::world::block::command_block::BaseCommandBlock
Local link to file: vanilla_mcdoc/world/block/command_block/BaseCommandBlock.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.util.text.Text import Text


class BaseCommandBlock(GeneratedModel):
    Command: str | None = None  # The command to run.
    SuccessCount: int | None = None  # Success count of the last command.
    LastOutput: Text | None = None  # Output of the last command.
    TrackOutput: bool | None = None  # Whether to record command output.
    UpdateLastExecution: bool | None = None  # Whether to record the tick of the latest command execution.
    LastExecution: int | None = None  # Tick of the latest command execution.
