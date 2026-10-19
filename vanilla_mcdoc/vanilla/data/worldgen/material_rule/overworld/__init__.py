"""Vanilla's data/worldgen/material_rule/overworld/ files"""
from vanilla_mcdoc.data.worldgen.VerticalAnchor import VerticalAnchorStruct1
from vanilla_mcdoc.data.worldgen.material_condition.MaterialCondition import MaterialConditionBiome, MaterialConditionHole, MaterialConditionNoiseThreshold, MaterialConditionNot, MaterialConditionVerticalGradient, MaterialConditionYAbove
from vanilla_mcdoc.data.worldgen.material_rule.MaterialRule import MaterialRuleBandlands, MaterialRuleBlock, MaterialRuleCondition, MaterialRuleOreVein, MaterialRuleSequence

BIOME_SURFACE = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:frozen_peaks', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/frozen_peaks',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:snowy_slopes', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/snowy_slopes',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:jagged_peaks', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/jagged_peaks',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:grove', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/grove',
            type='minecraft:condition',
        ),
        MaterialRuleSequence(
            sequence=[
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:stony_peaks', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/stony_peaks',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:stony_shore', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/stony_shore',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:windswept_hills', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/windswept_hills',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(
                        biome_is=['minecraft:warm_ocean', 'minecraft:beach', 'minecraft:snowy_beach'],
                        type='minecraft:biome',
                    ),
                    then_run='minecraft:overworld/sand_or_sandstone_if_ceiling',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:desert', type='minecraft:biome'),
                    then_run='minecraft:overworld/sand_or_sandstone_if_ceiling',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:dripstone_caves', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/dripstone_caves',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:sulfur_caves', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/sulfur_caves',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:ice_caves', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/ice_caves',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:mangrove_swamp', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/mangrove_swamp',
                    type='minecraft:condition',
                ),
            ],
            type='minecraft:sequence',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:windswept_savanna', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/windswept_savanna',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:windswept_gravelly_hills', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/windswept_gravelly_hills',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(
                biome_is=['minecraft:old_growth_pine_taiga', 'minecraft:old_growth_spruce_taiga'],
                type='minecraft:biome',
            ),
            then_run='minecraft:overworld/biome_surface/old_growth_pine_taiga',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:ice_spikes', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/ice_spikes',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:mushroom_fields', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/mushroom_fields',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:dappled_forest', type='minecraft:biome'),
            then_run='minecraft:overworld/biome_surface/dappled_forest',
            type='minecraft:condition',
        ),
        'minecraft:overworld/biome_surface/default',
    ],
    type='minecraft:sequence',
)

COPPER_ORE_VEIN = MaterialRuleOreVein(
    ore_block='minecraft:copper_ore',
    raw_ore_block='minecraft:raw_copper_block',
    filler_block='minecraft:granite',
    raw_ore_chance=0.02,
    density='minecraft:overworld/ore_vein/copper_density',
    richness='minecraft:overworld/ore_vein/richness',
    filler_gap='minecraft:overworld/ore_vein/gap',
    type='minecraft:ore_vein',
)

GRAVEL_OR_STONE_IF_CEILING = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true='minecraft:on_ceiling',
            then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleBlock(result_state='minecraft:gravel', type='minecraft:block'),
    ],
    type='minecraft:sequence',
)

ICE_CAVE_BANDS = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:ice_cave_gradient',
                min_threshold=-0.6000000238418579,
                max_threshold=-0.5,
                is_3d=True,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:calcite', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:ice_cave_gradient',
                min_threshold=-0.5,
                max_threshold=0.20000000298023224,
                is_3d=True,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:packed_ice', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:ice_cave_gradient',
                min_threshold=0.20000000298023224,
                max_threshold=0.30000001192092896,
                is_3d=True,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:calcite', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:ice_cave_gradient',
                min_threshold=0.30000001192092896,
                max_threshold=0.5,
                is_3d=True,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:packed_ice', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:ice_cave_gradient',
                min_threshold=0.5,
                max_threshold=0.699999988079071,
                is_3d=True,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:calcite', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

