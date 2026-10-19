"""Vanilla's data/worldgen/material_rule/overworld/under_biome_surface/ files"""
from vanilla_mcdoc.data.worldgen.material_condition.MaterialCondition import MaterialConditionNoiseThreshold, MaterialConditionSteep
from vanilla_mcdoc.data.worldgen.material_rule.MaterialRule import MaterialRuleBlock, MaterialRuleCondition, MaterialRuleSequence

DEFAULT = MaterialRuleBlock(result_state='minecraft:dirt', type='minecraft:block')

FROZEN_PEAKS = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionSteep(type='minecraft:steep'),
            then_run=MaterialRuleBlock(result_state='minecraft:packed_ice', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:packed_ice',
                min_threshold=-0.5,
                max_threshold=0.2,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:packed_ice', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:ice',
                min_threshold=-0.0625,
                max_threshold=0.025,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:ice', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true='minecraft:not_underwater',
            then_run=MaterialRuleBlock(result_state='minecraft:snow_block', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

GROVE = MaterialRuleSequence(
    sequence=[
        'minecraft:overworld/powder_snow_under_surface',
        MaterialRuleBlock(result_state='minecraft:dirt', type='minecraft:block'),
    ],
    type='minecraft:sequence',
)

JAGGED_PEAKS = MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block')

SNOWY_SLOPES = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionSteep(type='minecraft:steep'),
            then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
            type='minecraft:condition',
        ),
        'minecraft:overworld/powder_snow_under_surface',
        MaterialRuleCondition(
            if_true='minecraft:not_underwater',
            then_run=MaterialRuleBlock(result_state='minecraft:snow_block', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

WINDSWEPT_GRAVELLY_HILLS = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:surface',
                min_threshold=0.24242424242424243,
                max_threshold=1.7976931348623157e+308,
                type='minecraft:noise_threshold',
            ),
            then_run='minecraft:overworld/gravel_or_stone_if_ceiling',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:surface',
                min_threshold=0.12121212121212122,
                max_threshold=1.7976931348623157e+308,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:surface',
                min_threshold=-0.12121212121212122,
                max_threshold=1.7976931348623157e+308,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:dirt', type='minecraft:block'),
            type='minecraft:condition',
        ),
        'minecraft:overworld/gravel_or_stone_if_ceiling',
    ],
    type='minecraft:sequence',
)

WINDSWEPT_SAVANNA = MaterialRuleCondition(
    if_true=MaterialConditionNoiseThreshold(
        noise='minecraft:surface',
        min_threshold=0.21212121212121213,
        max_threshold=1.7976931348623157e+308,
        type='minecraft:noise_threshold',
    ),
    then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
    type='minecraft:condition',
)
