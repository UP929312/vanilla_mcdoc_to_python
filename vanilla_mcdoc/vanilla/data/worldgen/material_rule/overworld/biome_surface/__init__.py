"""Vanilla's data/worldgen/material_rule/overworld/biome_surface/ files"""
from vanilla_mcdoc.data.worldgen.material_condition.MaterialCondition import MaterialConditionNoiseThreshold, MaterialConditionSteep
from vanilla_mcdoc.data.worldgen.material_rule.MaterialRule import MaterialRuleBlock, MaterialRuleCondition, MaterialRuleSequence

DAPPLED_FOREST = MaterialRuleCondition(
    if_true=MaterialConditionNoiseThreshold(
        noise='minecraft:small_patch',
        min_threshold=1.2000000476837158,
        max_threshold=1.7976931348623157e+308,
        type='minecraft:noise_threshold',
    ),
    then_run=MaterialRuleBlock(result_state='minecraft:coarse_dirt', type='minecraft:block'),
    type='minecraft:condition',
)

DEFAULT = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true='minecraft:not_underwater',
            then_run=MaterialRuleBlock(result_state='minecraft:grass_block', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleBlock(result_state='minecraft:dirt', type='minecraft:block'),
    ],
    type='minecraft:sequence',
)

DRIPSTONE_CAVES = MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block')

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
                min_threshold=0.0,
                max_threshold=0.2,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:packed_ice', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:ice',
                min_threshold=0.0,
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
        'minecraft:overworld/powder_snow_surface',
        MaterialRuleCondition(
            if_true='minecraft:not_underwater',
            then_run=MaterialRuleBlock(result_state='minecraft:snow_block', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

ICE_CAVES = MaterialRuleSequence(
    sequence=['minecraft:overworld/ice_cave_bands', MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block')],
    type='minecraft:sequence',
)

ICE_SPIKES = MaterialRuleCondition(
    if_true='minecraft:not_underwater',
    then_run=MaterialRuleBlock(result_state='minecraft:snow_block', type='minecraft:block'),
    type='minecraft:condition',
)

JAGGED_PEAKS = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionSteep(type='minecraft:steep'),
            then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
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

MANGROVE_SWAMP = MaterialRuleBlock(result_state='minecraft:mud', type='minecraft:block')

MUSHROOM_FIELDS = MaterialRuleBlock(result_state='minecraft:mycelium', type='minecraft:block')

OLD_GROWTH_PINE_TAIGA = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:surface',
                min_threshold=0.21212121212121213,
                max_threshold=1.7976931348623157e+308,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:coarse_dirt', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:surface',
                min_threshold=-0.11515151515151514,
                max_threshold=1.7976931348623157e+308,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:podzol', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

SNOWY_SLOPES = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionSteep(type='minecraft:steep'),
            then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
            type='minecraft:condition',
        ),
        'minecraft:overworld/powder_snow_surface',
        MaterialRuleCondition(
            if_true='minecraft:not_underwater',
            then_run=MaterialRuleBlock(result_state='minecraft:snow_block', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

STONY_PEAKS = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:calcite',
                min_threshold=-0.0125,
                max_threshold=0.0125,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:calcite', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
    ],
    type='minecraft:sequence',
)

STONY_SHORE = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:gravel',
                min_threshold=-0.05,
                max_threshold=0.05,
                type='minecraft:noise_threshold',
            ),
            then_run='minecraft:overworld/gravel_or_stone_if_ceiling',
            type='minecraft:condition',
        ),
        MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
    ],
    type='minecraft:sequence',
)

SULFUR_CAVES = MaterialRuleSequence(
    sequence=['minecraft:overworld/sulfur_cave_bands', MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block')],
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
            then_run='minecraft:overworld/biome_surface/default',
            type='minecraft:condition',
        ),
        'minecraft:overworld/gravel_or_stone_if_ceiling',
    ],
    type='minecraft:sequence',
)

WINDSWEPT_HILLS = MaterialRuleCondition(
    if_true=MaterialConditionNoiseThreshold(
        noise='minecraft:surface',
        min_threshold=0.12121212121212122,
        max_threshold=1.7976931348623157e+308,
        type='minecraft:noise_threshold',
    ),
    then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
    type='minecraft:condition',
)

WINDSWEPT_SAVANNA = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:surface',
                min_threshold=0.21212121212121213,
                max_threshold=1.7976931348623157e+308,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:surface',
                min_threshold=-0.06060606060606061,
                max_threshold=1.7976931348623157e+308,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:coarse_dirt', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)
