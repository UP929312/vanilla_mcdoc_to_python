"""Vanilla's assets/waypoint_style/ files"""
from vanilla_mcdoc.assets.waypoint_style.WaypointStyle import WaypointStyle

BOWTIE = WaypointStyle(
    near_distance=64,
    sprites=['minecraft:bowtie', 'minecraft:default_0', 'minecraft:default_1', 'minecraft:default_2', 'minecraft:default_3'],
)

DEFAULT = WaypointStyle(sprites=['minecraft:default_0', 'minecraft:default_1', 'minecraft:default_2', 'minecraft:default_3'])