IRON_ORE_VEIN = MaterialRuleOreVein(
    ore_block='minecraft:deepslate_iron_ore',
    raw_ore_block='minecraft:raw_iron_block',
    filler_block='minecraft:tuff',
    raw_ore_chance=0.02,
    density='minecraft:overworld/ore_vein/iron_density',
    richness='minecraft:overworld/ore_vein/richness',
    filler_gap='minecraft:overworld/ore_vein/gap',
    type='minecraft:ore_vein',
)

POWDER_SNOW_SURFACE = MaterialRuleCondition(
    if_true=MaterialConditionNoiseThreshold(
        noise='minecraft:powder_snow',
        min_threshold=0.35,
        max_threshold=0.6,
        type='minecraft:noise_threshold',
    ),
    then_run=MaterialRuleCondition(
        if_true='minecraft:not_underwater',
        then_run=MaterialRuleBlock(result_state='minecraft:powder_snow', type='minecraft:block'),
        type='minecraft:condition',
    ),
    type='minecraft:condition',
)

POWDER_SNOW_UNDER_SURFACE = MaterialRuleCondition(
    if_true=MaterialConditionNoiseThreshold(
        noise='minecraft:powder_snow',
        min_threshold=0.45,
        max_threshold=0.58,
        type='minecraft:noise_threshold',
    ),
    then_run=MaterialRuleCondition(
        if_true='minecraft:not_underwater',
        then_run=MaterialRuleBlock(result_state='minecraft:powder_snow', type='minecraft:block'),
        type='minecraft:condition',
    ),
    type='minecraft:condition',
)

SAND_OR_SANDSTONE_IF_CEILING = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true='minecraft:on_ceiling',
            then_run=MaterialRuleBlock(result_state='minecraft:sandstone', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleBlock(result_state='minecraft:sand', type='minecraft:block'),
    ],
    type='minecraft:sequence',
)

SULFUR_CAVE_BANDS = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:sulfur_cave_gradient',
                min_threshold=-0.4000000059604645,
                max_threshold=-0.10000000149011612,
                is_3d=True,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:cinnabar', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:sulfur_cave_gradient',
                min_threshold=0.0,
                max_threshold=0.4000000059604645,
                is_3d=True,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:sulfur', type='minecraft:block'),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionNoiseThreshold(
                noise='minecraft:sulfur_cave_gradient',
                min_threshold=0.4000000059604645,
                max_threshold=1.7976931348623157e+308,
                is_3d=True,
                type='minecraft:noise_threshold',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:cinnabar', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

