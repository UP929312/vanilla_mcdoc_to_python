"""
Generated from symbols.json for ::java::data::worldgen::feature::tree::TreeDecorator
Local link to file: generated_symbols/data/worldgen/feature/tree/TreeDecorator.py
"""
# ~~~ CODE ~~~
from typing import Literal

from generated_symbols.data.worldgen.feature.tree.AlterGroundTreeDecorator import AlterGroundTreeDecorator
from generated_symbols.data.worldgen.feature.tree.AttachedToLeavesTreeDecorator import AttachedToLeavesTreeDecorator
from generated_symbols.data.worldgen.feature.tree.AttachedToLogsTreeDecorator import AttachedToLogsTreeDecorator
from generated_symbols.data.worldgen.feature.tree.BeehiveTreeDecorator import BeehiveTreeDecorator
from generated_symbols.data.worldgen.feature.tree.CocoaTreeDecorator import CocoaTreeDecorator
from generated_symbols.data.worldgen.feature.tree.CreakingHeartTreeDecorator import CreakingHeartTreeDecorator
from generated_symbols.data.worldgen.feature.tree.LeaveVineTreeDecorator import LeaveVineTreeDecorator
from generated_symbols.data.worldgen.feature.tree.PaleMossTreeDecorator import PaleMossTreeDecorator
from generated_symbols.data.worldgen.feature.tree.PlaceOnGroundTreeDecorator import PlaceOnGroundTreeDecorator
from generated_symbols.data.worldgen.feature.tree.ShelfMushroomTreeDecorator import ShelfMushroomTreeDecorator


class TreeDecoratorAlterGround(AlterGroundTreeDecorator):
    type: Literal['minecraft:alter_ground'] = 'minecraft:alter_ground'


class TreeDecoratorAttachedToLeaves(AttachedToLeavesTreeDecorator):
    type: Literal['minecraft:attached_to_leaves'] = 'minecraft:attached_to_leaves'


class TreeDecoratorAttachedToLogs(AttachedToLogsTreeDecorator):
    type: Literal['minecraft:attached_to_logs'] = 'minecraft:attached_to_logs'


class TreeDecoratorBeehive(BeehiveTreeDecorator):
    type: Literal['minecraft:beehive'] = 'minecraft:beehive'


class TreeDecoratorCocoa(CocoaTreeDecorator):
    type: Literal['minecraft:cocoa'] = 'minecraft:cocoa'


class TreeDecoratorCreakingHeart(CreakingHeartTreeDecorator):
    type: Literal['minecraft:creaking_heart'] = 'minecraft:creaking_heart'


class TreeDecoratorLeaveVine(LeaveVineTreeDecorator):
    type: Literal['minecraft:leave_vine'] = 'minecraft:leave_vine'


class TreeDecoratorPaleMoss(PaleMossTreeDecorator):
    type: Literal['minecraft:pale_moss'] = 'minecraft:pale_moss'


class TreeDecoratorPlaceOnGround(PlaceOnGroundTreeDecorator):
    type: Literal['minecraft:place_on_ground'] = 'minecraft:place_on_ground'


class TreeDecoratorShelfMushroom(ShelfMushroomTreeDecorator):
    type: Literal['minecraft:shelf_mushroom'] = 'minecraft:shelf_mushroom'


type TreeDecorator = TreeDecoratorAlterGround | TreeDecoratorAttachedToLeaves | TreeDecoratorAttachedToLogs | TreeDecoratorBeehive | TreeDecoratorCocoa | TreeDecoratorCreakingHeart | TreeDecoratorLeaveVine | TreeDecoratorPaleMoss | TreeDecoratorPlaceOnGround | TreeDecoratorShelfMushroom


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::tree::TreeDecorator": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "type",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "worldgen/tree_decorator_type"
                                }
                            }
                        }
                    ]
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "type"
                            ]
                        }
                    ],
                    "registry": "minecraft:tree_decorator"
                }
            }
        ]
    }
}

