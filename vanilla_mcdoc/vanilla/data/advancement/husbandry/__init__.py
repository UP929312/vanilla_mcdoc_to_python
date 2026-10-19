"""Vanilla's data/advancement/husbandry/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionAllayDropItemOnBlock, AdvancementCriterionBeeNestDestroyed, AdvancementCriterionBredAnimals, AdvancementCriterionConsumeItem, AdvancementCriterionEffectsChanged, AdvancementCriterionFilledBucket, AdvancementCriterionFishingRodHooked, AdvancementCriterionInventoryChanged, AdvancementCriterionItemUsedOnBlock, AdvancementCriterionPlacedBlock, AdvancementCriterionPlayerInteractedWithEntity, AdvancementCriterionPlayerShearedEquipment, AdvancementCriterionStartedRiding, AdvancementCriterionTameAnimal, AdvancementCriterionThrownItemPickedUpByEntity, AdvancementCriterionThrownItemPickedUpByPlayer
from vanilla_mcdoc.data.advancement.AdvancementDisplay import AdvancementDisplay
from vanilla_mcdoc.data.advancement.AdvancementFrame import AdvancementFrame
from vanilla_mcdoc.data.advancement.AdvancementRewards import AdvancementRewards
from vanilla_mcdoc.data.advancement.RootAdvancementDisplay import RootAdvancementDisplay
from vanilla_mcdoc.data.advancement.predicate.BlockPredicate import BlockPredicate
from vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate import EnchantmentPredicate
from vanilla_mcdoc.data.advancement.predicate.EntityFlagsPredicate import EntityFlagsPredicate
from vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap import EntitySubPredicateMap
from vanilla_mcdoc.data.advancement.predicate.EquipmentPredicateSlot import EquipmentPredicateSlot
from vanilla_mcdoc.data.advancement.predicate.ItemPredicate import ItemPredicate
from vanilla_mcdoc.data.advancement.predicate.LocationPredicate import LocationPredicate
from vanilla_mcdoc.data.advancement.trigger.BeeNestDestroyedTrigger import BeeNestDestroyedTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.BredAnimalsTrigger import BredAnimalsTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.ConsumeItemTrigger import ConsumeItemTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.EffectsChangedTrigger import EffectsChangedTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.FilledBucketTrigger import FilledBucketTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.FishingRodHookedTrigger import FishingRodHookedTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.InventoryChangeTrigger import InventoryChangeTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.ItemUesdOnLocationConditions import ItemUesdOnLocationConditions
from vanilla_mcdoc.data.advancement.trigger.PickedUpItemTrigger import PickedUpItemTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.PlayerConditions import PlayerConditions
from vanilla_mcdoc.data.advancement.trigger.PlayerInteractTrigger import PlayerInteractTriggerTypeArg
from vanilla_mcdoc.data.advancement.trigger.TameAnimalTrigger import TameAnimalTriggerTypeArg
from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget
from vanilla_mcdoc.data.loot.condition.LootCondition import LootConditionAllOf, LootConditionEntityProperties, LootConditionLocationCheck, LootConditionMatchBlock, LootConditionMatchTool
from vanilla_mcdoc.data.util.MinMaxBounds import MinMaxBounds
from vanilla_mcdoc.util.text.TextObject import TextObjectStruct2
from vanilla_mcdoc.world.component.DataComponentExactPredicate import DataComponentExactPredicate
from vanilla_mcdoc.world.item.ItemStackOfComponent import ItemStackOfComponent

ALLAY_DELIVER_CAKE_TO_NOTE_BLOCK = Advancement(
    parent='minecraft:husbandry/allay_deliver_item_to_player',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:note_block'),
        title=TextObjectStruct2(translate='advancements.husbandry.allay_deliver_cake_to_note_block.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.allay_deliver_cake_to_note_block.description'),
        hidden=True,
    ),
    criteria={
        'allay_deliver_cake_to_note_block': AdvancementCriterionAllayDropItemOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(block=BlockPredicate(blocks='minecraft:note_block')),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(items='minecraft:cake'),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:allay_drop_item_on_block',
        ),
    },
    requirements=[['allay_deliver_cake_to_note_block']],
    sends_telemetry_event=True,
)

ALLAY_DELIVER_ITEM_TO_PLAYER = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:cookie'),
        title=TextObjectStruct2(translate='advancements.husbandry.allay_deliver_item_to_player.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.allay_deliver_item_to_player.description'),
        hidden=True,
    ),
    criteria={
        'allay_deliver_item_to_player': AdvancementCriterionThrownItemPickedUpByPlayer(
            conditions=PickedUpItemTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:allay'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:thrown_item_picked_up_by_player',
        ),
    },
    requirements=[['allay_deliver_item_to_player']],
    sends_telemetry_event=True,
)

AXOLOTL_IN_A_BUCKET = Advancement(
    parent='minecraft:husbandry/tactical_fishing',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:axolotl_bucket'),
        title=TextObjectStruct2(translate='advancements.husbandry.axolotl_in_a_bucket.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.axolotl_in_a_bucket.description'),
    ),
    criteria={
        'axolotl_bucket': AdvancementCriterionFilledBucket(
            conditions=FilledBucketTriggerTypeArg(item=ItemPredicate(items='minecraft:axolotl_bucket')),
            trigger='minecraft:filled_bucket',
        ),
    },
    requirements=[['axolotl_bucket']],
    sends_telemetry_event=True,
)

BALANCED_DIET = Advancement(
    parent='minecraft:husbandry/plant_seed',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:apple'),
        title=TextObjectStruct2(translate='advancements.husbandry.balanced_diet.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.balanced_diet.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'apple': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:apple')),
            trigger='minecraft:consume_item',
        ),
        'baked_potato': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:baked_potato')),
            trigger='minecraft:consume_item',
        ),
        'beef': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:beef')),
            trigger='minecraft:consume_item',
        ),
        'beetroot': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:beetroot')),
            trigger='minecraft:consume_item',
        ),
        'beetroot_soup': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:beetroot_soup')),
            trigger='minecraft:consume_item',
        ),
        'bread': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:bread')),
            trigger='minecraft:consume_item',
        ),
        'carrot': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:carrot')),
            trigger='minecraft:consume_item',
        ),
        'chicken': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:chicken')),
            trigger='minecraft:consume_item',
        ),
        'chorus_fruit': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:chorus_fruit')),
            trigger='minecraft:consume_item',
        ),
        'cod': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cod')),
            trigger='minecraft:consume_item',
        ),
        'cooked_beef': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cooked_beef')),
            trigger='minecraft:consume_item',
        ),
        'cooked_chicken': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cooked_chicken')),
            trigger='minecraft:consume_item',
        ),
        'cooked_cod': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cooked_cod')),
            trigger='minecraft:consume_item',
        ),
        'cooked_mutton': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cooked_mutton')),
            trigger='minecraft:consume_item',
        ),
        'cooked_porkchop': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cooked_porkchop')),
            trigger='minecraft:consume_item',
        ),
        'cooked_rabbit': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cooked_rabbit')),
            trigger='minecraft:consume_item',
        ),
        'cooked_salmon': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cooked_salmon')),
            trigger='minecraft:consume_item',
        ),
        'cookie': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:cookie')),
            trigger='minecraft:consume_item',
        ),
        'dried_kelp': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:dried_kelp')),
            trigger='minecraft:consume_item',
        ),
        'enchanted_golden_apple': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:enchanted_golden_apple')),
            trigger='minecraft:consume_item',
        ),
        'glow_berries': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:glow_berries')),
            trigger='minecraft:consume_item',
        ),
        'golden_apple': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:golden_apple')),
            trigger='minecraft:consume_item',
        ),
        'golden_carrot': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:golden_carrot')),
            trigger='minecraft:consume_item',
        ),
        'honey_bottle': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:honey_bottle')),
            trigger='minecraft:consume_item',
        ),
        'melon_slice': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:melon_slice')),
            trigger='minecraft:consume_item',
        ),
        'mushroom_stew': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:mushroom_stew')),
            trigger='minecraft:consume_item',
        ),
        'mutton': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:mutton')),
            trigger='minecraft:consume_item',
        ),
        'poisonous_potato': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:poisonous_potato')),
            trigger='minecraft:consume_item',
        ),
        'porkchop': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:porkchop')),
            trigger='minecraft:consume_item',
        ),
        'potato': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:potato')),
            trigger='minecraft:consume_item',
        ),
        'pufferfish': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:pufferfish')),
            trigger='minecraft:consume_item',
        ),
        'pumpkin_pie': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:pumpkin_pie')),
            trigger='minecraft:consume_item',
        ),
        'rabbit': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:rabbit')),
            trigger='minecraft:consume_item',
        ),
        'rabbit_stew': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:rabbit_stew')),
            trigger='minecraft:consume_item',
        ),
        'rotten_flesh': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:rotten_flesh')),
            trigger='minecraft:consume_item',
        ),
        'salmon': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:salmon')),
            trigger='minecraft:consume_item',
        ),
        'spider_eye': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:spider_eye')),
            trigger='minecraft:consume_item',
        ),
        'suspicious_stew': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:suspicious_stew')),
            trigger='minecraft:consume_item',
        ),
        'sweet_berries': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:sweet_berries')),
            trigger='minecraft:consume_item',
        ),
        'tropical_fish': AdvancementCriterionConsumeItem(
            conditions=ConsumeItemTriggerTypeArg(item=ItemPredicate(items='minecraft:tropical_fish')),
            trigger='minecraft:consume_item',
        ),
    },
    requirements=[
        ['apple'],
        ['mushroom_stew'],
        ['bread'],
        ['porkchop'],
        ['cooked_porkchop'],
        ['golden_apple'],
        ['enchanted_golden_apple'],
        ['cod'],
        ['salmon'],
        ['tropical_fish'],
        ['pufferfish'],
        ['cooked_cod'],
        ['cooked_salmon'],
        ['cookie'],
        ['melon_slice'],
        ['beef'],
        ['cooked_beef'],
        ['chicken'],
        ['cooked_chicken'],
        ['rotten_flesh'],
        ['spider_eye'],
        ['carrot'],
        ['potato'],
        ['baked_potato'],
        ['poisonous_potato'],
        ['golden_carrot'],
        ['pumpkin_pie'],
        ['rabbit'],
        ['cooked_rabbit'],
        ['rabbit_stew'],
        ['mutton'],
        ['cooked_mutton'],
        ['chorus_fruit'],
        ['beetroot'],
        ['beetroot_soup'],
        ['dried_kelp'],
        ['suspicious_stew'],
        ['sweet_berries'],
        ['honey_bottle'],
        ['glow_berries'],
    ],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)

BRED_ALL_ANIMALS = Advancement(
    parent='minecraft:husbandry/breed_an_animal',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:golden_carrot'),
        title=TextObjectStruct2(translate='advancements.husbandry.breed_all_animals.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.breed_all_animals.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'minecraft:armadillo': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:armadillo'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:axolotl': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:axolotl'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:bee': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:bee'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:camel': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:camel'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:cat': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:cat'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:chicken': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:chicken'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:cow': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:cow'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:donkey': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:donkey'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:fox': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:fox'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:frog': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                parent=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:frog'),
                    type='minecraft:entity_properties',
                ),
                partner=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:frog'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:goat': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:goat'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:hoglin': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:hoglin'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:horse': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:horse'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:llama': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:llama'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:mooshroom': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:mooshroom'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:mule': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:mule'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:nautilus': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:nautilus'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:ocelot': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:ocelot'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:panda': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:panda'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:pig': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:pig'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:rabbit': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:rabbit'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:sheep': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:sheep'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:sniffer': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                parent=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:sniffer'),
                    type='minecraft:entity_properties',
                ),
                partner=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:sniffer'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:strider': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:strider'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:turtle': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                parent=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:turtle'),
                    type='minecraft:entity_properties',
                ),
                partner=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:turtle'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
        'minecraft:wolf': AdvancementCriterionBredAnimals(
            conditions=BredAnimalsTriggerTypeArg(
                child=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:wolf'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:bred_animals',
        ),
    },
    requirements=[
        ['minecraft:horse'],
        ['minecraft:donkey'],
        ['minecraft:mule'],
        ['minecraft:sheep'],
        ['minecraft:cow'],
        ['minecraft:mooshroom'],
        ['minecraft:pig'],
        ['minecraft:chicken'],
        ['minecraft:wolf'],
        ['minecraft:ocelot'],
        ['minecraft:rabbit'],
        ['minecraft:llama'],
        ['minecraft:cat'],
        ['minecraft:panda'],
        ['minecraft:fox'],
        ['minecraft:bee'],
        ['minecraft:hoglin'],
        ['minecraft:strider'],
        ['minecraft:goat'],
        ['minecraft:axolotl'],
        ['minecraft:camel'],
        ['minecraft:armadillo'],
        ['minecraft:nautilus'],
        ['minecraft:turtle'],
        ['minecraft:frog'],
        ['minecraft:sniffer'],
    ],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)

BREED_AN_ANIMAL = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:wheat'),
        title=TextObjectStruct2(translate='advancements.husbandry.breed_an_animal.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.breed_an_animal.description'),
    ),
    criteria={'bred': AdvancementCriterionBredAnimals(trigger='minecraft:bred_animals')},
    requirements=[['bred']],
    sends_telemetry_event=True,
)

COMPLETE_CATALOGUE = Advancement(
    parent='minecraft:husbandry/tame_an_animal',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:cod'),
        title=TextObjectStruct2(translate='advancements.husbandry.complete_catalogue.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.complete_catalogue.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'minecraft:all_black': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:all_black')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:black': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:black')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:british_shorthair': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        components=DataComponentExactPredicate(cat_variant='minecraft:british_shorthair'),
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:calico': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:calico')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:jellie': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:jellie')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:persian': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:persian')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:ragdoll': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:ragdoll')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:red': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:red')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:siamese': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:siamese')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:tabby': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:tabby')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:white': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(cat_variant='minecraft:white')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
    },
    requirements=[
        ['minecraft:all_black'],
        ['minecraft:black'],
        ['minecraft:british_shorthair'],
        ['minecraft:calico'],
        ['minecraft:jellie'],
        ['minecraft:persian'],
        ['minecraft:ragdoll'],
        ['minecraft:red'],
        ['minecraft:siamese'],
        ['minecraft:tabby'],
        ['minecraft:white'],
    ],
    rewards=AdvancementRewards(experience=50),
    sends_telemetry_event=True,
)

FEED_SNIFFLET = Advancement(
    parent='minecraft:husbandry/obtain_sniffer_egg',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:torchflower_seeds'),
        title=TextObjectStruct2(translate='advancements.husbandry.feed_snifflet.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.feed_snifflet.description'),
        hidden=True,
    ),
    criteria={
        'feed_snifflet': AdvancementCriterionPlayerInteractedWithEntity(
            conditions=PlayerInteractTriggerTypeArg(
                item=ItemPredicate(items='#minecraft:sniffer_food'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:sniffer', flags=EntityFlagsPredicate(is_baby=True)),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_interacted_with_entity',
        ),
    },
    requirements=[['feed_snifflet']],
    sends_telemetry_event=True,
)

FISHY_BUSINESS = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:fishing_rod'),
        title=TextObjectStruct2(translate='advancements.husbandry.fishy_business.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.fishy_business.description'),
    ),
    criteria={
        'cod': AdvancementCriterionFishingRodHooked(
            conditions=FishingRodHookedTriggerTypeArg(item=ItemPredicate(items='minecraft:cod')),
            trigger='minecraft:fishing_rod_hooked',
        ),
        'pufferfish': AdvancementCriterionFishingRodHooked(
            conditions=FishingRodHookedTriggerTypeArg(item=ItemPredicate(items='minecraft:pufferfish')),
            trigger='minecraft:fishing_rod_hooked',
        ),
        'salmon': AdvancementCriterionFishingRodHooked(
            conditions=FishingRodHookedTriggerTypeArg(item=ItemPredicate(items='minecraft:salmon')),
            trigger='minecraft:fishing_rod_hooked',
        ),
        'tropical_fish': AdvancementCriterionFishingRodHooked(
            conditions=FishingRodHookedTriggerTypeArg(item=ItemPredicate(items='minecraft:tropical_fish')),
            trigger='minecraft:fishing_rod_hooked',
        ),
    },
    requirements=[['cod', 'tropical_fish', 'pufferfish', 'salmon']],
    sends_telemetry_event=True,
)

FROGLIGHTS = Advancement(
    parent='minecraft:husbandry/leash_all_frog_variants',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:verdant_froglight'),
        title=TextObjectStruct2(translate='advancements.husbandry.froglights.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.froglights.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'froglights': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(
                items=[
                    ItemPredicate(items='minecraft:ochre_froglight'),
                    ItemPredicate(items='minecraft:pearlescent_froglight'),
                    ItemPredicate(items='minecraft:verdant_froglight'),
                ],
            ),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['froglights']],
    sends_telemetry_event=True,
)

KILL_AXOLOTL_TARGET = Advancement(
    parent='minecraft:husbandry/axolotl_in_a_bucket',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:tropical_fish_bucket'),
        title=TextObjectStruct2(translate='advancements.husbandry.kill_axolotl_target.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.kill_axolotl_target.description'),
    ),
    criteria={
        'kill_axolotl_target': AdvancementCriterionEffectsChanged(
            conditions=EffectsChangedTriggerTypeArg(
                source=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:axolotl'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:effects_changed',
        ),
    },
    requirements=[['kill_axolotl_target']],
    sends_telemetry_event=True,
)

LEASH_ALL_FROG_VARIANTS = Advancement(
    parent='minecraft:husbandry/tadpole_in_a_bucket',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:lead'),
        title=TextObjectStruct2(translate='advancements.husbandry.leash_all_frog_variants.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.leash_all_frog_variants.description'),
    ),
    criteria={
        'minecraft:cold': AdvancementCriterionPlayerInteractedWithEntity(
            conditions=PlayerInteractTriggerTypeArg(
                item=ItemPredicate(items='minecraft:lead'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        components=DataComponentExactPredicate(frog_variant='minecraft:cold'),
                        entity_type='minecraft:frog',
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_interacted_with_entity',
        ),
        'minecraft:temperate': AdvancementCriterionPlayerInteractedWithEntity(
            conditions=PlayerInteractTriggerTypeArg(
                item=ItemPredicate(items='minecraft:lead'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        components=DataComponentExactPredicate(frog_variant='minecraft:temperate'),
                        entity_type='minecraft:frog',
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_interacted_with_entity',
        ),
        'minecraft:warm': AdvancementCriterionPlayerInteractedWithEntity(
            conditions=PlayerInteractTriggerTypeArg(
                item=ItemPredicate(items='minecraft:lead'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        components=DataComponentExactPredicate(frog_variant='minecraft:warm'),
                        entity_type='minecraft:frog',
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_interacted_with_entity',
        ),
    },
    requirements=[['minecraft:cold'], ['minecraft:temperate'], ['minecraft:warm']],
    sends_telemetry_event=True,
)

MAKE_A_SIGN_GLOW = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:glow_ink_sac'),
        title=TextObjectStruct2(translate='advancements.husbandry.make_a_sign_glow.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.make_a_sign_glow.description'),
    ),
    criteria={
        'make_a_sign_glow': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(block=BlockPredicate(blocks='#minecraft:all_signs')),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(items='minecraft:glow_ink_sac'),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['make_a_sign_glow']],
    sends_telemetry_event=True,
)

OBTAIN_NETHERITE_HOE = Advancement(
    parent='minecraft:husbandry/plant_seed',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:netherite_hoe'),
        title=TextObjectStruct2(translate='advancements.husbandry.netherite_hoe.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.netherite_hoe.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'netherite_hoe': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:netherite_hoe')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['netherite_hoe']],
    rewards=AdvancementRewards(experience=100),
    sends_telemetry_event=True,
)

OBTAIN_SNIFFER_EGG = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:sniffer_egg'),
        title=TextObjectStruct2(translate='advancements.husbandry.obtain_sniffer_egg.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.obtain_sniffer_egg.description'),
        hidden=True,
    ),
    criteria={
        'obtain_sniffer_egg': AdvancementCriterionInventoryChanged(
            conditions=InventoryChangeTriggerTypeArg(items=[ItemPredicate(items='minecraft:sniffer_egg')]),
            trigger='minecraft:inventory_changed',
        ),
    },
    requirements=[['obtain_sniffer_egg']],
    sends_telemetry_event=True,
)

PLACE_DRIED_GHAST_IN_WATER = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:dried_ghast'),
        title=TextObjectStruct2(translate='advancements.husbandry.place_dried_ghast_in_water.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.place_dried_ghast_in_water.description'),
    ),
    criteria={
        'place_dried_ghast_in_water': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(
                    blocks='minecraft:dried_ghast',
                    state={'waterlogged': 'true'},
                    type='minecraft:match_block',
                ),
            ),
            trigger='minecraft:placed_block',
        ),
    },
    requirements=[['place_dried_ghast_in_water']],
    sends_telemetry_event=True,
)

PLANT_ANY_SNIFFER_SEED = Advancement(
    parent='minecraft:husbandry/feed_snifflet',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:pitcher_pod'),
        title=TextObjectStruct2(translate='advancements.husbandry.plant_any_sniffer_seed.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.plant_any_sniffer_seed.description'),
        hidden=True,
    ),
    criteria={
        'pitcher_pod': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:pitcher_crop', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
        'torchflower': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:torchflower_crop', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
    },
    requirements=[['torchflower', 'pitcher_pod']],
    sends_telemetry_event=True,
)

PLANT_SEED = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:wheat'),
        title=TextObjectStruct2(translate='advancements.husbandry.plant_seed.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.plant_seed.description'),
    ),
    criteria={
        'beetroots': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:beetroots', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
        'melon_stem': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:melon_stem', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
        'nether_wart': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:nether_wart', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
        'pitcher_pod': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:pitcher_crop', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
        'pumpkin_stem': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:pumpkin_stem', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
        'torchflower': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:torchflower_crop', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
        'wheat': AdvancementCriterionPlacedBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionMatchBlock(blocks='minecraft:wheat', type='minecraft:match_block'),
            ),
            trigger='minecraft:placed_block',
        ),
    },
    requirements=[['wheat', 'pumpkin_stem', 'melon_stem', 'beetroots', 'nether_wart', 'torchflower', 'pitcher_pod']],
    sends_telemetry_event=True,
)

REMOVE_WOLF_ARMOR = Advancement(
    parent='minecraft:husbandry/tame_an_animal',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:shears'),
        title=TextObjectStruct2(translate='advancements.husbandry.remove_wolf_armor.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.remove_wolf_armor.description'),
    ),
    criteria={
        'remove_wolf_armor': AdvancementCriterionPlayerShearedEquipment(
            conditions=PlayerInteractTriggerTypeArg(
                item=ItemPredicate(items='minecraft:wolf_armor'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(entity_type='minecraft:wolf'),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_sheared_equipment',
        ),
    },
    requirements=[['remove_wolf_armor']],
    sends_telemetry_event=True,
)

REPAIR_WOLF_ARMOR = Advancement(
    parent='minecraft:husbandry/tame_an_animal',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:wolf_armor'),
        title=TextObjectStruct2(translate='advancements.husbandry.repair_wolf_armor.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.repair_wolf_armor.description'),
    ),
    criteria={
        'repair_wolf_armor': AdvancementCriterionPlayerInteractedWithEntity(
            conditions=PlayerInteractTriggerTypeArg(
                item=ItemPredicate(items='minecraft:armadillo_scute'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        entity_type='minecraft:wolf',
                        equipment={
                            EquipmentPredicateSlot.BODY: ItemPredicate(
                                items='minecraft:wolf_armor',
                                components=DataComponentExactPredicate(damage=0),
                            ),
                        },
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_interacted_with_entity',
        ),
    },
    requirements=[['repair_wolf_armor']],
    sends_telemetry_event=True,
)

RIDE_A_BOAT_WITH_A_GOAT = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:oak_boat'),
        title=TextObjectStruct2(translate='advancements.husbandry.ride_a_boat_with_a_goat.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.ride_a_boat_with_a_goat.description'),
    ),
    criteria={
        'ride_a_boat_with_a_goat': AdvancementCriterionStartedRiding(
            conditions=PlayerConditions(
                player=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        vehicle=EntitySubPredicateMap(
                            entity_type='#minecraft:boat',
                            passenger=EntitySubPredicateMap(entity_type='minecraft:goat'),
                        ),
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:started_riding',
        ),
    },
    requirements=[['ride_a_boat_with_a_goat']],
    sends_telemetry_event=True,
)

ROOT = Advancement(
    display=RootAdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:hay_block'),
        title=TextObjectStruct2(translate='advancements.husbandry.root.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.root.description'),
        show_toast=False,
        announce_to_chat=False,
        background='minecraft:gui/advancements/backgrounds/husbandry',
    ),
    criteria={'consumed_item': AdvancementCriterionConsumeItem(trigger='minecraft:consume_item')},
    requirements=[['consumed_item']],
    sends_telemetry_event=True,
)

SAFELY_HARVEST_HONEY = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:honey_bottle'),
        title=TextObjectStruct2(translate='advancements.husbandry.safely_harvest_honey.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.safely_harvest_honey.description'),
    ),
    criteria={
        'safely_harvest_honey': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(block=BlockPredicate(blocks='#minecraft:beehives'), smokey=True),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(items='minecraft:glass_bottle'),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['safely_harvest_honey']],
    sends_telemetry_event=True,
)

SILK_TOUCH_NEST = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:bee_nest'),
        title=TextObjectStruct2(translate='advancements.husbandry.silk_touch_nest.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.silk_touch_nest.description'),
    ),
    criteria={
        'silk_touch_nest': AdvancementCriterionBeeNestDestroyed(
            conditions=BeeNestDestroyedTriggerTypeArg(
                blocks='minecraft:bee_nest',
                num_bees_inside=3,
                item=ItemPredicate(
                    predicates={
                        'minecraft:enchantments': [EnchantmentPredicate(enchantments='minecraft:silk_touch', levels=MinMaxBounds(min=1))],
                    },
                ),
            ),
            trigger='minecraft:bee_nest_destroyed',
        ),
    },
    requirements=[['silk_touch_nest']],
    sends_telemetry_event=True,
)

TACTICAL_FISHING = Advancement(
    parent='minecraft:husbandry/fishy_business',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:pufferfish_bucket'),
        title=TextObjectStruct2(translate='advancements.husbandry.tactical_fishing.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.tactical_fishing.description'),
    ),
    criteria={
        'cod_bucket': AdvancementCriterionFilledBucket(
            conditions=FilledBucketTriggerTypeArg(item=ItemPredicate(items='minecraft:cod_bucket')),
            trigger='minecraft:filled_bucket',
        ),
        'pufferfish_bucket': AdvancementCriterionFilledBucket(
            conditions=FilledBucketTriggerTypeArg(item=ItemPredicate(items='minecraft:pufferfish_bucket')),
            trigger='minecraft:filled_bucket',
        ),
        'salmon_bucket': AdvancementCriterionFilledBucket(
            conditions=FilledBucketTriggerTypeArg(item=ItemPredicate(items='minecraft:salmon_bucket')),
            trigger='minecraft:filled_bucket',
        ),
        'tropical_fish_bucket': AdvancementCriterionFilledBucket(
            conditions=FilledBucketTriggerTypeArg(item=ItemPredicate(items='minecraft:tropical_fish_bucket')),
            trigger='minecraft:filled_bucket',
        ),
    },
    requirements=[['cod_bucket', 'tropical_fish_bucket', 'pufferfish_bucket', 'salmon_bucket']],
    sends_telemetry_event=True,
)

TADPOLE_IN_A_BUCKET = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:tadpole_bucket'),
        title=TextObjectStruct2(translate='advancements.husbandry.tadpole_in_a_bucket.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.tadpole_in_a_bucket.description'),
    ),
    criteria={
        'tadpole_bucket': AdvancementCriterionFilledBucket(
            conditions=FilledBucketTriggerTypeArg(item=ItemPredicate(items='minecraft:tadpole_bucket')),
            trigger='minecraft:filled_bucket',
        ),
    },
    requirements=[['tadpole_bucket']],
    sends_telemetry_event=True,
)

TAME_AN_ANIMAL = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:lead'),
        title=TextObjectStruct2(translate='advancements.husbandry.tame_an_animal.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.tame_an_animal.description'),
    ),
    criteria={'tamed_animal': AdvancementCriterionTameAnimal(trigger='minecraft:tame_animal')},
    requirements=[['tamed_animal']],
    sends_telemetry_event=True,
)

UH_OH = Advancement(
    parent='minecraft:husbandry/root',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:tnt'),
        title=TextObjectStruct2(translate='advancements.husbandry.uh_oh.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.uh_oh.description'),
    ),
    criteria={
        'give_tnt_directly': AdvancementCriterionPlayerInteractedWithEntity(
            conditions=PlayerInteractTriggerTypeArg(
                item=ItemPredicate(items='#minecraft:sulfur_cube_archetype/explosive'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        entity_type='minecraft:sulfur_cube',
                        flags=EntityFlagsPredicate(is_baby=False),
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:player_interacted_with_entity',
        ),
        'pick_up_dropped_tnt': AdvancementCriterionThrownItemPickedUpByEntity(
            conditions=PickedUpItemTriggerTypeArg(
                item=ItemPredicate(items='#minecraft:sulfur_cube_archetype/explosive'),
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(
                        entity_type='minecraft:sulfur_cube',
                        flags=EntityFlagsPredicate(is_baby=False),
                    ),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:thrown_item_picked_up_by_entity',
        ),
    },
    requirements=[['pick_up_dropped_tnt', 'give_tnt_directly']],
    sends_telemetry_event=True,
)

WAX_OFF = Advancement(
    parent='minecraft:husbandry/wax_on',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:stone_axe'),
        title=TextObjectStruct2(translate='advancements.husbandry.wax_off.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.wax_off.description'),
    ),
    criteria={
        'wax_off': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(
                                block=BlockPredicate(
                                    blocks=[
                                        'minecraft:waxed_copper_block',
                                        'minecraft:waxed_exposed_copper',
                                        'minecraft:waxed_weathered_copper',
                                        'minecraft:waxed_oxidized_copper',
                                        'minecraft:waxed_cut_copper',
                                        'minecraft:waxed_exposed_cut_copper',
                                        'minecraft:waxed_weathered_cut_copper',
                                        'minecraft:waxed_oxidized_cut_copper',
                                        'minecraft:waxed_cut_copper_slab',
                                        'minecraft:waxed_exposed_cut_copper_slab',
                                        'minecraft:waxed_weathered_cut_copper_slab',
                                        'minecraft:waxed_oxidized_cut_copper_slab',
                                        'minecraft:waxed_cut_copper_stairs',
                                        'minecraft:waxed_exposed_cut_copper_stairs',
                                        'minecraft:waxed_weathered_cut_copper_stairs',
                                        'minecraft:waxed_oxidized_cut_copper_stairs',
                                        'minecraft:waxed_chiseled_copper',
                                        'minecraft:waxed_exposed_chiseled_copper',
                                        'minecraft:waxed_weathered_chiseled_copper',
                                        'minecraft:waxed_oxidized_chiseled_copper',
                                        'minecraft:waxed_copper_door',
                                        'minecraft:waxed_exposed_copper_door',
                                        'minecraft:waxed_weathered_copper_door',
                                        'minecraft:waxed_oxidized_copper_door',
                                        'minecraft:waxed_copper_trapdoor',
                                        'minecraft:waxed_exposed_copper_trapdoor',
                                        'minecraft:waxed_weathered_copper_trapdoor',
                                        'minecraft:waxed_oxidized_copper_trapdoor',
                                        'minecraft:waxed_copper_bars',
                                        'minecraft:waxed_exposed_copper_bars',
                                        'minecraft:waxed_weathered_copper_bars',
                                        'minecraft:waxed_oxidized_copper_bars',
                                        'minecraft:waxed_copper_grate',
                                        'minecraft:waxed_exposed_copper_grate',
                                        'minecraft:waxed_weathered_copper_grate',
                                        'minecraft:waxed_oxidized_copper_grate',
                                        'minecraft:waxed_copper_bulb',
                                        'minecraft:waxed_exposed_copper_bulb',
                                        'minecraft:waxed_weathered_copper_bulb',
                                        'minecraft:waxed_oxidized_copper_bulb',
                                        'minecraft:waxed_copper_chest',
                                        'minecraft:waxed_exposed_copper_chest',
                                        'minecraft:waxed_weathered_copper_chest',
                                        'minecraft:waxed_oxidized_copper_chest',
                                        'minecraft:waxed_copper_golem_statue',
                                        'minecraft:waxed_exposed_copper_golem_statue',
                                        'minecraft:waxed_weathered_copper_golem_statue',
                                        'minecraft:waxed_oxidized_copper_golem_statue',
                                        'minecraft:waxed_lightning_rod',
                                        'minecraft:waxed_exposed_lightning_rod',
                                        'minecraft:waxed_weathered_lightning_rod',
                                        'minecraft:waxed_oxidized_lightning_rod',
                                        'minecraft:waxed_copper_lantern',
                                        'minecraft:waxed_exposed_copper_lantern',
                                        'minecraft:waxed_weathered_copper_lantern',
                                        'minecraft:waxed_oxidized_copper_lantern',
                                        'minecraft:waxed_copper_chain',
                                        'minecraft:waxed_exposed_copper_chain',
                                        'minecraft:waxed_weathered_copper_chain',
                                        'minecraft:waxed_oxidized_copper_chain',
                                    ],
                                ),
                            ),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(
                                items=[
                                    'minecraft:wooden_axe',
                                    'minecraft:golden_axe',
                                    'minecraft:stone_axe',
                                    'minecraft:copper_axe',
                                    'minecraft:iron_axe',
                                    'minecraft:diamond_axe',
                                    'minecraft:netherite_axe',
                                ],
                            ),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['wax_off']],
    sends_telemetry_event=True,
)

WAX_ON = Advancement(
    parent='minecraft:husbandry/safely_harvest_honey',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:honeycomb'),
        title=TextObjectStruct2(translate='advancements.husbandry.wax_on.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.wax_on.description'),
    ),
    criteria={
        'wax_on': AdvancementCriterionItemUsedOnBlock(
            conditions=ItemUesdOnLocationConditions(
                location=LootConditionAllOf(
                    terms=[
                        LootConditionLocationCheck(
                            predicate=LocationPredicate(
                                block=BlockPredicate(
                                    blocks=[
                                        'minecraft:copper_block',
                                        'minecraft:exposed_copper',
                                        'minecraft:weathered_copper',
                                        'minecraft:oxidized_copper',
                                        'minecraft:cut_copper',
                                        'minecraft:exposed_cut_copper',
                                        'minecraft:weathered_cut_copper',
                                        'minecraft:oxidized_cut_copper',
                                        'minecraft:cut_copper_slab',
                                        'minecraft:exposed_cut_copper_slab',
                                        'minecraft:weathered_cut_copper_slab',
                                        'minecraft:oxidized_cut_copper_slab',
                                        'minecraft:cut_copper_stairs',
                                        'minecraft:exposed_cut_copper_stairs',
                                        'minecraft:weathered_cut_copper_stairs',
                                        'minecraft:oxidized_cut_copper_stairs',
                                        'minecraft:chiseled_copper',
                                        'minecraft:exposed_chiseled_copper',
                                        'minecraft:weathered_chiseled_copper',
                                        'minecraft:oxidized_chiseled_copper',
                                        'minecraft:copper_door',
                                        'minecraft:exposed_copper_door',
                                        'minecraft:weathered_copper_door',
                                        'minecraft:oxidized_copper_door',
                                        'minecraft:copper_trapdoor',
                                        'minecraft:exposed_copper_trapdoor',
                                        'minecraft:weathered_copper_trapdoor',
                                        'minecraft:oxidized_copper_trapdoor',
                                        'minecraft:copper_bars',
                                        'minecraft:exposed_copper_bars',
                                        'minecraft:weathered_copper_bars',
                                        'minecraft:oxidized_copper_bars',
                                        'minecraft:copper_grate',
                                        'minecraft:exposed_copper_grate',
                                        'minecraft:weathered_copper_grate',
                                        'minecraft:oxidized_copper_grate',
                                        'minecraft:copper_bulb',
                                        'minecraft:exposed_copper_bulb',
                                        'minecraft:weathered_copper_bulb',
                                        'minecraft:oxidized_copper_bulb',
                                        'minecraft:copper_chest',
                                        'minecraft:exposed_copper_chest',
                                        'minecraft:weathered_copper_chest',
                                        'minecraft:oxidized_copper_chest',
                                        'minecraft:copper_golem_statue',
                                        'minecraft:exposed_copper_golem_statue',
                                        'minecraft:weathered_copper_golem_statue',
                                        'minecraft:oxidized_copper_golem_statue',
                                        'minecraft:lightning_rod',
                                        'minecraft:exposed_lightning_rod',
                                        'minecraft:weathered_lightning_rod',
                                        'minecraft:oxidized_lightning_rod',
                                        'minecraft:copper_lantern',
                                        'minecraft:exposed_copper_lantern',
                                        'minecraft:weathered_copper_lantern',
                                        'minecraft:oxidized_copper_lantern',
                                        'minecraft:copper_chain',
                                        'minecraft:exposed_copper_chain',
                                        'minecraft:weathered_copper_chain',
                                        'minecraft:oxidized_copper_chain',
                                    ],
                                ),
                            ),
                            type='minecraft:location_check',
                        ),
                        LootConditionMatchTool(
                            predicate=ItemPredicate(items='minecraft:honeycomb'),
                            type='minecraft:match_tool',
                        ),
                    ],
                    type='minecraft:all_of',
                ),
            ),
            trigger='minecraft:item_used_on_block',
        ),
    },
    requirements=[['wax_on']],
    sends_telemetry_event=True,
)

WHOLE_PACK = Advancement(
    parent='minecraft:husbandry/tame_an_animal',
    display=AdvancementDisplay(
        icon=ItemStackOfComponent(id='minecraft:bone'),
        title=TextObjectStruct2(translate='advancements.husbandry.whole_pack.title'),
        description=TextObjectStruct2(translate='advancements.husbandry.whole_pack.description'),
        frame=AdvancementFrame.CHALLENGE,
    ),
    criteria={
        'minecraft:ashen': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:ashen')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:black': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:black')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:chestnut': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:chestnut')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:pale': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:pale')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:rusty': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:rusty')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:snowy': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:snowy')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:spotted': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:spotted')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:striped': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:striped')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
        'minecraft:woods': AdvancementCriterionTameAnimal(
            conditions=TameAnimalTriggerTypeArg(
                entity=LootConditionEntityProperties(
                    entity=EntityTarget.THIS,
                    predicate=EntitySubPredicateMap(components=DataComponentExactPredicate(wolf_variant='minecraft:woods')),
                    type='minecraft:entity_properties',
                ),
            ),
            trigger='minecraft:tame_animal',
        ),
    },
    requirements=[
        ['minecraft:ashen'],
        ['minecraft:black'],
        ['minecraft:chestnut'],
        ['minecraft:pale'],
        ['minecraft:rusty'],
        ['minecraft:snowy'],
        ['minecraft:spotted'],
        ['minecraft:striped'],
        ['minecraft:woods'],
    ],
    rewards=AdvancementRewards(experience=50),
    sends_telemetry_event=True,
)