SURFACE = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true='minecraft:on_floor',
            then_run=MaterialRuleSequence(
                sequence=[
                    MaterialRuleCondition(
                        if_true=MaterialConditionBiome(biome_is='minecraft:wooded_badlands', type='minecraft:biome'),
                        then_run=MaterialRuleCondition(
                            if_true=MaterialConditionYAbove(
                                anchor=VerticalAnchorStruct1(absolute=97),
                                surface_depth_multiplier=2,
                                add_stone_depth=False,
                                type='minecraft:y_above',
                            ),
                            then_run=MaterialRuleSequence(
                                sequence=[
                                    MaterialRuleCondition(
                                        if_true=MaterialConditionNoiseThreshold(
                                            noise='minecraft:surface',
                                            min_threshold=-0.909,
                                            max_threshold=-0.5454,
                                            type='minecraft:noise_threshold',
                                        ),
                                        then_run=MaterialRuleBlock(result_state='minecraft:coarse_dirt', type='minecraft:block'),
                                        type='minecraft:condition',
                                    ),
                                    MaterialRuleCondition(
                                        if_true=MaterialConditionNoiseThreshold(
                                            noise='minecraft:surface',
                                            min_threshold=-0.1818,
                                            max_threshold=0.1818,
                                            type='minecraft:noise_threshold',
                                        ),
                                        then_run=MaterialRuleBlock(result_state='minecraft:coarse_dirt', type='minecraft:block'),
                                        type='minecraft:condition',
                                    ),
                                    MaterialRuleCondition(
                                        if_true=MaterialConditionNoiseThreshold(
                                            noise='minecraft:surface',
                                            min_threshold=0.5454,
                                            max_threshold=0.909,
                                            type='minecraft:noise_threshold',
                                        ),
                                        then_run=MaterialRuleBlock(result_state='minecraft:coarse_dirt', type='minecraft:block'),
                                        type='minecraft:condition',
                                    ),
                                    'minecraft:overworld/biome_surface/default',
                                ],
                                type='minecraft:sequence',
                            ),
                            type='minecraft:condition',
                        ),
                        type='minecraft:condition',
                    ),
                    MaterialRuleCondition(
                        if_true=MaterialConditionBiome(biome_is='minecraft:swamp', type='minecraft:biome'),
                        then_run=MaterialRuleCondition(
                            if_true=MaterialConditionYAbove(
                                anchor=VerticalAnchorStruct1(absolute=62),
                                surface_depth_multiplier=0,
                                add_stone_depth=False,
                                type='minecraft:y_above',
                            ),
                            then_run=MaterialRuleCondition(
                                if_true=MaterialConditionNot(
                                    invert=MaterialConditionYAbove(
                                        anchor=VerticalAnchorStruct1(absolute=63),
                                        surface_depth_multiplier=0,
                                        add_stone_depth=False,
                                        type='minecraft:y_above',
                                    ),
                                    type='minecraft:not',
                                ),
                                then_run=MaterialRuleCondition(
                                    if_true=MaterialConditionNoiseThreshold(
                                        noise='minecraft:surface_swamp',
                                        min_threshold=0.0,
                                        max_threshold=1.7976931348623157e+308,
                                        type='minecraft:noise_threshold',
                                    ),
                                    then_run=MaterialRuleBlock(result_state='minecraft:water', type='minecraft:block'),
                                    type='minecraft:condition',
                                ),
                                type='minecraft:condition',
                            ),
                            type='minecraft:condition',
                        ),
                        type='minecraft:condition',
                    ),
                    MaterialRuleCondition(
                        if_true=MaterialConditionBiome(biome_is='minecraft:mangrove_swamp', type='minecraft:biome'),
                        then_run=MaterialRuleCondition(
                            if_true=MaterialConditionYAbove(
                                anchor=VerticalAnchorStruct1(absolute=60),
                                surface_depth_multiplier=0,
                                add_stone_depth=False,
                                type='minecraft:y_above',
                            ),
                            then_run=MaterialRuleCondition(
                                if_true=MaterialConditionNot(
                                    invert=MaterialConditionYAbove(
                                        anchor=VerticalAnchorStruct1(absolute=63),
                                        surface_depth_multiplier=0,
                                        add_stone_depth=False,
                                        type='minecraft:y_above',
                                    ),
                                    type='minecraft:not',
                                ),
                                then_run=MaterialRuleCondition(
                                    if_true=MaterialConditionNoiseThreshold(
                                        noise='minecraft:surface_swamp',
                                        min_threshold=0.0,
                                        max_threshold=1.7976931348623157e+308,
                                        type='minecraft:noise_threshold',
                                    ),
                                    then_run=MaterialRuleBlock(result_state='minecraft:water', type='minecraft:block'),
                                    type='minecraft:condition',
                                ),
                                type='minecraft:condition',
                            ),
                            type='minecraft:condition',
                        ),
                        type='minecraft:condition',
                    ),
                ],
                type='minecraft:sequence',
            ),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(
                biome_is=['minecraft:badlands', 'minecraft:eroded_badlands', 'minecraft:wooded_badlands'],
                type='minecraft:biome',
            ),
            then_run=MaterialRuleSequence(
                sequence=[
                    MaterialRuleCondition(
                        if_true='minecraft:on_floor',
                        then_run=MaterialRuleSequence(
                            sequence=[
                                MaterialRuleCondition(
                                    if_true=MaterialConditionYAbove(
                                        anchor=VerticalAnchorStruct1(absolute=256),
                                        surface_depth_multiplier=0,
                                        add_stone_depth=False,
                                        type='minecraft:y_above',
                                    ),
                                    then_run=MaterialRuleBlock(
                                        result_state='minecraft:orange_terracotta',
                                        type='minecraft:block',
                                    ),
                                    type='minecraft:condition',
                                ),
                                MaterialRuleCondition(
                                    if_true=MaterialConditionYAbove(
                                        anchor=VerticalAnchorStruct1(absolute=74),
                                        surface_depth_multiplier=1,
                                        add_stone_depth=True,
                                        type='minecraft:y_above',
                                    ),
                                    then_run=MaterialRuleSequence(
                                        sequence=[
                                            MaterialRuleCondition(
                                                if_true=MaterialConditionNoiseThreshold(
                                                    noise='minecraft:surface',
                                                    min_threshold=-0.909,
                                                    max_threshold=-0.5454,
                                                    type='minecraft:noise_threshold',
                                                ),
                                                then_run=MaterialRuleBlock(
                                                    result_state='minecraft:terracotta',
                                                    type='minecraft:block',
                                                ),
                                                type='minecraft:condition',
                                            ),
                                            MaterialRuleCondition(
                                                if_true=MaterialConditionNoiseThreshold(
                                                    noise='minecraft:surface',
                                                    min_threshold=-0.1818,
                                                    max_threshold=0.1818,
                                                    type='minecraft:noise_threshold',
                                                ),
                                                then_run=MaterialRuleBlock(
                                                    result_state='minecraft:terracotta',
                                                    type='minecraft:block',
                                                ),
                                                type='minecraft:condition',
                                            ),
                                            MaterialRuleCondition(
                                                if_true=MaterialConditionNoiseThreshold(
                                                    noise='minecraft:surface',
                                                    min_threshold=0.5454,
                                                    max_threshold=0.909,
                                                    type='minecraft:noise_threshold',
                                                ),
                                                then_run=MaterialRuleBlock(
                                                    result_state='minecraft:terracotta',
                                                    type='minecraft:block',
                                                ),
                                                type='minecraft:condition',
                                            ),
                                            MaterialRuleBandlands(type='minecraft:bandlands'),
                                        ],
                                        type='minecraft:sequence',
                                    ),
                                    type='minecraft:condition',
                                ),
                                MaterialRuleCondition(
                                    if_true='minecraft:not_underwater',
                                    then_run=MaterialRuleSequence(
                                        sequence=[
                                            MaterialRuleCondition(
                                                if_true='minecraft:on_ceiling',
                                                then_run=MaterialRuleBlock(
                                                    result_state='minecraft:red_sandstone',
                                                    type='minecraft:block',
                                                ),
                                                type='minecraft:condition',
                                            ),
                                            MaterialRuleBlock(result_state='minecraft:red_sand', type='minecraft:block'),
                                        ],
                                        type='minecraft:sequence',
                                    ),
                                    type='minecraft:condition',
                                ),
                                MaterialRuleCondition(
                                    if_true=MaterialConditionNot(
                                        invert=MaterialConditionHole(type='minecraft:hole'),
                                        type='minecraft:not',
                                    ),
                                    then_run=MaterialRuleBlock(
                                        result_state='minecraft:orange_terracotta',
                                        type='minecraft:block',
                                    ),
                                    type='minecraft:condition',
                                ),
                                MaterialRuleCondition(
                                    if_true='minecraft:not_under_deep_water',
                                    then_run=MaterialRuleBlock(result_state='minecraft:white_terracotta', type='minecraft:block'),
                                    type='minecraft:condition',
                                ),
                                'minecraft:overworld/gravel_or_stone_if_ceiling',
                            ],
                            type='minecraft:sequence',
                        ),
                        type='minecraft:condition',
                    ),
                    MaterialRuleCondition(
                        if_true=MaterialConditionYAbove(
                            anchor=VerticalAnchorStruct1(absolute=63),
                            surface_depth_multiplier=-1,
                            add_stone_depth=True,
                            type='minecraft:y_above',
                        ),
                        then_run=MaterialRuleSequence(
                            sequence=[
                                MaterialRuleCondition(
                                    if_true=MaterialConditionYAbove(
                                        anchor=VerticalAnchorStruct1(absolute=63),
                                        surface_depth_multiplier=0,
                                        add_stone_depth=False,
                                        type='minecraft:y_above',
                                    ),
                                    then_run=MaterialRuleCondition(
                                        if_true=MaterialConditionNot(
                                            invert=MaterialConditionYAbove(
                                                anchor=VerticalAnchorStruct1(absolute=74),
                                                surface_depth_multiplier=1,
                                                add_stone_depth=True,
                                                type='minecraft:y_above',
                                            ),
                                            type='minecraft:not',
                                        ),
                                        then_run=MaterialRuleBlock(
                                            result_state='minecraft:orange_terracotta',
                                            type='minecraft:block',
                                        ),
                                        type='minecraft:condition',
                                    ),
                                    type='minecraft:condition',
                                ),
                                MaterialRuleBandlands(type='minecraft:bandlands'),
                            ],
                            type='minecraft:sequence',
                        ),
                        type='minecraft:condition',
                    ),
                    MaterialRuleCondition(
                        if_true='minecraft:under_floor',
                        then_run=MaterialRuleCondition(
                            if_true='minecraft:not_under_deep_water',
                            then_run=MaterialRuleBlock(result_state='minecraft:white_terracotta', type='minecraft:block'),
                            type='minecraft:condition',
                        ),
                        type='minecraft:condition',
                    ),
                ],
                type='minecraft:sequence',
            ),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true='minecraft:on_floor',
            then_run=MaterialRuleCondition(
                if_true='minecraft:not_underwater',
                then_run=MaterialRuleSequence(
                    sequence=[
                        MaterialRuleCondition(
                            if_true=MaterialConditionBiome(
                                biome_is=['minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean'],
                                type='minecraft:biome',
                            ),
                            then_run=MaterialRuleCondition(
                                if_true=MaterialConditionHole(type='minecraft:hole'),
                                then_run=MaterialRuleBlock(result_state='minecraft:air', type='minecraft:block'),
                                type='minecraft:condition',
                            ),
                            type='minecraft:condition',
                        ),
                        'minecraft:overworld/biome_surface',
                    ],
                    type='minecraft:sequence',
                ),
                type='minecraft:condition',
            ),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true='minecraft:not_under_deep_water',
            then_run=MaterialRuleSequence(
                sequence=[
                    MaterialRuleCondition(
                        if_true='minecraft:on_floor',
                        then_run=MaterialRuleCondition(
                            if_true=MaterialConditionBiome(
                                biome_is=['minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean'],
                                type='minecraft:biome',
                            ),
                            then_run=MaterialRuleCondition(
                                if_true=MaterialConditionHole(type='minecraft:hole'),
                                then_run=MaterialRuleBlock(result_state='minecraft:water', type='minecraft:block'),
                                type='minecraft:condition',
                            ),
                            type='minecraft:condition',
                        ),
                        type='minecraft:condition',
                    ),
                    MaterialRuleCondition(
                        if_true='minecraft:under_floor',
                        then_run='minecraft:overworld/under_biome_surface',
                        type='minecraft:condition',
                    ),
                    MaterialRuleCondition(
                        if_true=MaterialConditionBiome(
                            biome_is=['minecraft:warm_ocean', 'minecraft:beach', 'minecraft:snowy_beach'],
                            type='minecraft:biome',
                        ),
                        then_run=MaterialRuleCondition(
                            if_true='minecraft:deep_under_floor',
                            then_run=MaterialRuleBlock(result_state='minecraft:sandstone', type='minecraft:block'),
                            type='minecraft:condition',
                        ),
                        type='minecraft:condition',
                    ),
                    MaterialRuleCondition(
                        if_true=MaterialConditionBiome(biome_is='minecraft:desert', type='minecraft:biome'),
                        then_run=MaterialRuleCondition(
                            if_true='minecraft:very_deep_under_floor',
                            then_run=MaterialRuleBlock(result_state='minecraft:sandstone', type='minecraft:block'),
                            type='minecraft:condition',
                        ),
                        type='minecraft:condition',
                    ),
                ],
                type='minecraft:sequence',
            ),
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true='minecraft:on_floor',
            then_run=MaterialRuleSequence(
                sequence=[
                    MaterialRuleCondition(
                        if_true=MaterialConditionBiome(
                            biome_is=['minecraft:frozen_peaks', 'minecraft:jagged_peaks'],
                            type='minecraft:biome',
                        ),
                        then_run=MaterialRuleBlock(result_state='minecraft:stone', type='minecraft:block'),
                        type='minecraft:condition',
                    ),
                    MaterialRuleCondition(
                        if_true=MaterialConditionBiome(
                            biome_is=['minecraft:warm_ocean', 'minecraft:lukewarm_ocean', 'minecraft:deep_lukewarm_ocean'],
                            type='minecraft:biome',
                        ),
                        then_run='minecraft:overworld/sand_or_sandstone_if_ceiling',
                        type='minecraft:condition',
                    ),
                    'minecraft:overworld/gravel_or_stone_if_ceiling',
                ],
                type='minecraft:sequence',
            ),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

