"""
Generated from symbols.json for ::java::data::advancement::AdvancementFrame
Local link to file: vanilla_mcdoc/data/advancement/AdvancementFrame.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class AdvancementFrame(StrEnum):
    TASK = "task"  # Normal border.
    CHALLENGE = "challenge"  # Fancy spiked border (used for the kill all mobs advancement).
    GOAL = "goal"  # Rounded border (used for the full beacon advancement).
