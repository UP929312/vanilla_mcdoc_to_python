"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::TreeDecorator
Local link to file: vanilla_mcdoc/data/worldgen/feature/tree/TreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import Annotated, Literal

from pydantic import Discriminator, Tag

from vanilla_mcdoc.base import GeneratedModel, tag_of
from vanilla_mcdoc.data.worldgen.feature.tree.AlterGroundTreeDecorator import AlterGroundTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.AttachedToLeavesTreeDecorator import AttachedToLeavesTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.AttachedToLogsTreeDecorator import AttachedToLogsTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.BeehiveTreeDecorator import BeehiveTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.CocoaTreeDecorator import CocoaTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.CreakingHeartTreeDecorator import CreakingHeartTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.LeaveVineTreeDecorator import LeaveVineTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.PaleMossTreeDecorator import PaleMossTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.PlaceOnGroundTreeDecorator import PlaceOnGroundTreeDecorator
from vanilla_mcdoc.data.worldgen.feature.tree.ShelfMushroomTreeDecorator import ShelfMushroomTreeDecorator


class TreeDecoratorAlterGround(AlterGroundTreeDecorator):
    type: Literal['minecraft:alter_ground', 'alter_ground'] = 'minecraft:alter_ground'


class TreeDecoratorAttachedToLeaves(AttachedToLeavesTreeDecorator):
    type: Literal['minecraft:attached_to_leaves', 'attached_to_leaves'] = 'minecraft:attached_to_leaves'


class TreeDecoratorAttachedToLogs(AttachedToLogsTreeDecorator):
    type: Literal['minecraft:attached_to_logs', 'attached_to_logs'] = 'minecraft:attached_to_logs'


class TreeDecoratorBeehive(BeehiveTreeDecorator):
    type: Literal['minecraft:beehive', 'beehive'] = 'minecraft:beehive'


class TreeDecoratorCocoa(CocoaTreeDecorator):
    type: Literal['minecraft:cocoa', 'cocoa'] = 'minecraft:cocoa'


class TreeDecoratorCreakingHeart(CreakingHeartTreeDecorator):
    type: Literal['minecraft:creaking_heart', 'creaking_heart'] = 'minecraft:creaking_heart'


class TreeDecoratorLeaveVine(LeaveVineTreeDecorator):
    type: Literal['minecraft:leave_vine', 'leave_vine'] = 'minecraft:leave_vine'


class TreeDecoratorPaleMoss(PaleMossTreeDecorator):
    type: Literal['minecraft:pale_moss', 'pale_moss'] = 'minecraft:pale_moss'


class TreeDecoratorPlaceOnGround(PlaceOnGroundTreeDecorator):
    type: Literal['minecraft:place_on_ground', 'place_on_ground'] = 'minecraft:place_on_ground'


class TreeDecoratorShelfMushroom(ShelfMushroomTreeDecorator):
    type: Literal['minecraft:shelf_mushroom', 'shelf_mushroom'] = 'minecraft:shelf_mushroom'


class TreeDecoratorTrunkVine(GeneratedModel):
    type: Literal['minecraft:trunk_vine', 'trunk_vine'] = 'minecraft:trunk_vine'


type TreeDecorator = Annotated[
    Annotated[TreeDecoratorAlterGround, Tag('minecraft:alter_ground')]
    | Annotated[TreeDecoratorAttachedToLeaves, Tag('minecraft:attached_to_leaves')]
    | Annotated[TreeDecoratorAttachedToLogs, Tag('minecraft:attached_to_logs')]
    | Annotated[TreeDecoratorBeehive, Tag('minecraft:beehive')]
    | Annotated[TreeDecoratorCocoa, Tag('minecraft:cocoa')]
    | Annotated[TreeDecoratorCreakingHeart, Tag('minecraft:creaking_heart')]
    | Annotated[TreeDecoratorLeaveVine, Tag('minecraft:leave_vine')]
    | Annotated[TreeDecoratorPaleMoss, Tag('minecraft:pale_moss')]
    | Annotated[TreeDecoratorPlaceOnGround, Tag('minecraft:place_on_ground')]
    | Annotated[TreeDecoratorShelfMushroom, Tag('minecraft:shelf_mushroom')]
    | Annotated[TreeDecoratorTrunkVine, Tag('minecraft:trunk_vine')],
    Discriminator(tag_of('type')),
]