UNDERGROUND = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:sulfur_caves', type='minecraft:biome'),
            then_run='minecraft:overworld/sulfur_cave_bands',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:ice_caves', type='minecraft:biome'),
            then_run='minecraft:overworld/ice_cave_bands',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionVerticalGradient(
                random_name='minecraft:deepslate',
                true_at_and_below=VerticalAnchorStruct1(absolute=0),
                false_at_and_above=VerticalAnchorStruct1(absolute=8),
                type='minecraft:vertical_gradient',
            ),
            then_run=MaterialRuleBlock(result_state='minecraft:deepslate', type='minecraft:block'),
            type='minecraft:condition',
        ),
    ],
    type='minecraft:sequence',
)

UNDER_BIOME_SURFACE = MaterialRuleSequence(
    sequence=[
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:frozen_peaks', type='minecraft:biome'),
            then_run='minecraft:overworld/under_biome_surface/frozen_peaks',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:snowy_slopes', type='minecraft:biome'),
            then_run='minecraft:overworld/under_biome_surface/snowy_slopes',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:jagged_peaks', type='minecraft:biome'),
            then_run='minecraft:overworld/under_biome_surface/jagged_peaks',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:grove', type='minecraft:biome'),
            then_run='minecraft:overworld/under_biome_surface/grove',
            type='minecraft:condition',
        ),
        MaterialRuleSequence(
            sequence=[
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:stony_peaks', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/stony_peaks',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:stony_shore', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/stony_shore',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:windswept_hills', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/windswept_hills',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(
                        biome_is=['minecraft:warm_ocean', 'minecraft:beach', 'minecraft:snowy_beach'],
                        type='minecraft:biome',
                    ),
                    then_run='minecraft:overworld/sand_or_sandstone_if_ceiling',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:desert', type='minecraft:biome'),
                    then_run='minecraft:overworld/sand_or_sandstone_if_ceiling',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:dripstone_caves', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/dripstone_caves',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:sulfur_caves', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/sulfur_caves',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:ice_caves', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/ice_caves',
                    type='minecraft:condition',
                ),
                MaterialRuleCondition(
                    if_true=MaterialConditionBiome(biome_is='minecraft:mangrove_swamp', type='minecraft:biome'),
                    then_run='minecraft:overworld/biome_surface/mangrove_swamp',
                    type='minecraft:condition',
                ),
            ],
            type='minecraft:sequence',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:windswept_savanna', type='minecraft:biome'),
            then_run='minecraft:overworld/under_biome_surface/windswept_savanna',
            type='minecraft:condition',
        ),
        MaterialRuleCondition(
            if_true=MaterialConditionBiome(biome_is='minecraft:windswept_gravelly_hills', type='minecraft:biome'),
            then_run='minecraft:overworld/under_biome_surface/windswept_gravelly_hills',
            type='minecraft:condition',
        ),
        'minecraft:overworld/under_biome_surface/default',
    ],
    type='minecraft:sequence',
)
