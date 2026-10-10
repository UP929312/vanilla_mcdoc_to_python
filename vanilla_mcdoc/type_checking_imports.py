"""For each generated module, the names its annotations use that it only imports under `if TYPE_CHECKING:`, and where
from (the module, and what it's called there). base.py imports them for real when a model is first used."""

TYPE_CHECKING_IMPORTS: dict[str, dict[str, tuple[str, str]]] = {
    'vanilla_mcdoc.assets.atlas.Atlas': {
        'SpriteSource': ('vanilla_mcdoc.assets.atlas.SpriteSource', 'SpriteSource'),
    },
    'vanilla_mcdoc.assets.atlas.Filter': {
        'FilterPattern': ('vanilla_mcdoc.assets.atlas.FilterPattern', 'FilterPattern'),
    },
    'vanilla_mcdoc.assets.atlas.PalettedPermutations': {
        'PaletteTexture': ('vanilla_mcdoc.assets.atlas.PaletteTexture', 'PaletteTexture'),
    },
    'vanilla_mcdoc.assets.atlas.PermutationsMap': {
        'PaletteTexture': ('vanilla_mcdoc.assets.atlas.PaletteTexture', 'PaletteTexture'),
    },
    'vanilla_mcdoc.assets.atlas.Unstitch': {
        'UnstitchRegion': ('vanilla_mcdoc.assets.atlas.UnstitchRegion', 'UnstitchRegion'),
    },
    'vanilla_mcdoc.assets.block_state_definition.BlockStateDefinition': {
        'ModelVariant': ('vanilla_mcdoc.assets.block_state_definition.ModelVariant', 'ModelVariant'),
        'MultiPartCondition': ('vanilla_mcdoc.assets.block_state_definition.MultiPartCondition', 'MultiPartCondition'),
    },
    'vanilla_mcdoc.assets.block_state_definition.BlockStateDefinitionMultipart': {
        'ModelVariant': ('vanilla_mcdoc.assets.block_state_definition.ModelVariant', 'ModelVariant'),
        'MultiPartCondition': ('vanilla_mcdoc.assets.block_state_definition.MultiPartCondition', 'MultiPartCondition'),
    },
    'vanilla_mcdoc.assets.block_state_definition.BlockStateDefinitionMultipartEntry': {
        'ModelVariant': ('vanilla_mcdoc.assets.block_state_definition.ModelVariant', 'ModelVariant'),
        'MultiPartCondition': ('vanilla_mcdoc.assets.block_state_definition.MultiPartCondition', 'MultiPartCondition'),
    },
    'vanilla_mcdoc.assets.block_state_definition.BlockStateDefinitionVariant': {
        'ModelVariant': ('vanilla_mcdoc.assets.block_state_definition.ModelVariant', 'ModelVariant'),
    },
    'vanilla_mcdoc.assets.block_state_definition.BlockStateDefinitionVariantMap': {
        'ModelVariant': ('vanilla_mcdoc.assets.block_state_definition.ModelVariant', 'ModelVariant'),
    },
    'vanilla_mcdoc.assets.block_state_definition.ModelVariantBase': {
        'ModelRef': ('vanilla_mcdoc.assets.model.ModelRef', 'ModelRef'),
    },
    'vanilla_mcdoc.assets.block_state_definition.MultiPartAlternatives': {
        'MultiPartCondition': ('vanilla_mcdoc.assets.block_state_definition.MultiPartCondition', 'MultiPartCondition'),
    },
    'vanilla_mcdoc.assets.block_state_definition.MultiPartAnd': {
        'MultiPartCondition': ('vanilla_mcdoc.assets.block_state_definition.MultiPartCondition', 'MultiPartCondition'),
    },
    'vanilla_mcdoc.assets.equipment.Dyeable': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.assets.equipment.Equipment': {
        'Layers': ('vanilla_mcdoc.assets.equipment.Layers', 'Layers'),
        'TrimOverride': ('vanilla_mcdoc.assets.equipment.TrimOverride', 'TrimOverride'),
    },
    'vanilla_mcdoc.assets.equipment.Layer': {
        'Dyeable': ('vanilla_mcdoc.assets.equipment.Dyeable', 'Dyeable'),
    },
    'vanilla_mcdoc.assets.equipment.Layers': {
        'Layer': ('vanilla_mcdoc.assets.equipment.Layer', 'Layer'),
        'WingsLayer': ('vanilla_mcdoc.assets.equipment.WingsLayer', 'WingsLayer'),
    },
    'vanilla_mcdoc.assets.equipment.TrimOverride': {
        'PaletteRef': ('vanilla_mcdoc.assets.atlas.PaletteRef', 'PaletteRef'),
    },
    'vanilla_mcdoc.assets.font.Font': {
        'GlyphProvider': ('vanilla_mcdoc.assets.font.GlyphProvider', 'GlyphProvider'),
    },
    'vanilla_mcdoc.assets.font.GlyphProvider': {
        'FontOption': ('vanilla_mcdoc.assets.font.FontOption', 'FontOption'),
    },
    'vanilla_mcdoc.assets.font.UnihexProvider': {
        'UnihexOverrideRange': ('vanilla_mcdoc.assets.font.UnihexOverrideRange', 'UnihexOverrideRange'),
    },
    'vanilla_mcdoc.assets.item_definition.Banner': {
        'BannerAttachment': ('vanilla_mcdoc.assets.item_definition.BannerAttachment', 'BannerAttachment'),
        'DyeColor': ('vanilla_mcdoc.util.color.DyeColor', 'DyeColor'),
    },
    'vanilla_mcdoc.assets.item_definition.Bed': {
        'BedPart': ('vanilla_mcdoc.assets.item_definition.BedPart', 'BedPart'),
    },
    'vanilla_mcdoc.assets.item_definition.Chest': {
        'ChestType': ('vanilla_mcdoc.assets.item_definition.ChestType', 'ChestType'),
    },
    'vanilla_mcdoc.assets.item_definition.Compass': {
        'CompassTarget': ('vanilla_mcdoc.assets.item_definition.CompassTarget', 'CompassTarget'),
    },
    'vanilla_mcdoc.assets.item_definition.ComponentFlags': {
        'AttributeModifiersPredicate': ('vanilla_mcdoc.world.component.predicate.AttributeModifiersPredicate', 'AttributeModifiersPredicate'),
        'BundleContentsPredicate': ('vanilla_mcdoc.world.component.predicate.BundleContentsPredicate', 'BundleContentsPredicate'),
        'ContainerPredicate': ('vanilla_mcdoc.world.component.predicate.ContainerPredicate', 'ContainerPredicate'),
        'CustomData': ('vanilla_mcdoc.world.component.CustomData', 'CustomData'),
        'EnchantmentPredicate': ('vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate', 'EnchantmentPredicate'),
        'FireworkExplosionPredicate': ('vanilla_mcdoc.world.component.predicate.FireworkExplosionPredicate', 'FireworkExplosionPredicate'),
        'FireworksPredicate': ('vanilla_mcdoc.world.component.predicate.FireworksPredicate', 'FireworksPredicate'),
        'ItemDamagePredicate': ('vanilla_mcdoc.world.component.predicate.ItemDamagePredicate', 'ItemDamagePredicate'),
        'JukeboxPlayablePredicate': ('vanilla_mcdoc.world.component.predicate.JukeboxPlayablePredicate', 'JukeboxPlayablePredicate'),
        'PotionsPredicate': ('vanilla_mcdoc.world.component.predicate.PotionsPredicate', 'PotionsPredicate'),
        'TrimPredicate': ('vanilla_mcdoc.world.component.predicate.TrimPredicate', 'TrimPredicate'),
        'WritableBookPredicate': ('vanilla_mcdoc.world.component.predicate.WritableBookPredicate', 'WritableBookPredicate'),
        'WrittenBookPredicate': ('vanilla_mcdoc.world.component.predicate.WrittenBookPredicate', 'WrittenBookPredicate'),
    },
    'vanilla_mcdoc.assets.item_definition.Composite': {
        'ItemModel': ('vanilla_mcdoc.assets.item_definition.ItemModel', 'ItemModel'),
        'Transformation': ('vanilla_mcdoc.world.entity.display.Transformation', 'Transformation'),
    },
    'vanilla_mcdoc.assets.item_definition.Condition': {
        'ConditionalPropertyType': ('vanilla_mcdoc.assets.item_definition.ConditionalPropertyType', 'ConditionalPropertyType'),
        'ItemModel': ('vanilla_mcdoc.assets.item_definition.ItemModel', 'ItemModel'),
        'Transformation': ('vanilla_mcdoc.world.entity.display.Transformation', 'Transformation'),
    },
    'vanilla_mcdoc.assets.item_definition.ConstantTint': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.assets.item_definition.CopperGolemStatue': {
        'CopperGolemStatuePose': ('vanilla_mcdoc.assets.item_definition.CopperGolemStatuePose', 'CopperGolemStatuePose'),
    },
    'vanilla_mcdoc.assets.item_definition.CustomModelDataTint': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.assets.item_definition.DyeTint': {
        'ActuallyTranslucentRGB': ('vanilla_mcdoc.assets.item_definition.ActuallyTranslucentRGB', 'ActuallyTranslucentRGB'),
    },
    'vanilla_mcdoc.assets.item_definition.EndCube': {
        'EndCubeEffectType': ('vanilla_mcdoc.assets.item_definition.EndCubeEffectType', 'EndCubeEffectType'),
    },
    'vanilla_mcdoc.assets.item_definition.FireworkTint': {
        'ActuallyTranslucentRGB': ('vanilla_mcdoc.assets.item_definition.ActuallyTranslucentRGB', 'ActuallyTranslucentRGB'),
    },
    'vanilla_mcdoc.assets.item_definition.HangingSign': {
        'HangingSignAttachment': ('vanilla_mcdoc.assets.item_definition.HangingSignAttachment', 'HangingSignAttachment'),
        'WoodType': ('vanilla_mcdoc.assets.item_definition.WoodType', 'WoodType'),
    },
    'vanilla_mcdoc.assets.item_definition.Head': {
        'HeadType': ('vanilla_mcdoc.assets.item_definition.HeadType', 'HeadType'),
    },
    'vanilla_mcdoc.assets.item_definition.ItemDefinition': {
        'ItemModel': ('vanilla_mcdoc.assets.item_definition.ItemModel', 'ItemModel'),
    },
    'vanilla_mcdoc.assets.item_definition.ItemModel': {
        'ConditionalPropertyType': ('vanilla_mcdoc.assets.item_definition.ConditionalPropertyType', 'ConditionalPropertyType'),
        'NumericPropertyType': ('vanilla_mcdoc.assets.item_definition.NumericPropertyType', 'NumericPropertyType'),
        'SelectPropertyType': ('vanilla_mcdoc.assets.item_definition.SelectPropertyType', 'SelectPropertyType'),
        'Transformation': ('vanilla_mcdoc.world.entity.display.Transformation', 'Transformation'),
    },
    'vanilla_mcdoc.assets.item_definition.KeybindDown': {
        'Keybind': ('vanilla_mcdoc.util.text.Keybind', 'Keybind'),
    },
    'vanilla_mcdoc.assets.item_definition.MapColorTint': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.assets.item_definition.Model': {
        'ModelRef': ('vanilla_mcdoc.assets.model.ModelRef', 'ModelRef'),
        'ModelTint': ('vanilla_mcdoc.assets.item_definition.ModelTint', 'ModelTint'),
        'Transformation': ('vanilla_mcdoc.world.entity.display.Transformation', 'Transformation'),
    },
    'vanilla_mcdoc.assets.item_definition.PotionTint': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.assets.item_definition.RangeDispatch': {
        'ItemModel': ('vanilla_mcdoc.assets.item_definition.ItemModel', 'ItemModel'),
        'NumericPropertyType': ('vanilla_mcdoc.assets.item_definition.NumericPropertyType', 'NumericPropertyType'),
        'Transformation': ('vanilla_mcdoc.world.entity.display.Transformation', 'Transformation'),
    },
    'vanilla_mcdoc.assets.item_definition.RangeDispatchEntry': {
        'ItemModel': ('vanilla_mcdoc.assets.item_definition.ItemModel', 'ItemModel'),
    },
    'vanilla_mcdoc.assets.item_definition.Select': {
        'ItemModel': ('vanilla_mcdoc.assets.item_definition.ItemModel', 'ItemModel'),
        'SelectPropertyType': ('vanilla_mcdoc.assets.item_definition.SelectPropertyType', 'SelectPropertyType'),
        'Transformation': ('vanilla_mcdoc.world.entity.display.Transformation', 'Transformation'),
    },
    'vanilla_mcdoc.assets.item_definition.SelectCase': {
        'ItemModel': ('vanilla_mcdoc.assets.item_definition.ItemModel', 'ItemModel'),
    },
    'vanilla_mcdoc.assets.item_definition.SelectCases': {
        'SelectCase': ('vanilla_mcdoc.assets.item_definition.SelectCase', 'SelectCase'),
    },
    'vanilla_mcdoc.assets.item_definition.Special': {
        'ModelRef': ('vanilla_mcdoc.assets.model.ModelRef', 'ModelRef'),
        'SpecialModelType': ('vanilla_mcdoc.assets.item_definition.SpecialModelType', 'SpecialModelType'),
        'Transformation': ('vanilla_mcdoc.world.entity.display.Transformation', 'Transformation'),
    },
    'vanilla_mcdoc.assets.item_definition.SpecialModel': {
        'SpecialModelType': ('vanilla_mcdoc.assets.item_definition.SpecialModelType', 'SpecialModelType'),
    },
    'vanilla_mcdoc.assets.item_definition.StandingSign': {
        'StandingSignAttachment': ('vanilla_mcdoc.assets.item_definition.StandingSignAttachment', 'StandingSignAttachment'),
        'WoodType': ('vanilla_mcdoc.assets.item_definition.WoodType', 'WoodType'),
    },
    'vanilla_mcdoc.assets.item_definition.TeamTint': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.assets.item_definition.Time': {
        'TimeSource': ('vanilla_mcdoc.assets.item_definition.TimeSource', 'TimeSource'),
    },
    'vanilla_mcdoc.assets.model.Model': {
        'CustomizableItemDisplayContext': ('vanilla_mcdoc.assets.model.CustomizableItemDisplayContext', 'CustomizableItemDisplayContext'),
        'ModelElement': ('vanilla_mcdoc.assets.model.ModelElement', 'ModelElement'),
        'TextureMaterial': ('vanilla_mcdoc.assets.model.TextureMaterial', 'TextureMaterial'),
    },
    'vanilla_mcdoc.assets.model.ModelDisplay': {
        'CustomizableItemDisplayContext': ('vanilla_mcdoc.assets.model.CustomizableItemDisplayContext', 'CustomizableItemDisplayContext'),
    },
    'vanilla_mcdoc.assets.model.ModelElement': {
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
        'ModelElementRotation': ('vanilla_mcdoc.assets.model.ModelElementRotation', 'ModelElementRotation'),
    },
    'vanilla_mcdoc.assets.model.ModelElementFace': {
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
    },
    'vanilla_mcdoc.assets.model.ModelElementFaceMap': {
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
    },
    'vanilla_mcdoc.assets.model.ModelElementRotation': {
        'Axis': ('vanilla_mcdoc.util.direction.Axis', 'Axis'),
    },
    'vanilla_mcdoc.assets.model.ModelOverride': {
        'ModelRef': ('vanilla_mcdoc.assets.model.ModelRef', 'ModelRef'),
        'Predicates': ('vanilla_mcdoc.assets.model.Predicates', 'Predicates'),
    },
    'vanilla_mcdoc.assets.model.ModelOverridePredicates': {
        'Predicates': ('vanilla_mcdoc.assets.model.Predicates', 'Predicates'),
    },
    'vanilla_mcdoc.assets.model.ModelTextures': {
        'TextureMaterial': ('vanilla_mcdoc.assets.model.TextureMaterial', 'TextureMaterial'),
    },
    'vanilla_mcdoc.assets.model.MultipleAxesModelElementRotation': {
        'Axis': ('vanilla_mcdoc.util.direction.Axis', 'Axis'),
    },
    'vanilla_mcdoc.assets.model.SingleAxisModelElementRotation': {
        'Axis': ('vanilla_mcdoc.util.direction.Axis', 'Axis'),
    },
    'vanilla_mcdoc.assets.regional_compliancies.RegionalCompliancies': {
        'Code': ('vanilla_mcdoc.assets.regional_compliancies.Code', 'Code'),
        'Notification': ('vanilla_mcdoc.assets.regional_compliancies.Notification', 'Notification'),
    },
    'vanilla_mcdoc.assets.shader.post.InternalTarget': {
        'RGBA': ('vanilla_mcdoc.util.color.RGBA', 'RGBA'),
    },
    'vanilla_mcdoc.assets.shader.post.Pass': {
        'TargetInput': ('vanilla_mcdoc.assets.shader.post.TargetInput', 'TargetInput'),
        'TextureInput': ('vanilla_mcdoc.assets.shader.post.TextureInput', 'TextureInput'),
        'UniformBlocks': ('vanilla_mcdoc.assets.shader.post.UniformBlocks', 'UniformBlocks'),
    },
    'vanilla_mcdoc.assets.shader.post.PostEffect': {
        'Pass': ('vanilla_mcdoc.assets.shader.post.Pass', 'Pass'),
        'Targets': ('vanilla_mcdoc.assets.shader.post.Targets', 'Targets'),
    },
    'vanilla_mcdoc.assets.shader.post.Targets': {
        'InternalTarget': ('vanilla_mcdoc.assets.shader.post.InternalTarget', 'InternalTarget'),
    },
    'vanilla_mcdoc.assets.shader.post.UniformBlocks': {
        'UniformValue': ('vanilla_mcdoc.assets.shader.post.UniformValue', 'UniformValue'),
    },
    'vanilla_mcdoc.assets.shader.post.UniformValue': {
        'UniformValueType': ('vanilla_mcdoc.assets.shader.post.UniformValueType', 'UniformValueType'),
    },
    'vanilla_mcdoc.assets.shader.program.BlendMode': {
        'BlendFactor': ('vanilla_mcdoc.assets.shader.program.BlendFactor', 'BlendFactor'),
        'BlendFunc': ('vanilla_mcdoc.assets.shader.program.BlendFunc', 'BlendFunc'),
    },
    'vanilla_mcdoc.assets.shader.program.ShaderProgram': {
        'Defines': ('vanilla_mcdoc.assets.shader.program.Defines', 'Defines'),
        'Sampler': ('vanilla_mcdoc.assets.shader.program.Sampler', 'Sampler'),
        'Uniform': ('vanilla_mcdoc.assets.shader.program.Uniform', 'Uniform'),
    },
    'vanilla_mcdoc.assets.shader.program.Uniform': {
        'UniformType': ('vanilla_mcdoc.assets.shader.program.UniformType', 'UniformType'),
    },
    'vanilla_mcdoc.assets.sounds.Sound': {
        'SoundType': ('vanilla_mcdoc.assets.sounds.SoundType', 'SoundType'),
    },
    'vanilla_mcdoc.assets.sounds.SoundEventRegistration': {
        'Sound': ('vanilla_mcdoc.assets.sounds.Sound', 'Sound'),
    },
    'vanilla_mcdoc.assets.sounds.Sounds': {
        'SoundEventRegistration': ('vanilla_mcdoc.assets.sounds.SoundEventRegistration', 'SoundEventRegistration'),
    },
    'vanilla_mcdoc.assets.texture_meta.ColormapTextureMeta': {
        'MipmapStrategy': ('vanilla_mcdoc.assets.texture_meta.MipmapStrategy', 'MipmapStrategy'),
    },
    'vanilla_mcdoc.assets.texture_meta.GuiMeta': {
        'GuiSpriteScaling': ('vanilla_mcdoc.assets.texture_meta.GuiSpriteScaling', 'GuiSpriteScaling'),
    },
    'vanilla_mcdoc.assets.texture_meta.NineSlice': {
        'NineSliceBorder': ('vanilla_mcdoc.assets.texture_meta.NineSliceBorder', 'NineSliceBorder'),
    },
    'vanilla_mcdoc.assets.texture_meta.PaletteMeta': {
        'PaletteRef': ('vanilla_mcdoc.assets.atlas.PaletteRef', 'PaletteRef'),
    },
    'vanilla_mcdoc.assets.texture_meta.TextureMeta': {
        'GuiSpriteScaling': ('vanilla_mcdoc.assets.texture_meta.GuiSpriteScaling', 'GuiSpriteScaling'),
        'MipmapStrategy': ('vanilla_mcdoc.assets.texture_meta.MipmapStrategy', 'MipmapStrategy'),
        'PaletteRef': ('vanilla_mcdoc.assets.atlas.PaletteRef', 'PaletteRef'),
        'VillagerHatType': ('vanilla_mcdoc.assets.texture_meta.VillagerHatType', 'VillagerHatType'),
    },
    'vanilla_mcdoc.assets.texture_meta.VillagerTextureMeta': {
        'VillagerHatType': ('vanilla_mcdoc.assets.texture_meta.VillagerHatType', 'VillagerHatType'),
    },
    'vanilla_mcdoc.data.advancement.Advancement': {
        'AdvancementCriterion': ('vanilla_mcdoc.data.advancement.AdvancementCriterion', 'AdvancementCriterion'),
        'AdvancementDisplay': ('vanilla_mcdoc.data.advancement.AdvancementDisplay', 'AdvancementDisplay'),
        'AdvancementRewards': ('vanilla_mcdoc.data.advancement.AdvancementRewards', 'AdvancementRewards'),
        'RootAdvancementDisplay': ('vanilla_mcdoc.data.advancement.RootAdvancementDisplay', 'RootAdvancementDisplay'),
    },
    'vanilla_mcdoc.data.advancement.AdvancementCriteriaMap': {
        'AdvancementCriterion': ('vanilla_mcdoc.data.advancement.AdvancementCriterion', 'AdvancementCriterion'),
    },
    'vanilla_mcdoc.data.advancement.AdvancementDisplay': {
        'AdvancementFrame': ('vanilla_mcdoc.data.advancement.AdvancementFrame', 'AdvancementFrame'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.advancement.AdvancementIcon': {
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.data.advancement.AdvancementRewards': {
        'LootTableListRef': ('vanilla_mcdoc.data.loot.LootTableListRef', 'LootTableListRef'),
    },
    'vanilla_mcdoc.data.advancement.predicate.AxolotlPredicate': {
        'AxolotlVariant': ('vanilla_mcdoc.world.component.entity.AxolotlVariant', 'AxolotlVariant'),
    },
    'vanilla_mcdoc.data.advancement.predicate.BlockPredicate': {
        'Banner': ('vanilla_mcdoc.world.block.banner.Banner', 'Banner'),
        'Beacon': ('vanilla_mcdoc.world.block.beacon.Beacon', 'Beacon'),
        'Beehive': ('vanilla_mcdoc.world.block.beehive.Beehive', 'Beehive'),
        'BlockEntity': ('vanilla_mcdoc.world.block.BlockEntity', 'BlockEntity'),
        'BlockPredicateState': ('vanilla_mcdoc.data.advancement.predicate.BlockPredicateState', 'BlockPredicateState'),
        'BrewingStand': ('vanilla_mcdoc.world.block.brewing_stand.BrewingStand', 'BrewingStand'),
        'BrushableBlock': ('vanilla_mcdoc.world.block.brushable_block.BrushableBlock', 'BrushableBlock'),
        'Campfire': ('vanilla_mcdoc.world.block.campfire.Campfire', 'Campfire'),
        'ChiseledBookshelf': ('vanilla_mcdoc.world.block.chiseled_bookshelf.ChiseledBookshelf', 'ChiseledBookshelf'),
        'CommandBlock': ('vanilla_mcdoc.world.block.command_block.CommandBlock', 'CommandBlock'),
        'Comparator': ('vanilla_mcdoc.world.block.comparator.Comparator', 'Comparator'),
        'Conduit': ('vanilla_mcdoc.world.block.conduit.Conduit', 'Conduit'),
        'Container27': ('vanilla_mcdoc.world.block.container.Container27', 'Container27'),
        'Container9': ('vanilla_mcdoc.world.block.container.Container9', 'Container9'),
        'Crafter': ('vanilla_mcdoc.world.block.crafter.Crafter', 'Crafter'),
        'DataComponentExactPredicate': ('vanilla_mcdoc.world.component.DataComponentExactPredicate', 'DataComponentExactPredicate'),
        'DataComponentPredicate': ('vanilla_mcdoc.world.component.DataComponentPredicate', 'DataComponentPredicate'),
        'DecoratedPot': ('vanilla_mcdoc.world.block.decorated_pot.DecoratedPot', 'DecoratedPot'),
        'EnchantingTable': ('vanilla_mcdoc.world.block.enchanting_table.EnchantingTable', 'EnchantingTable'),
        'EndGateway': ('vanilla_mcdoc.world.block.end_gateway.EndGateway', 'EndGateway'),
        'Furnace': ('vanilla_mcdoc.world.block.furnace.Furnace', 'Furnace'),
        'Hopper': ('vanilla_mcdoc.world.block.container.Hopper', 'Hopper'),
        'Jigsaw': ('vanilla_mcdoc.world.block.jigsaw.Jigsaw', 'Jigsaw'),
        'Jukebox': ('vanilla_mcdoc.world.block.jukebox.Jukebox', 'Jukebox'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
        'Lectern': ('vanilla_mcdoc.world.block.lectern.Lectern', 'Lectern'),
        'MovingPiston': ('vanilla_mcdoc.world.block.moving_piston.MovingPiston', 'MovingPiston'),
        'PotentSulfur': ('vanilla_mcdoc.world.block.potent_sulfur.PotentSulfur', 'PotentSulfur'),
        'SculkCatalyst': ('vanilla_mcdoc.world.block.sculk_catalyst.SculkCatalyst', 'SculkCatalyst'),
        'SculkSensor': ('vanilla_mcdoc.world.block.sculk_sensor.SculkSensor', 'SculkSensor'),
        'SculkShrieker': ('vanilla_mcdoc.world.block.sculk_shrieker.SculkShrieker', 'SculkShrieker'),
        'Shelf': ('vanilla_mcdoc.world.block.container.Shelf', 'Shelf'),
        'Sign': ('vanilla_mcdoc.world.block.sign.Sign', 'Sign'),
        'Skull': ('vanilla_mcdoc.world.block.head.Skull', 'Skull'),
        'Spawner': ('vanilla_mcdoc.world.block.spawner.Spawner', 'Spawner'),
        'StructureBlock': ('vanilla_mcdoc.world.block.structure_block.StructureBlock', 'StructureBlock'),
        'TestBlock': ('vanilla_mcdoc.world.block.test_block.TestBlock', 'TestBlock'),
        'TestInstanceBlock': ('vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlock', 'TestInstanceBlock'),
        'TrialSpawner': ('vanilla_mcdoc.world.block.spawner.TrialSpawner', 'TrialSpawner'),
        'Vault': ('vanilla_mcdoc.world.block.vault.Vault', 'Vault'),
    },
    'vanilla_mcdoc.data.advancement.predicate.BlockPredicateState': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.BoatPredicate': {
        'BoatType': ('vanilla_mcdoc.world.entity.boat.BoatType', 'BoatType'),
    },
    'vanilla_mcdoc.data.advancement.predicate.DamagePredicate': {
        'DamageSourcePredicate': ('vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate', 'DamageSourcePredicate'),
        'EntityPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityPredicate', 'EntityPredicate'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate': {
        'DamageTagPredicate': ('vanilla_mcdoc.data.advancement.predicate.DamageTagPredicate', 'DamageTagPredicate'),
        'EntityPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityPredicate', 'EntityPredicate'),
    },
    'vanilla_mcdoc.data.advancement.predicate.DistancePredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.EntityEffectsPredicate': {
        'MobEffectPredicate': ('vanilla_mcdoc.data.advancement.predicate.MobEffectPredicate', 'MobEffectPredicate'),
    },
    'vanilla_mcdoc.data.advancement.predicate.EntityEquipmentPredicate': {
        'EquipmentPredicateSlot': ('vanilla_mcdoc.data.advancement.predicate.EquipmentPredicateSlot', 'EquipmentPredicateSlot'),
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
    },
    'vanilla_mcdoc.data.advancement.predicate.EntitySlotsPredicate': {
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
    },
    'vanilla_mcdoc.data.advancement.predicate.EntitySubPredicateMap': {
        'AcceleratingProjectileBase': ('vanilla_mcdoc.world.entity.projectile.fireball.AcceleratingProjectileBase', 'AcceleratingProjectileBase'),
        'Allay': ('vanilla_mcdoc.world.entity.mob.allay.Allay', 'Allay'),
        'AreaEffectCloud': ('vanilla_mcdoc.world.entity.area_effect_cloud.AreaEffectCloud', 'AreaEffectCloud'),
        'Armadillo': ('vanilla_mcdoc.world.entity.mob.breedable.armadillo.Armadillo', 'Armadillo'),
        'ArmorStand': ('vanilla_mcdoc.world.entity.mob.armor_stand.ArmorStand', 'ArmorStand'),
        'Arrow': ('vanilla_mcdoc.world.entity.projectile.arrow.Arrow', 'Arrow'),
        'Axolotl': ('vanilla_mcdoc.world.entity.mob.breedable.axolotl.Axolotl', 'Axolotl'),
        'Bat': ('vanilla_mcdoc.world.entity.mob.bat.Bat', 'Bat'),
        'Bee': ('vanilla_mcdoc.world.entity.mob.breedable.bee.Bee', 'Bee'),
        'BlockAttachedEntity': ('vanilla_mcdoc.world.entity.BlockAttachedEntity', 'BlockAttachedEntity'),
        'BlockDisplay': ('vanilla_mcdoc.world.entity.display.BlockDisplay', 'BlockDisplay'),
        'Boat': ('vanilla_mcdoc.world.entity.boat.Boat', 'Boat'),
        'Bogged': ('vanilla_mcdoc.world.entity.mob.bogged.Bogged', 'Bogged'),
        'Breedable': ('vanilla_mcdoc.world.entity.mob.breedable.Breedable', 'Breedable'),
        'Camel': ('vanilla_mcdoc.world.entity.mob.breedable.horse.Camel', 'Camel'),
        'Cat': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.Cat', 'Cat'),
        'ChestBoat': ('vanilla_mcdoc.world.entity.boat.ChestBoat', 'ChestBoat'),
        'ChestMinecart': ('vanilla_mcdoc.world.entity.minecart.ChestMinecart', 'ChestMinecart'),
        'ChestedHorse': ('vanilla_mcdoc.world.entity.mob.breedable.horse.ChestedHorse', 'ChestedHorse'),
        'Chicken': ('vanilla_mcdoc.world.entity.mob.breedable.chicken.Chicken', 'Chicken'),
        'CommandBlockMinecart': ('vanilla_mcdoc.world.entity.minecart.CommandBlockMinecart', 'CommandBlockMinecart'),
        'CopperGolem': ('vanilla_mcdoc.world.entity.mob.copper_golem.CopperGolem', 'CopperGolem'),
        'Cow': ('vanilla_mcdoc.world.entity.mob.breedable.cow.Cow', 'Cow'),
        'Creaking': ('vanilla_mcdoc.world.entity.mob.creaking.Creaking', 'Creaking'),
        'Creeper': ('vanilla_mcdoc.world.entity.mob.creeper.Creeper', 'Creeper'),
        'Cushion': ('vanilla_mcdoc.world.entity.cushion.Cushion', 'Cushion'),
        'DataComponentExactPredicate': ('vanilla_mcdoc.world.component.DataComponentExactPredicate', 'DataComponentExactPredicate'),
        'DataComponentPredicate': ('vanilla_mcdoc.world.component.DataComponentPredicate', 'DataComponentPredicate'),
        'DespawnableProjectileBase': ('vanilla_mcdoc.world.entity.projectile.fireball.DespawnableProjectileBase', 'DespawnableProjectileBase'),
        'DistancePredicate': ('vanilla_mcdoc.data.advancement.predicate.DistancePredicate', 'DistancePredicate'),
        'Dolphin': ('vanilla_mcdoc.world.entity.mob.dolphin.Dolphin', 'Dolphin'),
        'EndCrystal': ('vanilla_mcdoc.world.entity.end_crystal.EndCrystal', 'EndCrystal'),
        'EnderDragon': ('vanilla_mcdoc.world.entity.mob.ender_dragon.EnderDragon', 'EnderDragon'),
        'Enderman': ('vanilla_mcdoc.world.entity.mob.enderman.Enderman', 'Enderman'),
        'Endermite': ('vanilla_mcdoc.world.entity.mob.endermite.Endermite', 'Endermite'),
        'EntityEffectsPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityEffectsPredicate', 'EntityEffectsPredicate'),
        'EntityEquipmentPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityEquipmentPredicate', 'EntityEquipmentPredicate'),
        'EntityFlagsPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityFlagsPredicate', 'EntityFlagsPredicate'),
        'EntityPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityPredicate', 'EntityPredicate'),
        'EntitySlotsPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntitySlotsPredicate', 'EntitySlotsPredicate'),
        'EntityTagPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityTagPredicate', 'EntityTagPredicate'),
        'EntityTypePredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityTypePredicate', 'EntityTypePredicate'),
        'EvokerFangs': ('vanilla_mcdoc.world.entity.evoker_fangs.EvokerFangs', 'EvokerFangs'),
        'ExperienceOrb': ('vanilla_mcdoc.world.entity.experience_orb.ExperienceOrb', 'ExperienceOrb'),
        'EyeOfEnder': ('vanilla_mcdoc.world.entity.eye_of_ender.EyeOfEnder', 'EyeOfEnder'),
        'FallingBlock': ('vanilla_mcdoc.world.entity.falling_block.FallingBlock', 'FallingBlock'),
        'FireWorkRocket': ('vanilla_mcdoc.world.entity.projectile.firework_rocket.FireWorkRocket', 'FireWorkRocket'),
        'FireballBase': ('vanilla_mcdoc.world.entity.projectile.fireball.FireballBase', 'FireballBase'),
        'Fish': ('vanilla_mcdoc.world.entity.mob.fish.Fish', 'Fish'),
        'FishingHookPredicate': ('vanilla_mcdoc.data.advancement.predicate.FishingHookPredicate', 'FishingHookPredicate'),
        'Fox': ('vanilla_mcdoc.world.entity.mob.breedable.fox.Fox', 'Fox'),
        'Frog': ('vanilla_mcdoc.world.entity.mob.breedable.frog.Frog', 'Frog'),
        'FurnaceMinecart': ('vanilla_mcdoc.world.entity.minecart.FurnaceMinecart', 'FurnaceMinecart'),
        'Ghast': ('vanilla_mcdoc.world.entity.mob.ghast.Ghast', 'Ghast'),
        'GlowSquid': ('vanilla_mcdoc.world.entity.mob.glow_squid.GlowSquid', 'GlowSquid'),
        'Goat': ('vanilla_mcdoc.world.entity.mob.breedable.goat.Goat', 'Goat'),
        'HappyGhast': ('vanilla_mcdoc.world.entity.mob.happy_ghast.HappyGhast', 'HappyGhast'),
        'Hoglin': ('vanilla_mcdoc.world.entity.mob.breedable.hoglin.Hoglin', 'Hoglin'),
        'HopperMinecart': ('vanilla_mcdoc.world.entity.minecart.HopperMinecart', 'HopperMinecart'),
        'Horse': ('vanilla_mcdoc.world.entity.mob.breedable.horse.Horse', 'Horse'),
        'HorseBase': ('vanilla_mcdoc.world.entity.mob.breedable.horse.HorseBase', 'HorseBase'),
        'Interaction': ('vanilla_mcdoc.world.entity.interaction.Interaction', 'Interaction'),
        'IronGolem': ('vanilla_mcdoc.world.entity.mob.iron_golem.IronGolem', 'IronGolem'),
        'Item': ('vanilla_mcdoc.world.entity.item.Item', 'Item'),
        'ItemDisplay': ('vanilla_mcdoc.world.entity.display.ItemDisplay', 'ItemDisplay'),
        'ItemFrame': ('vanilla_mcdoc.world.entity.item_frame.ItemFrame', 'ItemFrame'),
        'LargeFireball': ('vanilla_mcdoc.world.entity.projectile.fireball.LargeFireball', 'LargeFireball'),
        'LightningBoltPredicate': ('vanilla_mcdoc.data.advancement.predicate.LightningBoltPredicate', 'LightningBoltPredicate'),
        'Llama': ('vanilla_mcdoc.world.entity.mob.breedable.horse.Llama', 'Llama'),
        'LlamaSpit': ('vanilla_mcdoc.world.entity.projectile.LlamaSpit', 'LlamaSpit'),
        'LocationPredicate': ('vanilla_mcdoc.data.advancement.predicate.LocationPredicate', 'LocationPredicate'),
        'Mannequin': ('vanilla_mcdoc.world.entity.mob.mannequin.Mannequin', 'Mannequin'),
        'Marker': ('vanilla_mcdoc.world.entity.marker.Marker', 'Marker'),
        'Minecart': ('vanilla_mcdoc.world.entity.minecart.Minecart', 'Minecart'),
        'MobBase': ('vanilla_mcdoc.world.entity.mob.MobBase', 'MobBase'),
        'Mooshroom': ('vanilla_mcdoc.world.entity.mob.breedable.mooshroom.Mooshroom', 'Mooshroom'),
        'MovementPredicate': ('vanilla_mcdoc.data.advancement.predicate.MovementPredicate', 'MovementPredicate'),
        'Ocelot': ('vanilla_mcdoc.world.entity.mob.breedable.ocelot.Ocelot', 'Ocelot'),
        'OminousItemSpawner': ('vanilla_mcdoc.world.entity.ominous_item_spawner.OminousItemSpawner', 'OminousItemSpawner'),
        'Painting': ('vanilla_mcdoc.world.entity.painting.Painting', 'Painting'),
        'Panda': ('vanilla_mcdoc.world.entity.mob.breedable.panda.Panda', 'Panda'),
        'Parrot': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.Parrot', 'Parrot'),
        'Phantom': ('vanilla_mcdoc.world.entity.mob.phantom.Phantom', 'Phantom'),
        'Pig': ('vanilla_mcdoc.world.entity.mob.breedable.saddled.Pig', 'Pig'),
        'Piglin': ('vanilla_mcdoc.world.entity.mob.piglin.Piglin', 'Piglin'),
        'PiglinBase': ('vanilla_mcdoc.world.entity.mob.piglin.PiglinBase', 'PiglinBase'),
        'Pillager': ('vanilla_mcdoc.world.entity.mob.raider.Pillager', 'Pillager'),
        'Player': ('vanilla_mcdoc.world.entity.mob.player.Player', 'Player'),
        'PlayerPredicate': ('vanilla_mcdoc.data.advancement.predicate.PlayerPredicate', 'PlayerPredicate'),
        'PolarBear': ('vanilla_mcdoc.world.entity.mob.breedable.polar_bear.PolarBear', 'PolarBear'),
        'Potion': ('vanilla_mcdoc.world.entity.projectile.throwable.Potion', 'Potion'),
        'Pufferfish': ('vanilla_mcdoc.world.entity.mob.fish.Pufferfish', 'Pufferfish'),
        'Rabbit': ('vanilla_mcdoc.world.entity.mob.breedable.rabbit.Rabbit', 'Rabbit'),
        'RaiderBase': ('vanilla_mcdoc.world.entity.mob.raider.RaiderBase', 'RaiderBase'),
        'RaiderPredicate': ('vanilla_mcdoc.data.advancement.predicate.RaiderPredicate', 'RaiderPredicate'),
        'Ravager': ('vanilla_mcdoc.world.entity.mob.raider.Ravager', 'Ravager'),
        'Saddled': ('vanilla_mcdoc.world.entity.mob.breedable.saddled.Saddled', 'Saddled'),
        'Salmon': ('vanilla_mcdoc.world.entity.mob.fish.Salmon', 'Salmon'),
        'Sheep': ('vanilla_mcdoc.world.entity.mob.breedable.sheep.Sheep', 'Sheep'),
        'SheepPredicate': ('vanilla_mcdoc.data.advancement.predicate.SheepPredicate', 'SheepPredicate'),
        'Shulker': ('vanilla_mcdoc.world.entity.mob.shulker.Shulker', 'Shulker'),
        'ShulkerBullet': ('vanilla_mcdoc.world.entity.projectile.shulker_bullet.ShulkerBullet', 'ShulkerBullet'),
        'Skeleton': ('vanilla_mcdoc.world.entity.mob.skeleton.Skeleton', 'Skeleton'),
        'SkeletonHorse': ('vanilla_mcdoc.world.entity.mob.breedable.horse.SkeletonHorse', 'SkeletonHorse'),
        'Slime': ('vanilla_mcdoc.world.entity.mob.slime.Slime', 'Slime'),
        'SlimePredicate': ('vanilla_mcdoc.data.advancement.predicate.SlimePredicate', 'SlimePredicate'),
        'SnowGolem': ('vanilla_mcdoc.world.entity.mob.snow_golem.SnowGolem', 'SnowGolem'),
        'SpawnerMinecart': ('vanilla_mcdoc.world.entity.minecart.SpawnerMinecart', 'SpawnerMinecart'),
        'SpectralArrow': ('vanilla_mcdoc.world.entity.projectile.arrow.SpectralArrow', 'SpectralArrow'),
        'Spellcaster': ('vanilla_mcdoc.world.entity.mob.raider.Spellcaster', 'Spellcaster'),
        'Squid': ('vanilla_mcdoc.world.entity.mob.Squid', 'Squid'),
        'SulfurCube': ('vanilla_mcdoc.world.entity.mob.slime.SulfurCube', 'SulfurCube'),
        'Tadpole': ('vanilla_mcdoc.world.entity.mob.tadpole.Tadpole', 'Tadpole'),
        'Tamable': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.Tamable', 'Tamable'),
        'TextDisplay': ('vanilla_mcdoc.world.entity.display.TextDisplay', 'TextDisplay'),
        'ThrowableItem': ('vanilla_mcdoc.world.entity.projectile.throwable.ThrowableItem', 'ThrowableItem'),
        'Tnt': ('vanilla_mcdoc.world.entity.tnt.Tnt', 'Tnt'),
        'TntMinecart': ('vanilla_mcdoc.world.entity.minecart.TntMinecart', 'TntMinecart'),
        'TraderLlama': ('vanilla_mcdoc.world.entity.mob.breedable.horse.TraderLlama', 'TraderLlama'),
        'Trident': ('vanilla_mcdoc.world.entity.projectile.arrow.Trident', 'Trident'),
        'TropicalFish': ('vanilla_mcdoc.world.entity.mob.fish.TropicalFish', 'TropicalFish'),
        'Turtle': ('vanilla_mcdoc.world.entity.mob.breedable.turtle.Turtle', 'Turtle'),
        'Vex': ('vanilla_mcdoc.world.entity.mob.vex.Vex', 'Vex'),
        'Villager': ('vanilla_mcdoc.world.entity.mob.breedable.villager.Villager', 'Villager'),
        'Vindicator': ('vanilla_mcdoc.world.entity.mob.raider.Vindicator', 'Vindicator'),
        'WanderingTrader': ('vanilla_mcdoc.world.entity.mob.breedable.villager.WanderingTrader', 'WanderingTrader'),
        'Warden': ('vanilla_mcdoc.world.entity.mob.warden.Warden', 'Warden'),
        'Wither': ('vanilla_mcdoc.world.entity.mob.wither.Wither', 'Wither'),
        'WitherSkull': ('vanilla_mcdoc.world.entity.projectile.fireball.WitherSkull', 'WitherSkull'),
        'Wolf': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.Wolf', 'Wolf'),
        'Zoglin': ('vanilla_mcdoc.world.entity.mob.zoglin.Zoglin', 'Zoglin'),
        'Zombie': ('vanilla_mcdoc.world.entity.mob.zombie.Zombie', 'Zombie'),
        'ZombiePigman': ('vanilla_mcdoc.world.entity.mob.zombified_piglin.ZombiePigman', 'ZombiePigman'),
        'ZombieVillager': ('vanilla_mcdoc.world.entity.mob.zombie.ZombieVillager', 'ZombieVillager'),
    },
    'vanilla_mcdoc.data.advancement.predicate.FluidPredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.FluidPredicateState': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.FoodPredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.FoxPredicate': {
        'FoxType': ('vanilla_mcdoc.world.component.entity.FoxType', 'FoxType'),
    },
    'vanilla_mcdoc.data.advancement.predicate.HorsePredicate': {
        'HorseVariant': ('vanilla_mcdoc.world.component.entity.HorseVariant', 'HorseVariant'),
    },
    'vanilla_mcdoc.data.advancement.predicate.ItemPredicate': {
        'DataComponentExactPredicate': ('vanilla_mcdoc.world.component.DataComponentExactPredicate', 'DataComponentExactPredicate'),
        'DataComponentPredicate': ('vanilla_mcdoc.world.component.DataComponentPredicate', 'DataComponentPredicate'),
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.LightningBoltPredicate': {
        'EntityPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityPredicate', 'EntityPredicate'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.LlamaPredicate': {
        'LlamaVariant': ('vanilla_mcdoc.world.component.entity.LlamaVariant', 'LlamaVariant'),
    },
    'vanilla_mcdoc.data.advancement.predicate.LocationPredicate': {
        'BlockPredicate': ('vanilla_mcdoc.data.advancement.predicate.BlockPredicate', 'BlockPredicate'),
        'FluidPredicate': ('vanilla_mcdoc.data.advancement.predicate.FluidPredicate', 'FluidPredicate'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.LocationPredicateLight': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.LocationPredicatePosition': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.MobEffectPredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.MooshroomPredicate': {
        'MooshroomType': ('vanilla_mcdoc.world.component.entity.MooshroomType', 'MooshroomType'),
    },
    'vanilla_mcdoc.data.advancement.predicate.MovementPredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.OldEntityPredicate': {
        'AcceleratingProjectileBase': ('vanilla_mcdoc.world.entity.projectile.fireball.AcceleratingProjectileBase', 'AcceleratingProjectileBase'),
        'Allay': ('vanilla_mcdoc.world.entity.mob.allay.Allay', 'Allay'),
        'AreaEffectCloud': ('vanilla_mcdoc.world.entity.area_effect_cloud.AreaEffectCloud', 'AreaEffectCloud'),
        'Armadillo': ('vanilla_mcdoc.world.entity.mob.breedable.armadillo.Armadillo', 'Armadillo'),
        'ArmorStand': ('vanilla_mcdoc.world.entity.mob.armor_stand.ArmorStand', 'ArmorStand'),
        'Arrow': ('vanilla_mcdoc.world.entity.projectile.arrow.Arrow', 'Arrow'),
        'Axolotl': ('vanilla_mcdoc.world.entity.mob.breedable.axolotl.Axolotl', 'Axolotl'),
        'Bat': ('vanilla_mcdoc.world.entity.mob.bat.Bat', 'Bat'),
        'Bee': ('vanilla_mcdoc.world.entity.mob.breedable.bee.Bee', 'Bee'),
        'BlockAttachedEntity': ('vanilla_mcdoc.world.entity.BlockAttachedEntity', 'BlockAttachedEntity'),
        'BlockDisplay': ('vanilla_mcdoc.world.entity.display.BlockDisplay', 'BlockDisplay'),
        'Boat': ('vanilla_mcdoc.world.entity.boat.Boat', 'Boat'),
        'Bogged': ('vanilla_mcdoc.world.entity.mob.bogged.Bogged', 'Bogged'),
        'Breedable': ('vanilla_mcdoc.world.entity.mob.breedable.Breedable', 'Breedable'),
        'Camel': ('vanilla_mcdoc.world.entity.mob.breedable.horse.Camel', 'Camel'),
        'Cat': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.Cat', 'Cat'),
        'ChestBoat': ('vanilla_mcdoc.world.entity.boat.ChestBoat', 'ChestBoat'),
        'ChestMinecart': ('vanilla_mcdoc.world.entity.minecart.ChestMinecart', 'ChestMinecart'),
        'ChestedHorse': ('vanilla_mcdoc.world.entity.mob.breedable.horse.ChestedHorse', 'ChestedHorse'),
        'Chicken': ('vanilla_mcdoc.world.entity.mob.breedable.chicken.Chicken', 'Chicken'),
        'CommandBlockMinecart': ('vanilla_mcdoc.world.entity.minecart.CommandBlockMinecart', 'CommandBlockMinecart'),
        'CopperGolem': ('vanilla_mcdoc.world.entity.mob.copper_golem.CopperGolem', 'CopperGolem'),
        'Cow': ('vanilla_mcdoc.world.entity.mob.breedable.cow.Cow', 'Cow'),
        'Creaking': ('vanilla_mcdoc.world.entity.mob.creaking.Creaking', 'Creaking'),
        'Creeper': ('vanilla_mcdoc.world.entity.mob.creeper.Creeper', 'Creeper'),
        'Cushion': ('vanilla_mcdoc.world.entity.cushion.Cushion', 'Cushion'),
        'DataComponentExactPredicate': ('vanilla_mcdoc.world.component.DataComponentExactPredicate', 'DataComponentExactPredicate'),
        'DataComponentPredicate': ('vanilla_mcdoc.world.component.DataComponentPredicate', 'DataComponentPredicate'),
        'DespawnableProjectileBase': ('vanilla_mcdoc.world.entity.projectile.fireball.DespawnableProjectileBase', 'DespawnableProjectileBase'),
        'DistancePredicate': ('vanilla_mcdoc.data.advancement.predicate.DistancePredicate', 'DistancePredicate'),
        'Dolphin': ('vanilla_mcdoc.world.entity.mob.dolphin.Dolphin', 'Dolphin'),
        'EndCrystal': ('vanilla_mcdoc.world.entity.end_crystal.EndCrystal', 'EndCrystal'),
        'EnderDragon': ('vanilla_mcdoc.world.entity.mob.ender_dragon.EnderDragon', 'EnderDragon'),
        'Enderman': ('vanilla_mcdoc.world.entity.mob.enderman.Enderman', 'Enderman'),
        'Endermite': ('vanilla_mcdoc.world.entity.mob.endermite.Endermite', 'Endermite'),
        'EntityEffectsPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityEffectsPredicate', 'EntityEffectsPredicate'),
        'EntityEquipmentPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityEquipmentPredicate', 'EntityEquipmentPredicate'),
        'EntityFlagsPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityFlagsPredicate', 'EntityFlagsPredicate'),
        'EntityPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityPredicate', 'EntityPredicate'),
        'EntitySlotsPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntitySlotsPredicate', 'EntitySlotsPredicate'),
        'EntitySubPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntitySubPredicate', 'EntitySubPredicate'),
        'EntityTypePredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityTypePredicate', 'EntityTypePredicate'),
        'EvokerFangs': ('vanilla_mcdoc.world.entity.evoker_fangs.EvokerFangs', 'EvokerFangs'),
        'ExperienceOrb': ('vanilla_mcdoc.world.entity.experience_orb.ExperienceOrb', 'ExperienceOrb'),
        'EyeOfEnder': ('vanilla_mcdoc.world.entity.eye_of_ender.EyeOfEnder', 'EyeOfEnder'),
        'FallingBlock': ('vanilla_mcdoc.world.entity.falling_block.FallingBlock', 'FallingBlock'),
        'FireWorkRocket': ('vanilla_mcdoc.world.entity.projectile.firework_rocket.FireWorkRocket', 'FireWorkRocket'),
        'FireballBase': ('vanilla_mcdoc.world.entity.projectile.fireball.FireballBase', 'FireballBase'),
        'Fish': ('vanilla_mcdoc.world.entity.mob.fish.Fish', 'Fish'),
        'Fox': ('vanilla_mcdoc.world.entity.mob.breedable.fox.Fox', 'Fox'),
        'Frog': ('vanilla_mcdoc.world.entity.mob.breedable.frog.Frog', 'Frog'),
        'FurnaceMinecart': ('vanilla_mcdoc.world.entity.minecart.FurnaceMinecart', 'FurnaceMinecart'),
        'Ghast': ('vanilla_mcdoc.world.entity.mob.ghast.Ghast', 'Ghast'),
        'GlowSquid': ('vanilla_mcdoc.world.entity.mob.glow_squid.GlowSquid', 'GlowSquid'),
        'Goat': ('vanilla_mcdoc.world.entity.mob.breedable.goat.Goat', 'Goat'),
        'HappyGhast': ('vanilla_mcdoc.world.entity.mob.happy_ghast.HappyGhast', 'HappyGhast'),
        'Hoglin': ('vanilla_mcdoc.world.entity.mob.breedable.hoglin.Hoglin', 'Hoglin'),
        'HopperMinecart': ('vanilla_mcdoc.world.entity.minecart.HopperMinecart', 'HopperMinecart'),
        'Horse': ('vanilla_mcdoc.world.entity.mob.breedable.horse.Horse', 'Horse'),
        'HorseBase': ('vanilla_mcdoc.world.entity.mob.breedable.horse.HorseBase', 'HorseBase'),
        'Interaction': ('vanilla_mcdoc.world.entity.interaction.Interaction', 'Interaction'),
        'IronGolem': ('vanilla_mcdoc.world.entity.mob.iron_golem.IronGolem', 'IronGolem'),
        'Item': ('vanilla_mcdoc.world.entity.item.Item', 'Item'),
        'ItemDisplay': ('vanilla_mcdoc.world.entity.display.ItemDisplay', 'ItemDisplay'),
        'ItemFrame': ('vanilla_mcdoc.world.entity.item_frame.ItemFrame', 'ItemFrame'),
        'LargeFireball': ('vanilla_mcdoc.world.entity.projectile.fireball.LargeFireball', 'LargeFireball'),
        'Llama': ('vanilla_mcdoc.world.entity.mob.breedable.horse.Llama', 'Llama'),
        'LlamaSpit': ('vanilla_mcdoc.world.entity.projectile.LlamaSpit', 'LlamaSpit'),
        'LocationPredicate': ('vanilla_mcdoc.data.advancement.predicate.LocationPredicate', 'LocationPredicate'),
        'Mannequin': ('vanilla_mcdoc.world.entity.mob.mannequin.Mannequin', 'Mannequin'),
        'Marker': ('vanilla_mcdoc.world.entity.marker.Marker', 'Marker'),
        'Minecart': ('vanilla_mcdoc.world.entity.minecart.Minecart', 'Minecart'),
        'MobBase': ('vanilla_mcdoc.world.entity.mob.MobBase', 'MobBase'),
        'Mooshroom': ('vanilla_mcdoc.world.entity.mob.breedable.mooshroom.Mooshroom', 'Mooshroom'),
        'MovementPredicate': ('vanilla_mcdoc.data.advancement.predicate.MovementPredicate', 'MovementPredicate'),
        'Ocelot': ('vanilla_mcdoc.world.entity.mob.breedable.ocelot.Ocelot', 'Ocelot'),
        'OminousItemSpawner': ('vanilla_mcdoc.world.entity.ominous_item_spawner.OminousItemSpawner', 'OminousItemSpawner'),
        'Painting': ('vanilla_mcdoc.world.entity.painting.Painting', 'Painting'),
        'Panda': ('vanilla_mcdoc.world.entity.mob.breedable.panda.Panda', 'Panda'),
        'Parrot': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.Parrot', 'Parrot'),
        'Phantom': ('vanilla_mcdoc.world.entity.mob.phantom.Phantom', 'Phantom'),
        'Pig': ('vanilla_mcdoc.world.entity.mob.breedable.saddled.Pig', 'Pig'),
        'Piglin': ('vanilla_mcdoc.world.entity.mob.piglin.Piglin', 'Piglin'),
        'PiglinBase': ('vanilla_mcdoc.world.entity.mob.piglin.PiglinBase', 'PiglinBase'),
        'Pillager': ('vanilla_mcdoc.world.entity.mob.raider.Pillager', 'Pillager'),
        'Player': ('vanilla_mcdoc.world.entity.mob.player.Player', 'Player'),
        'PolarBear': ('vanilla_mcdoc.world.entity.mob.breedable.polar_bear.PolarBear', 'PolarBear'),
        'Potion': ('vanilla_mcdoc.world.entity.projectile.throwable.Potion', 'Potion'),
        'Pufferfish': ('vanilla_mcdoc.world.entity.mob.fish.Pufferfish', 'Pufferfish'),
        'Rabbit': ('vanilla_mcdoc.world.entity.mob.breedable.rabbit.Rabbit', 'Rabbit'),
        'RaiderBase': ('vanilla_mcdoc.world.entity.mob.raider.RaiderBase', 'RaiderBase'),
        'Ravager': ('vanilla_mcdoc.world.entity.mob.raider.Ravager', 'Ravager'),
        'Saddled': ('vanilla_mcdoc.world.entity.mob.breedable.saddled.Saddled', 'Saddled'),
        'Salmon': ('vanilla_mcdoc.world.entity.mob.fish.Salmon', 'Salmon'),
        'Sheep': ('vanilla_mcdoc.world.entity.mob.breedable.sheep.Sheep', 'Sheep'),
        'Shulker': ('vanilla_mcdoc.world.entity.mob.shulker.Shulker', 'Shulker'),
        'ShulkerBullet': ('vanilla_mcdoc.world.entity.projectile.shulker_bullet.ShulkerBullet', 'ShulkerBullet'),
        'Skeleton': ('vanilla_mcdoc.world.entity.mob.skeleton.Skeleton', 'Skeleton'),
        'SkeletonHorse': ('vanilla_mcdoc.world.entity.mob.breedable.horse.SkeletonHorse', 'SkeletonHorse'),
        'Slime': ('vanilla_mcdoc.world.entity.mob.slime.Slime', 'Slime'),
        'SnowGolem': ('vanilla_mcdoc.world.entity.mob.snow_golem.SnowGolem', 'SnowGolem'),
        'SpawnerMinecart': ('vanilla_mcdoc.world.entity.minecart.SpawnerMinecart', 'SpawnerMinecart'),
        'SpectralArrow': ('vanilla_mcdoc.world.entity.projectile.arrow.SpectralArrow', 'SpectralArrow'),
        'Spellcaster': ('vanilla_mcdoc.world.entity.mob.raider.Spellcaster', 'Spellcaster'),
        'Squid': ('vanilla_mcdoc.world.entity.mob.Squid', 'Squid'),
        'SulfurCube': ('vanilla_mcdoc.world.entity.mob.slime.SulfurCube', 'SulfurCube'),
        'Tadpole': ('vanilla_mcdoc.world.entity.mob.tadpole.Tadpole', 'Tadpole'),
        'Tamable': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.Tamable', 'Tamable'),
        'TextDisplay': ('vanilla_mcdoc.world.entity.display.TextDisplay', 'TextDisplay'),
        'ThrowableItem': ('vanilla_mcdoc.world.entity.projectile.throwable.ThrowableItem', 'ThrowableItem'),
        'Tnt': ('vanilla_mcdoc.world.entity.tnt.Tnt', 'Tnt'),
        'TntMinecart': ('vanilla_mcdoc.world.entity.minecart.TntMinecart', 'TntMinecart'),
        'TraderLlama': ('vanilla_mcdoc.world.entity.mob.breedable.horse.TraderLlama', 'TraderLlama'),
        'Trident': ('vanilla_mcdoc.world.entity.projectile.arrow.Trident', 'Trident'),
        'TropicalFish': ('vanilla_mcdoc.world.entity.mob.fish.TropicalFish', 'TropicalFish'),
        'Turtle': ('vanilla_mcdoc.world.entity.mob.breedable.turtle.Turtle', 'Turtle'),
        'Vex': ('vanilla_mcdoc.world.entity.mob.vex.Vex', 'Vex'),
        'Villager': ('vanilla_mcdoc.world.entity.mob.breedable.villager.Villager', 'Villager'),
        'Vindicator': ('vanilla_mcdoc.world.entity.mob.raider.Vindicator', 'Vindicator'),
        'WanderingTrader': ('vanilla_mcdoc.world.entity.mob.breedable.villager.WanderingTrader', 'WanderingTrader'),
        'Warden': ('vanilla_mcdoc.world.entity.mob.warden.Warden', 'Warden'),
        'Wither': ('vanilla_mcdoc.world.entity.mob.wither.Wither', 'Wither'),
        'WitherSkull': ('vanilla_mcdoc.world.entity.projectile.fireball.WitherSkull', 'WitherSkull'),
        'Wolf': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.Wolf', 'Wolf'),
        'Zoglin': ('vanilla_mcdoc.world.entity.mob.zoglin.Zoglin', 'Zoglin'),
        'Zombie': ('vanilla_mcdoc.world.entity.mob.zombie.Zombie', 'Zombie'),
        'ZombiePigman': ('vanilla_mcdoc.world.entity.mob.zombified_piglin.ZombiePigman', 'ZombiePigman'),
        'ZombieVillager': ('vanilla_mcdoc.world.entity.mob.zombie.ZombieVillager', 'ZombieVillager'),
    },
    'vanilla_mcdoc.data.advancement.predicate.ParrotPredicate': {
        'ParrotVariant': ('vanilla_mcdoc.world.component.entity.ParrotVariant', 'ParrotVariant'),
    },
    'vanilla_mcdoc.data.advancement.predicate.PlayerPredicate': {
        'EntityPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityPredicate', 'EntityPredicate'),
        'GameMode': ('vanilla_mcdoc.data.advancement.predicate.GameMode', 'GameMode'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
        'StatisticPredicate': ('vanilla_mcdoc.data.advancement.predicate.StatisticPredicate', 'StatisticPredicate'),
    },
    'vanilla_mcdoc.data.advancement.predicate.PostComponentsItemPredicate': {
        'DataComponentExactPredicate': ('vanilla_mcdoc.world.component.DataComponentExactPredicate', 'DataComponentExactPredicate'),
        'DataComponentPredicate': ('vanilla_mcdoc.world.component.DataComponentPredicate', 'DataComponentPredicate'),
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.PreComponentsItemPredicate': {
        'EnchantmentPredicate': ('vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate', 'EnchantmentPredicate'),
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.RabbitPredicate': {
        'RabbitVariant': ('vanilla_mcdoc.world.component.entity.RabbitVariant', 'RabbitVariant'),
    },
    'vanilla_mcdoc.data.advancement.predicate.SalmonPredicate': {
        'SalmonVariant': ('vanilla_mcdoc.data.advancement.predicate.SalmonVariant', 'SalmonVariant'),
    },
    'vanilla_mcdoc.data.advancement.predicate.SlimePredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.StatisticPredicate': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.predicate.TropicalFishPredicate': {
        'TropicalFishPattern': ('vanilla_mcdoc.world.component.entity.TropicalFishPattern', 'TropicalFishPattern'),
    },
    'vanilla_mcdoc.data.advancement.trigger.BlockStateConditions': {
        'BlockListRef': ('vanilla_mcdoc.util.registry_ref.BlockListRef', 'BlockListRef'),
    },
    'vanilla_mcdoc.data.advancement.trigger.InventoryChangedSlots': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.advancement.trigger.ItemUesdOnLocationConditions': {
        'AdvancementLocationPredicate': ('vanilla_mcdoc.data.advancement.trigger.AdvancementLocationPredicate', 'AdvancementLocationPredicate'),
    },
    'vanilla_mcdoc.data.advancement.trigger.PlacedBlockConditions': {
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
        'LocationPredicate': ('vanilla_mcdoc.data.advancement.predicate.LocationPredicate', 'LocationPredicate'),
    },
    'vanilla_mcdoc.data.advancement.trigger.PlayerConditions': {
        'AdvancementEntityPredicate': ('vanilla_mcdoc.data.advancement.trigger.AdvancementEntityPredicate', 'AdvancementEntityPredicate'),
    },
    'vanilla_mcdoc.data.block_sound_set.BlockSoundSet': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.block_transformer.BlockTransformData': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'BlockTransformDropStrategy': ('vanilla_mcdoc.data.block_transformer.BlockTransformDropStrategy', 'BlockTransformDropStrategy'),
        'BlockTransformParticle': ('vanilla_mcdoc.data.block_transformer.BlockTransformParticle', 'BlockTransformParticle'),
        'BlockTransformType': ('vanilla_mcdoc.data.block_transformer.BlockTransformType', 'BlockTransformType'),
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.chat_type.ChatDecoration': {
        'ChatDecorationParameter': ('vanilla_mcdoc.data.chat_type.ChatDecorationParameter', 'ChatDecorationParameter'),
        'TextStyle': ('vanilla_mcdoc.util.text.TextStyle', 'TextStyle'),
    },
    'vanilla_mcdoc.data.chat_type.ChatType': {
        'ChatDecoration': ('vanilla_mcdoc.data.chat_type.ChatDecoration', 'ChatDecoration'),
    },
    'vanilla_mcdoc.data.chat_type.Narration': {
        'ChatDecoration': ('vanilla_mcdoc.data.chat_type.ChatDecoration', 'ChatDecoration'),
        'NarrationPriority': ('vanilla_mcdoc.data.chat_type.NarrationPriority', 'NarrationPriority'),
    },
    'vanilla_mcdoc.data.chat_type.OldChatType': {
        'Narration': ('vanilla_mcdoc.data.chat_type.Narration', 'Narration'),
        'TextDisplay': ('vanilla_mcdoc.data.chat_type.TextDisplay', 'TextDisplay'),
    },
    'vanilla_mcdoc.data.chat_type.TextDisplay': {
        'ChatDecoration': ('vanilla_mcdoc.data.chat_type.ChatDecoration', 'ChatDecoration'),
    },
    'vanilla_mcdoc.data.damage_type.DamageType': {
        'DamageEffects': ('vanilla_mcdoc.data.damage_type.DamageEffects', 'DamageEffects'),
        'DamageScaling': ('vanilla_mcdoc.data.damage_type.DamageScaling', 'DamageScaling'),
        'DeathMessageType': ('vanilla_mcdoc.data.damage_type.DeathMessageType', 'DeathMessageType'),
    },
    'vanilla_mcdoc.data.dialog.Button': {
        'ClickAction': ('vanilla_mcdoc.data.dialog.action.ClickAction', 'ClickAction'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.ButtonListDialogBase': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'Button': ('vanilla_mcdoc.data.dialog.Button', 'Button'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.ConfirmationDialog': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'Button': ('vanilla_mcdoc.data.dialog.Button', 'Button'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.Dialog': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'Button': ('vanilla_mcdoc.data.dialog.Button', 'Button'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'DialogListRef': ('vanilla_mcdoc.data.dialog.DialogListRef', 'DialogListRef'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.DialogBase': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.DialogListRef': {
        'Dialog': ('vanilla_mcdoc.data.dialog.Dialog', 'Dialog'),
        'KnownDialogId': ('vanilla_mcdoc.registry.KnownDialogId', 'KnownDialogId'),
    },
    'vanilla_mcdoc.data.dialog.ListDialogBase': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'Button': ('vanilla_mcdoc.data.dialog.Button', 'Button'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.MultiActionDialog': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'Button': ('vanilla_mcdoc.data.dialog.Button', 'Button'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.NoticeDialog': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'Button': ('vanilla_mcdoc.data.dialog.Button', 'Button'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.RedirectDialog': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'Button': ('vanilla_mcdoc.data.dialog.Button', 'Button'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'DialogListRef': ('vanilla_mcdoc.data.dialog.DialogListRef', 'DialogListRef'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.ServerLinksDialog': {
        'AfterAction': ('vanilla_mcdoc.data.dialog.AfterAction', 'AfterAction'),
        'Button': ('vanilla_mcdoc.data.dialog.Button', 'Button'),
        'DialogBody': ('vanilla_mcdoc.data.dialog.body.DialogBody', 'DialogBody'),
        'InputControl': ('vanilla_mcdoc.data.dialog.input.InputControl', 'InputControl'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.action.DynamicCustomAction': {
        'UnknownDynamicAdditions': ('vanilla_mcdoc.util.custom_event.UnknownDynamicAdditions', 'UnknownDynamicAdditions'),
    },
    'vanilla_mcdoc.data.dialog.body.ItemBody': {
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
        'PlainMessage': ('vanilla_mcdoc.data.dialog.body.PlainMessage', 'PlainMessage'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.body.PlainMessage': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.input.BooleanInput': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.input.NumberRangeInput': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.input.Option': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.input.SingleOptionInput': {
        'Option': ('vanilla_mcdoc.data.dialog.input.Option', 'Option'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.dialog.input.TextInput': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.enchantment.Enchantment': {
        'EnchantmentCost': ('vanilla_mcdoc.data.enchantment.EnchantmentCost', 'EnchantmentCost'),
        'EnchantmentEffectComponentMap': ('vanilla_mcdoc.data.enchantment.effect_component.EnchantmentEffectComponentMap', 'EnchantmentEffectComponentMap'),
        'EquipmentSlotGroup': ('vanilla_mcdoc.util.slot.EquipmentSlotGroup', 'EquipmentSlotGroup'),
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.enchantment.effect.AddEffectValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.AllOfEffectValue': {
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect.AllOfEntityEffect': {
        'EntityEffect': ('vanilla_mcdoc.data.enchantment.effect.EntityEffect', 'EntityEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect.AllOfLocationBasedEffect': {
        'LocationBasedEffect': ('vanilla_mcdoc.data.enchantment.effect.LocationBasedEffect', 'LocationBasedEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ApplyExhaustionEntityEffect': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ApplyImpulseEntityEffect': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ApplyMobEffectEntityEffect': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.AttributeEffect': {
        'AttributeOperation': ('vanilla_mcdoc.util.attribute.AttributeOperation', 'AttributeOperation'),
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ChangeItemDamageEffect': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.DamageEntityEffect': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.DamageItemEffect': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ExplodeEntityEffect': {
        'BlockInteraction': ('vanilla_mcdoc.data.enchantment.effect.BlockInteraction', 'BlockInteraction'),
        'ExplosionParticleInfo': ('vanilla_mcdoc.data.enchantment.effect.ExplosionParticleInfo', 'ExplosionParticleInfo'),
        'FlatWeightedList': ('vanilla_mcdoc.util.FlatWeightedList', 'FlatWeightedList'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ExplosionParticleInfo': {
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ExponentialEffectValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.IgniteEntityEffect': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.MultiplyEffectValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.PlaySoundEntityEffect': {
        'FloatProvider': ('vanilla_mcdoc.data.worldgen.FloatProvider', 'FloatProvider'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ReduceBinomialEffectValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ReplaceBlockEntityEffect': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.enchantment.effect.ReplaceDiskEntityEffect': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.SetEffectValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.effect.SpawnParticlesEntityEffect': {
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
        'ParticlePosition': ('vanilla_mcdoc.data.enchantment.effect.ParticlePosition', 'ParticlePosition'),
        'ParticleVelocity': ('vanilla_mcdoc.data.enchantment.effect.ParticleVelocity', 'ParticleVelocity'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.AmmoUseEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.ArmorEffectivenessEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.BlockExperienceEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.CrossbowChargeSoundsEnchantmentEffect': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.DamageEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.DamageImmunityEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.DamageProtectionEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.EnchantmentEffectComponentMap': {
        'AmmoUseEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.AmmoUseEnchantmentEffect', 'AmmoUseEnchantmentEffect'),
        'ArmorEffectivenessEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.ArmorEffectivenessEnchantmentEffect', 'ArmorEffectivenessEnchantmentEffect'),
        'AttributeEffect': ('vanilla_mcdoc.data.enchantment.effect.AttributeEffect', 'AttributeEffect'),
        'BlockExperienceEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.BlockExperienceEnchantmentEffect', 'BlockExperienceEnchantmentEffect'),
        'CrossbowChargeSoundsEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.CrossbowChargeSoundsEnchantmentEffect', 'CrossbowChargeSoundsEnchantmentEffect'),
        'DamageEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.DamageEnchantmentEffect', 'DamageEnchantmentEffect'),
        'DamageImmunityEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.DamageImmunityEnchantmentEffect', 'DamageImmunityEnchantmentEffect'),
        'DamageProtectionEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.DamageProtectionEnchantmentEffect', 'DamageProtectionEnchantmentEffect'),
        'EquipmentDropsEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.EquipmentDropsEnchantmentEffect', 'EquipmentDropsEnchantmentEffect'),
        'FishingLuckBonusEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.FishingLuckBonusEnchantmentEffect', 'FishingLuckBonusEnchantmentEffect'),
        'FishingTimeReductionEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.FishingTimeReductionEnchantmentEffect', 'FishingTimeReductionEnchantmentEffect'),
        'HitBlockEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.HitBlockEnchantmentEffect', 'HitBlockEnchantmentEffect'),
        'ItemDamageEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.ItemDamageEnchantmentEffect', 'ItemDamageEnchantmentEffect'),
        'KnockbackEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.KnockbackEnchantmentEffect', 'KnockbackEnchantmentEffect'),
        'LocationChangedEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.LocationChangedEnchantmentEffect', 'LocationChangedEnchantmentEffect'),
        'MobExperienceEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.MobExperienceEnchantmentEffect', 'MobExperienceEnchantmentEffect'),
        'PostAttackEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.PostAttackEnchantmentEffect', 'PostAttackEnchantmentEffect'),
        'PostPiercingAttackEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.PostPiercingAttackEnchantmentEffect', 'PostPiercingAttackEnchantmentEffect'),
        'ProjectileCountEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.ProjectileCountEnchantmentEffect', 'ProjectileCountEnchantmentEffect'),
        'ProjectilePiercingEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.ProjectilePiercingEnchantmentEffect', 'ProjectilePiercingEnchantmentEffect'),
        'ProjectileSpawnedEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.ProjectileSpawnedEnchantmentEffect', 'ProjectileSpawnedEnchantmentEffect'),
        'ProjectileSpreadEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.ProjectileSpreadEnchantmentEffect', 'ProjectileSpreadEnchantmentEffect'),
        'RepairWithXpEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.RepairWithXpEnchantmentEffect', 'RepairWithXpEnchantmentEffect'),
        'SmashDamagePerBlockFallenEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.SmashDamagePerBlockFallenEnchantmentEffect', 'SmashDamagePerBlockFallenEnchantmentEffect'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
        'TickEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.TickEnchantmentEffect', 'TickEnchantmentEffect'),
        'TridentReturnAccelerationEnchantmentEffect': ('vanilla_mcdoc.data.enchantment.effect_component.TridentReturnAccelerationEnchantmentEffect', 'TridentReturnAccelerationEnchantmentEffect'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.EquipmentDropsEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.FishingLuckBonusEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.FishingTimeReductionEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.HitBlockEnchantmentEffect': {
        'EntityEffect': ('vanilla_mcdoc.data.enchantment.effect.EntityEffect', 'EntityEffect'),
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.ItemDamageEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.KnockbackEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.LocationChangedEnchantmentEffect': {
        'LocationBasedEffect': ('vanilla_mcdoc.data.enchantment.effect.LocationBasedEffect', 'LocationBasedEffect'),
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.MobExperienceEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.PostAttackEnchantmentEffect': {
        'AttackTarget': ('vanilla_mcdoc.data.enchantment.effect_component.AttackTarget', 'AttackTarget'),
        'EntityEffect': ('vanilla_mcdoc.data.enchantment.effect.EntityEffect', 'EntityEffect'),
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.PostPiercingAttackEnchantmentEffect': {
        'EntityEffect': ('vanilla_mcdoc.data.enchantment.effect.EntityEffect', 'EntityEffect'),
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.ProjectileCountEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.ProjectilePiercingEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.ProjectileSpawnedEnchantmentEffect': {
        'EntityEffect': ('vanilla_mcdoc.data.enchantment.effect.EntityEffect', 'EntityEffect'),
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.ProjectileSpreadEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.RepairWithXpEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.SmashDamagePerBlockFallenEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.TickEnchantmentEffect': {
        'EntityEffect': ('vanilla_mcdoc.data.enchantment.effect.EntityEffect', 'EntityEffect'),
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
    },
    'vanilla_mcdoc.data.enchantment.effect_component.TridentReturnAccelerationEnchantmentEffect': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'ValueEffect': ('vanilla_mcdoc.data.enchantment.effect.ValueEffect', 'ValueEffect'),
    },
    'vanilla_mcdoc.data.enchantment.level_based_value.ClampedLevelValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.level_based_value.ExponentLevelValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.level_based_value.FractionLevelValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValue': {
        'LevelBasedValueMap': ('vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValueMap', 'LevelBasedValueMap'),
    },
    'vanilla_mcdoc.data.enchantment.level_based_value.LookupLevelValue': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.level_based_value.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.enchantment.provider.ByCostEnchantmentProvider': {
        'EnchantmentsType': ('vanilla_mcdoc.data.enchantment.provider.EnchantmentsType', 'EnchantmentsType'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.enchantment.provider.ByCostWithDifficultyEnchantmentProvider': {
        'EnchantmentsType': ('vanilla_mcdoc.data.enchantment.provider.EnchantmentsType', 'EnchantmentsType'),
    },
    'vanilla_mcdoc.data.enchantment.provider.SingleProvider': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.gametest.TestData': {
        'Rotation': ('vanilla_mcdoc.util.Rotation', 'Rotation'),
        'TestEnvironment': ('vanilla_mcdoc.data.gametest.test_environment.TestEnvironment', 'TestEnvironment'),
    },
    'vanilla_mcdoc.data.gametest.test_environment.AllOffTestEnvironment': {
        'TestEnvironment': ('vanilla_mcdoc.data.gametest.test_environment.TestEnvironment', 'TestEnvironment'),
    },
    'vanilla_mcdoc.data.gametest.test_environment.DifficultyTestEnvironment': {
        'Difficulty': ('vanilla_mcdoc.data.gametest.test_environment.Difficulty', 'Difficulty'),
    },
    'vanilla_mcdoc.data.gametest.test_environment.GameRuleMap': {
        'KnownGameRuleId': ('vanilla_mcdoc.registry.KnownGameRuleId', 'KnownGameRuleId'),
    },
    'vanilla_mcdoc.data.gametest.test_environment.GameRulesTestEnvironment': {
        'KnownGameRuleId': ('vanilla_mcdoc.registry.KnownGameRuleId', 'KnownGameRuleId'),
    },
    'vanilla_mcdoc.data.gametest.test_environment.WeatherTestEnvironment': {
        'Weather': ('vanilla_mcdoc.data.gametest.test_environment.Weather', 'Weather'),
    },
    'vanilla_mcdoc.data.item_modifier.ItemModifier': {
        'LootFunction': ('vanilla_mcdoc.data.loot.LootFunction', 'LootFunction'),
    },
    'vanilla_mcdoc.data.item_modifier.ItemModifierWithoutRootRef': {
        'LootFunction': ('vanilla_mcdoc.data.loot.LootFunction', 'LootFunction'),
    },
    'vanilla_mcdoc.data.loot.CompositePoolEntry': {
        'LootPoolEntry': ('vanilla_mcdoc.data.loot.LootPoolEntry', 'LootPoolEntry'),
    },
    'vanilla_mcdoc.data.loot.DynamicPoolEntry': {
        'DynamicDrops': ('vanilla_mcdoc.data.loot.DynamicDrops', 'DynamicDrops'),
    },
    'vanilla_mcdoc.data.loot.FloatRange': {
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.IntRange': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.LootPool': {
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
        'ItemModifier': ('vanilla_mcdoc.data.item_modifier.ItemModifier', 'ItemModifier'),
        'LootPoolEntry': ('vanilla_mcdoc.data.loot.LootPoolEntry', 'LootPoolEntry'),
        'PredicateRef': ('vanilla_mcdoc.data.predicate.PredicateRef', 'PredicateRef'),
    },
    'vanilla_mcdoc.data.loot.LootPoolEntryBase': {
        'ItemModifier': ('vanilla_mcdoc.data.item_modifier.ItemModifier', 'ItemModifier'),
        'PredicateRef': ('vanilla_mcdoc.data.predicate.PredicateRef', 'PredicateRef'),
    },
    'vanilla_mcdoc.data.loot.LootTable': {
        'ItemModifier': ('vanilla_mcdoc.data.item_modifier.ItemModifier', 'ItemModifier'),
        'LootContextParamSets': ('vanilla_mcdoc.data.loot.LootContextParamSets', 'LootContextParamSets'),
        'LootPool': ('vanilla_mcdoc.data.loot.LootPool', 'LootPool'),
    },
    'vanilla_mcdoc.data.loot.LootTableListRef': {
        'LootTable': ('vanilla_mcdoc.data.loot.LootTable', 'LootTable'),
    },
    'vanilla_mcdoc.data.loot.LootTablePoolEntry': {
        'LootTableListRef': ('vanilla_mcdoc.data.loot.LootTableListRef', 'LootTableListRef'),
    },
    'vanilla_mcdoc.data.loot.LootTableRef': {
        'LootTable': ('vanilla_mcdoc.data.loot.LootTable', 'LootTable'),
    },
    'vanilla_mcdoc.data.loot.SlotsPoolEntry': {
        'SlotSource': ('vanilla_mcdoc.data.slot_source.SlotSource', 'SlotSource'),
    },
    'vanilla_mcdoc.data.loot.TagPoolEntry': {
        'ItemListRef': ('vanilla_mcdoc.util.registry_ref.ItemListRef', 'ItemListRef'),
    },
    'vanilla_mcdoc.data.loot.condition.AllOf': {
        'PredicateListRef': ('vanilla_mcdoc.data.predicate.PredicateListRef', 'PredicateListRef'),
    },
    'vanilla_mcdoc.data.loot.condition.Alternative': {
        'LootCondition': ('vanilla_mcdoc.data.loot.condition.LootCondition', 'LootCondition'),
    },
    'vanilla_mcdoc.data.loot.condition.AnyOf': {
        'PredicateListRef': ('vanilla_mcdoc.data.predicate.PredicateListRef', 'PredicateListRef'),
    },
    'vanilla_mcdoc.data.loot.condition.BlockStateProperty': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.loot.condition.DamageSourceProperties': {
        'DamageSourcePredicate': ('vanilla_mcdoc.data.advancement.predicate.DamageSourcePredicate', 'DamageSourcePredicate'),
    },
    'vanilla_mcdoc.data.loot.condition.EntityProperties': {
        'EntityPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityPredicate', 'EntityPredicate'),
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
    },
    'vanilla_mcdoc.data.loot.condition.EntityScores': {
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
        'IntRange': ('vanilla_mcdoc.data.loot.IntRange', 'IntRange'),
    },
    'vanilla_mcdoc.data.loot.condition.EnvironmentAttributeCheck': {
        'AmbientParticle': ('vanilla_mcdoc.data.worldgen.attribute.AmbientParticle', 'AmbientParticle'),
        'AmbientSounds': ('vanilla_mcdoc.data.worldgen.attribute.AmbientSounds', 'AmbientSounds'),
        'BackgroundMusic': ('vanilla_mcdoc.data.worldgen.attribute.BackgroundMusic', 'BackgroundMusic'),
        'BedRule': ('vanilla_mcdoc.data.worldgen.attribute.BedRule', 'BedRule'),
        'KnownEnvironmentAttributeId': ('vanilla_mcdoc.registry.KnownEnvironmentAttributeId', 'KnownEnvironmentAttributeId'),
        'MoonPhase': ('vanilla_mcdoc.data.util.MoonPhase', 'MoonPhase'),
        'NaturalMobSpawns': ('vanilla_mcdoc.data.worldgen.biome.NaturalMobSpawns', 'NaturalMobSpawns'),
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
        'StringARGB': ('vanilla_mcdoc.util.color.StringARGB', 'StringARGB'),
        'StringRGB': ('vanilla_mcdoc.util.color.StringRGB', 'StringRGB'),
        'TriState': ('vanilla_mcdoc.data.worldgen.attribute.TriState', 'TriState'),
    },
    'vanilla_mcdoc.data.loot.condition.FloatValueCheck': {
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
        'FloatRange': ('vanilla_mcdoc.data.loot.FloatRange', 'FloatRange'),
    },
    'vanilla_mcdoc.data.loot.condition.IntegerValueCheck': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
        'IntRange': ('vanilla_mcdoc.data.loot.IntRange', 'IntRange'),
    },
    'vanilla_mcdoc.data.loot.condition.Inverted': {
        'PredicateRef': ('vanilla_mcdoc.data.predicate.PredicateRef', 'PredicateRef'),
    },
    'vanilla_mcdoc.data.loot.condition.LocationCheck': {
        'LocationPredicate': ('vanilla_mcdoc.data.advancement.predicate.LocationPredicate', 'LocationPredicate'),
    },
    'vanilla_mcdoc.data.loot.condition.MatchTool': {
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
    },
    'vanilla_mcdoc.data.loot.condition.RandomChance': {
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.condition.RandomChanceWithEnchantedBonus': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.loot.condition.TimeCheck': {
        'IntRange': ('vanilla_mcdoc.data.loot.IntRange', 'IntRange'),
    },
    'vanilla_mcdoc.data.loot.condition.ValueCheck': {
        'IntRange': ('vanilla_mcdoc.data.loot.IntRange', 'IntRange'),
        'LegacyNumberProvider': ('vanilla_mcdoc.data.number_provider.LegacyNumberProvider', 'LegacyNumberProvider'),
    },
    'vanilla_mcdoc.data.loot.function.AttributeModifier': {
        'AttributeOperation': ('vanilla_mcdoc.util.attribute.AttributeOperation', 'AttributeOperation'),
        'EquipmentSlotGroup': ('vanilla_mcdoc.util.slot.EquipmentSlotGroup', 'EquipmentSlotGroup'),
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.BannerPatternLayer': {
        'DyeColor': ('vanilla_mcdoc.util.color.DyeColor', 'DyeColor'),
    },
    'vanilla_mcdoc.data.loot.function.Conditions': {
        'PredicateRef': ('vanilla_mcdoc.data.predicate.PredicateRef', 'PredicateRef'),
    },
    'vanilla_mcdoc.data.loot.function.CopyComponents': {
        'BlockEntityTarget': ('vanilla_mcdoc.data.loot.BlockEntityTarget', 'BlockEntityTarget'),
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
        'ItemStackTarget': ('vanilla_mcdoc.data.loot.ItemStackTarget', 'ItemStackTarget'),
    },
    'vanilla_mcdoc.data.loot.function.CopyName': {
        'BlockEntityTarget': ('vanilla_mcdoc.data.loot.BlockEntityTarget', 'BlockEntityTarget'),
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
    },
    'vanilla_mcdoc.data.loot.function.CopyNbt': {
        'CopyNbtStrategy': ('vanilla_mcdoc.data.loot.function.CopyNbtStrategy', 'CopyNbtStrategy'),
        'NbtProvider': ('vanilla_mcdoc.data.util.NbtProvider', 'NbtProvider'),
    },
    'vanilla_mcdoc.data.loot.function.CopyNbtOperation': {
        'CopyNbtStrategy': ('vanilla_mcdoc.data.loot.function.CopyNbtStrategy', 'CopyNbtStrategy'),
    },
    'vanilla_mcdoc.data.loot.function.CopyState': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.loot.function.CustomModelDataColors': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.data.loot.function.CustomModelDataFloats': {
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.EnchantWithLevels': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.EnchantedCountBase': {
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.FillPlayerHead': {
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
    },
    'vanilla_mcdoc.data.loot.function.Filtered': {
        'ItemModifier': ('vanilla_mcdoc.data.item_modifier.ItemModifier', 'ItemModifier'),
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
    },
    'vanilla_mcdoc.data.loot.function.FireworkExplosions': {
        'Explosion': ('vanilla_mcdoc.world.component.item.Explosion', 'Explosion'),
    },
    'vanilla_mcdoc.data.loot.function.LimitCount': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.LootFunction': {
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
        'Filterable': ('vanilla_mcdoc.util.Filterable', 'Filterable'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.loot.function.ModifyContents': {
        'ContainerComponents': ('vanilla_mcdoc.data.loot.function.ContainerComponents', 'ContainerComponents'),
        'ItemModifier': ('vanilla_mcdoc.data.item_modifier.ItemModifier', 'ItemModifier'),
    },
    'vanilla_mcdoc.data.loot.function.Sequence': {
        'ItemModifier': ('vanilla_mcdoc.data.item_modifier.ItemModifier', 'ItemModifier'),
    },
    'vanilla_mcdoc.data.loot.function.SetAttributes': {
        'AttributeModifier': ('vanilla_mcdoc.data.loot.function.AttributeModifier', 'AttributeModifier'),
    },
    'vanilla_mcdoc.data.loot.function.SetBannerPattern': {
        'BannerPatternLayer': ('vanilla_mcdoc.data.loot.function.BannerPatternLayer', 'BannerPatternLayer'),
    },
    'vanilla_mcdoc.data.loot.function.SetBookCover': {
        'Filterable': ('vanilla_mcdoc.util.Filterable', 'Filterable'),
    },
    'vanilla_mcdoc.data.loot.function.SetComponents': {
        'DataComponentPatch': ('vanilla_mcdoc.world.component.DataComponentPatch', 'DataComponentPatch'),
    },
    'vanilla_mcdoc.data.loot.function.SetContents': {
        'ContainerComponents': ('vanilla_mcdoc.data.loot.function.ContainerComponents', 'ContainerComponents'),
        'LootPoolEntry': ('vanilla_mcdoc.data.loot.LootPoolEntry', 'LootPoolEntry'),
    },
    'vanilla_mcdoc.data.loot.function.SetCount': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.SetCustomData': {
        'CustomData': ('vanilla_mcdoc.world.component.CustomData', 'CustomData'),
    },
    'vanilla_mcdoc.data.loot.function.SetCustomModelData': {
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.data.loot.function.SetDamage': {
        'FloatNumberProviderRef': ('vanilla_mcdoc.data.number_provider.FloatNumberProviderRef', 'FloatNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.SetEnchantments': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.SetFireworkExplosion': {
        'FireworkShape': ('vanilla_mcdoc.world.component.item.FireworkShape', 'FireworkShape'),
    },
    'vanilla_mcdoc.data.loot.function.SetFireworks': {
        'Explosion': ('vanilla_mcdoc.world.component.item.Explosion', 'Explosion'),
    },
    'vanilla_mcdoc.data.loot.function.SetLore': {
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.loot.function.SetName': {
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
        'SetNameTarget': ('vanilla_mcdoc.data.loot.function.SetNameTarget', 'SetNameTarget'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.loot.function.SetOminousBottleAmplifier': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.SetRandomDyes': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
    },
    'vanilla_mcdoc.data.loot.function.SetStewEffect': {
        'StewEffect': ('vanilla_mcdoc.data.loot.function.StewEffect', 'StewEffect'),
    },
    'vanilla_mcdoc.data.loot.function.SetWriteableBookPages': {
        'Filterable': ('vanilla_mcdoc.util.Filterable', 'Filterable'),
    },
    'vanilla_mcdoc.data.loot.function.SetWrittenBookPages': {
        'Filterable': ('vanilla_mcdoc.util.Filterable', 'Filterable'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.loot.function.StewEffect': {
        'IntNumberProviderRef': ('vanilla_mcdoc.data.number_provider.IntNumberProviderRef', 'IntNumberProviderRef'),
    },
    'vanilla_mcdoc.data.number_provider.ConditionalProvider': {
        'PredicateRef': ('vanilla_mcdoc.data.predicate.PredicateRef', 'PredicateRef'),
    },
    'vanilla_mcdoc.data.number_provider.DispatcherProvider': {
        'PredicateRef': ('vanilla_mcdoc.data.predicate.PredicateRef', 'PredicateRef'),
    },
    'vanilla_mcdoc.data.number_provider.DistributionProvider': {
        'NonEmptyWeightedList': ('vanilla_mcdoc.util.NonEmptyWeightedList', 'NonEmptyWeightedList'),
    },
    'vanilla_mcdoc.data.number_provider.context_float.AggregateOperands': {
        'ContextFloatProvider': ('vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider', 'ContextFloatProvider'),
        'FloatRef': ('vanilla_mcdoc.data.number_provider.context_float.FloatRef', 'FloatRef'),
        'KnownContextFloatProviderId': ('vanilla_mcdoc.registry.KnownContextFloatProviderId', 'KnownContextFloatProviderId'),
    },
    'vanilla_mcdoc.data.number_provider.context_float.AggregateProvider': {
        'AggregateOperands': ('vanilla_mcdoc.data.number_provider.context_float.AggregateOperands', 'AggregateOperands'),
    },
    'vanilla_mcdoc.data.number_provider.context_float.BinaryProvider': {
        'FloatRef': ('vanilla_mcdoc.data.number_provider.context_float.FloatRef', 'FloatRef'),
    },
    'vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider': {
        'FloatRef': ('vanilla_mcdoc.data.number_provider.context_float.FloatRef', 'FloatRef'),
        'IntRef': ('vanilla_mcdoc.data.number_provider.context_int.IntRef', 'IntRef'),
        'NonEmptyWeightedList': ('vanilla_mcdoc.util.NonEmptyWeightedList', 'NonEmptyWeightedList'),
        'NumericalEnvironmentAttribute': ('vanilla_mcdoc.data.worldgen.attribute.NumericalEnvironmentAttribute', 'NumericalEnvironmentAttribute'),
        'PredicateRef': ('vanilla_mcdoc.data.predicate.PredicateRef', 'PredicateRef'),
    },
    'vanilla_mcdoc.data.number_provider.context_float.EnchantmentLevelProvider': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.number_provider.context_float.FloatRef': {
        'ContextFloatProvider': ('vanilla_mcdoc.data.number_provider.context_float.ContextFloatProvider', 'ContextFloatProvider'),
        'KnownContextFloatProviderId': ('vanilla_mcdoc.registry.KnownContextFloatProviderId', 'KnownContextFloatProviderId'),
    },
    'vanilla_mcdoc.data.number_provider.context_float.SingleProvider': {
        'FloatRef': ('vanilla_mcdoc.data.number_provider.context_float.FloatRef', 'FloatRef'),
    },
    'vanilla_mcdoc.data.number_provider.context_int.AggregateOperands': {
        'ContextIntProvider': ('vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider', 'ContextIntProvider'),
        'IntRef': ('vanilla_mcdoc.data.number_provider.context_int.IntRef', 'IntRef'),
        'KnownContextIntProviderId': ('vanilla_mcdoc.registry.KnownContextIntProviderId', 'KnownContextIntProviderId'),
    },
    'vanilla_mcdoc.data.number_provider.context_int.AggregateProvider': {
        'AggregateOperands': ('vanilla_mcdoc.data.number_provider.context_int.AggregateOperands', 'AggregateOperands'),
    },
    'vanilla_mcdoc.data.number_provider.context_int.BinaryProvider': {
        'IntRef': ('vanilla_mcdoc.data.number_provider.context_int.IntRef', 'IntRef'),
    },
    'vanilla_mcdoc.data.number_provider.context_int.BinomialDistributionGenerator': {
        'FloatRef': ('vanilla_mcdoc.data.number_provider.context_float.FloatRef', 'FloatRef'),
        'IntRef': ('vanilla_mcdoc.data.number_provider.context_int.IntRef', 'IntRef'),
    },
    'vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider': {
        'FloatRef': ('vanilla_mcdoc.data.number_provider.context_float.FloatRef', 'FloatRef'),
        'IntRef': ('vanilla_mcdoc.data.number_provider.context_int.IntRef', 'IntRef'),
        'IntegerEnvironmentAttribute': ('vanilla_mcdoc.data.worldgen.attribute.IntegerEnvironmentAttribute', 'IntegerEnvironmentAttribute'),
        'NonEmptyWeightedList': ('vanilla_mcdoc.util.NonEmptyWeightedList', 'NonEmptyWeightedList'),
        'PredicateRef': ('vanilla_mcdoc.data.predicate.PredicateRef', 'PredicateRef'),
    },
    'vanilla_mcdoc.data.number_provider.context_int.IntRef': {
        'ContextIntProvider': ('vanilla_mcdoc.data.number_provider.context_int.ContextIntProvider', 'ContextIntProvider'),
        'KnownContextIntProviderId': ('vanilla_mcdoc.registry.KnownContextIntProviderId', 'KnownContextIntProviderId'),
    },
    'vanilla_mcdoc.data.number_provider.context_int.ScoreboardValue': {
        'IntRef': ('vanilla_mcdoc.data.number_provider.context_int.IntRef', 'IntRef'),
        'ScoreProvider': ('vanilla_mcdoc.data.util.ScoreProvider', 'ScoreProvider'),
    },
    'vanilla_mcdoc.data.number_provider.context_int.SingleProvider': {
        'IntRef': ('vanilla_mcdoc.data.number_provider.context_int.IntRef', 'IntRef'),
    },
    'vanilla_mcdoc.data.number_provider.legacy.BinomialNumberProvider': {
        'LegacyNumberProvider': ('vanilla_mcdoc.data.number_provider.legacy.LegacyNumberProvider', 'LegacyNumberProvider'),
    },
    'vanilla_mcdoc.data.number_provider.legacy.EnchantmentLevelProvider': {
        'LevelBasedValue': ('vanilla_mcdoc.data.enchantment.LevelBasedValue', 'LevelBasedValue'),
    },
    'vanilla_mcdoc.data.number_provider.legacy.EnvironmentAttributeNumberProvider': {
        'NumericalEnvironmentAttribute': ('vanilla_mcdoc.data.worldgen.attribute.NumericalEnvironmentAttribute', 'NumericalEnvironmentAttribute'),
    },
    'vanilla_mcdoc.data.number_provider.legacy.ScoreNumberProvider': {
        'ScoreProvider': ('vanilla_mcdoc.data.util.ScoreProvider', 'ScoreProvider'),
    },
    'vanilla_mcdoc.data.number_provider.legacy.SumNumberProvider': {
        'LegacyNumberProvider': ('vanilla_mcdoc.data.number_provider.legacy.LegacyNumberProvider', 'LegacyNumberProvider'),
    },
    'vanilla_mcdoc.data.number_provider.legacy.UniformNumberProvider': {
        'LegacyNumberProvider': ('vanilla_mcdoc.data.number_provider.legacy.LegacyNumberProvider', 'LegacyNumberProvider'),
    },
    'vanilla_mcdoc.data.predicate.PredicateListRef': {
        'LootCondition': ('vanilla_mcdoc.data.loot.LootCondition', 'LootCondition'),
    },
    'vanilla_mcdoc.data.predicate.PredicateRef': {
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
    },
    'vanilla_mcdoc.data.recipe.Brewing': {
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
        'PotionIngredient': ('vanilla_mcdoc.data.recipe.PotionIngredient', 'PotionIngredient'),
    },
    'vanilla_mcdoc.data.recipe.CookingBookInfo': {
        'CookingBookCategory': ('vanilla_mcdoc.data.recipe.CookingBookCategory', 'CookingBookCategory'),
    },
    'vanilla_mcdoc.data.recipe.CraftingBookInfo': {
        'CraftingBookCategory': ('vanilla_mcdoc.data.recipe.CraftingBookCategory', 'CraftingBookCategory'),
    },
    'vanilla_mcdoc.data.recipe.CraftingDecoratedPot': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingDye': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingImbue': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingIngredients': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
    },
    'vanilla_mcdoc.data.recipe.CraftingShaped': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingShapeless': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingSpecialBannerDuplicate': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingSpecialBookCloning': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.recipe.CraftingSpecialFireworkRocket': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingSpecialFireworkStar': {
        'FireworkShape': ('vanilla_mcdoc.world.component.item.FireworkShape', 'FireworkShape'),
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingSpecialFireworkStarFade': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingSpecialMapExtending': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingSpecialShieldDecoration': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.CraftingTransmute': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.recipe.FireworkShapeIngredients': {
        'FireworkShape': ('vanilla_mcdoc.world.component.item.FireworkShape', 'FireworkShape'),
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
    },
    'vanilla_mcdoc.data.recipe.IngredientItem': {
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.data.recipe.IngredientTag': {
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.data.recipe.IngredientValue': {
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.data.recipe.ItemResult': {
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.data.recipe.OptionalSmithingIngredients': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
    },
    'vanilla_mcdoc.data.recipe.PotionIngredient': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'PotionsPredicate': ('vanilla_mcdoc.world.component.predicate.PotionsPredicate', 'PotionsPredicate'),
    },
    'vanilla_mcdoc.data.recipe.Recipe': {
        'KnownRecipeSerializerId': ('vanilla_mcdoc.registry.KnownRecipeSerializerId', 'KnownRecipeSerializerId'),
    },
    'vanilla_mcdoc.data.recipe.RequiredSmithingIngredients': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
    },
    'vanilla_mcdoc.data.recipe.Smelting': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.Smithing': {
        'IngredientValue': ('vanilla_mcdoc.data.recipe.IngredientValue', 'IngredientValue'),
        'ItemResult': ('vanilla_mcdoc.data.recipe.ItemResult', 'ItemResult'),
    },
    'vanilla_mcdoc.data.recipe.SmithingIngredients': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
    },
    'vanilla_mcdoc.data.recipe.SmithingTransform': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.recipe.SmithingTransformResult': {
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.data.recipe.SmithingTrim': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
    },
    'vanilla_mcdoc.data.recipe.Stonecutting': {
        'Ingredient': ('vanilla_mcdoc.data.recipe.Ingredient', 'Ingredient'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.data.slot_source.ContentsSlotSource': {
        'ContainerComponents': ('vanilla_mcdoc.data.loot.function.ContainerComponents', 'ContainerComponents'),
        'SlotSource': ('vanilla_mcdoc.data.slot_source.SlotSource', 'SlotSource'),
    },
    'vanilla_mcdoc.data.slot_source.FilterSlotSource': {
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
        'SlotSource': ('vanilla_mcdoc.data.slot_source.SlotSource', 'SlotSource'),
    },
    'vanilla_mcdoc.data.slot_source.GroupSlotSource': {
        'SlotSource': ('vanilla_mcdoc.data.slot_source.SlotSource', 'SlotSource'),
    },
    'vanilla_mcdoc.data.slot_source.LimitCountSlotSource': {
        'SlotSource': ('vanilla_mcdoc.data.slot_source.SlotSource', 'SlotSource'),
    },
    'vanilla_mcdoc.data.slot_source.RangeSlotSource': {
        'BlockEntityTarget': ('vanilla_mcdoc.data.loot.BlockEntityTarget', 'BlockEntityTarget'),
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
    },
    'vanilla_mcdoc.data.slot_source.SlotSource': {
        'KnownSlotSourceId': ('vanilla_mcdoc.registry.KnownSlotSourceId', 'KnownSlotSourceId'),
        'TypedSlotSource': ('vanilla_mcdoc.data.slot_source.TypedSlotSource', 'TypedSlotSource'),
    },
    'vanilla_mcdoc.data.structure.BlockPalette': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.structure.Palette': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.structure.RandomizedPalette': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.structure.StructureBlock': {
        'Banner': ('vanilla_mcdoc.world.block.banner.Banner', 'Banner'),
        'Beacon': ('vanilla_mcdoc.world.block.beacon.Beacon', 'Beacon'),
        'Beehive': ('vanilla_mcdoc.world.block.beehive.Beehive', 'Beehive'),
        'BlockEntity': ('vanilla_mcdoc.world.block.BlockEntity', 'BlockEntity'),
        'BrewingStand': ('vanilla_mcdoc.world.block.brewing_stand.BrewingStand', 'BrewingStand'),
        'BrushableBlock': ('vanilla_mcdoc.world.block.brushable_block.BrushableBlock', 'BrushableBlock'),
        'Campfire': ('vanilla_mcdoc.world.block.campfire.Campfire', 'Campfire'),
        'ChiseledBookshelf': ('vanilla_mcdoc.world.block.chiseled_bookshelf.ChiseledBookshelf', 'ChiseledBookshelf'),
        'CommandBlock': ('vanilla_mcdoc.world.block.command_block.CommandBlock', 'CommandBlock'),
        'Comparator': ('vanilla_mcdoc.world.block.comparator.Comparator', 'Comparator'),
        'Conduit': ('vanilla_mcdoc.world.block.conduit.Conduit', 'Conduit'),
        'Container27': ('vanilla_mcdoc.world.block.container.Container27', 'Container27'),
        'Container9': ('vanilla_mcdoc.world.block.container.Container9', 'Container9'),
        'Crafter': ('vanilla_mcdoc.world.block.crafter.Crafter', 'Crafter'),
        'DecoratedPot': ('vanilla_mcdoc.world.block.decorated_pot.DecoratedPot', 'DecoratedPot'),
        'EnchantingTable': ('vanilla_mcdoc.world.block.enchanting_table.EnchantingTable', 'EnchantingTable'),
        'EndGateway': ('vanilla_mcdoc.world.block.end_gateway.EndGateway', 'EndGateway'),
        'Furnace': ('vanilla_mcdoc.world.block.furnace.Furnace', 'Furnace'),
        'Hopper': ('vanilla_mcdoc.world.block.container.Hopper', 'Hopper'),
        'Jigsaw': ('vanilla_mcdoc.world.block.jigsaw.Jigsaw', 'Jigsaw'),
        'Jukebox': ('vanilla_mcdoc.world.block.jukebox.Jukebox', 'Jukebox'),
        'Lectern': ('vanilla_mcdoc.world.block.lectern.Lectern', 'Lectern'),
        'MovingPiston': ('vanilla_mcdoc.world.block.moving_piston.MovingPiston', 'MovingPiston'),
        'PotentSulfur': ('vanilla_mcdoc.world.block.potent_sulfur.PotentSulfur', 'PotentSulfur'),
        'SculkCatalyst': ('vanilla_mcdoc.world.block.sculk_catalyst.SculkCatalyst', 'SculkCatalyst'),
        'SculkSensor': ('vanilla_mcdoc.world.block.sculk_sensor.SculkSensor', 'SculkSensor'),
        'SculkShrieker': ('vanilla_mcdoc.world.block.sculk_shrieker.SculkShrieker', 'SculkShrieker'),
        'Shelf': ('vanilla_mcdoc.world.block.container.Shelf', 'Shelf'),
        'Sign': ('vanilla_mcdoc.world.block.sign.Sign', 'Sign'),
        'Skull': ('vanilla_mcdoc.world.block.head.Skull', 'Skull'),
        'Spawner': ('vanilla_mcdoc.world.block.spawner.Spawner', 'Spawner'),
        'StructureBlock2': ('vanilla_mcdoc.world.block.structure_block.StructureBlock', 'StructureBlock'),
        'TestBlock': ('vanilla_mcdoc.world.block.test_block.TestBlock', 'TestBlock'),
        'TestInstanceBlock': ('vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlock', 'TestInstanceBlock'),
        'TrialSpawner': ('vanilla_mcdoc.world.block.spawner.TrialSpawner', 'TrialSpawner'),
        'Vault': ('vanilla_mcdoc.world.block.vault.Vault', 'Vault'),
    },
    'vanilla_mcdoc.data.structure.StructureEntity': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
    },
    'vanilla_mcdoc.data.structure.StructureNBT': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
        'Banner': ('vanilla_mcdoc.world.block.banner.Banner', 'Banner'),
        'Beacon': ('vanilla_mcdoc.world.block.beacon.Beacon', 'Beacon'),
        'Beehive': ('vanilla_mcdoc.world.block.beehive.Beehive', 'Beehive'),
        'BlockEntity': ('vanilla_mcdoc.world.block.BlockEntity', 'BlockEntity'),
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'BrewingStand': ('vanilla_mcdoc.world.block.brewing_stand.BrewingStand', 'BrewingStand'),
        'BrushableBlock': ('vanilla_mcdoc.world.block.brushable_block.BrushableBlock', 'BrushableBlock'),
        'Campfire': ('vanilla_mcdoc.world.block.campfire.Campfire', 'Campfire'),
        'ChiseledBookshelf': ('vanilla_mcdoc.world.block.chiseled_bookshelf.ChiseledBookshelf', 'ChiseledBookshelf'),
        'CommandBlock': ('vanilla_mcdoc.world.block.command_block.CommandBlock', 'CommandBlock'),
        'Comparator': ('vanilla_mcdoc.world.block.comparator.Comparator', 'Comparator'),
        'Conduit': ('vanilla_mcdoc.world.block.conduit.Conduit', 'Conduit'),
        'Container27': ('vanilla_mcdoc.world.block.container.Container27', 'Container27'),
        'Container9': ('vanilla_mcdoc.world.block.container.Container9', 'Container9'),
        'Crafter': ('vanilla_mcdoc.world.block.crafter.Crafter', 'Crafter'),
        'DecoratedPot': ('vanilla_mcdoc.world.block.decorated_pot.DecoratedPot', 'DecoratedPot'),
        'EnchantingTable': ('vanilla_mcdoc.world.block.enchanting_table.EnchantingTable', 'EnchantingTable'),
        'EndGateway': ('vanilla_mcdoc.world.block.end_gateway.EndGateway', 'EndGateway'),
        'Furnace': ('vanilla_mcdoc.world.block.furnace.Furnace', 'Furnace'),
        'Hopper': ('vanilla_mcdoc.world.block.container.Hopper', 'Hopper'),
        'Jigsaw': ('vanilla_mcdoc.world.block.jigsaw.Jigsaw', 'Jigsaw'),
        'Jukebox': ('vanilla_mcdoc.world.block.jukebox.Jukebox', 'Jukebox'),
        'Lectern': ('vanilla_mcdoc.world.block.lectern.Lectern', 'Lectern'),
        'MovingPiston': ('vanilla_mcdoc.world.block.moving_piston.MovingPiston', 'MovingPiston'),
        'PotentSulfur': ('vanilla_mcdoc.world.block.potent_sulfur.PotentSulfur', 'PotentSulfur'),
        'SculkCatalyst': ('vanilla_mcdoc.world.block.sculk_catalyst.SculkCatalyst', 'SculkCatalyst'),
        'SculkSensor': ('vanilla_mcdoc.world.block.sculk_sensor.SculkSensor', 'SculkSensor'),
        'SculkShrieker': ('vanilla_mcdoc.world.block.sculk_shrieker.SculkShrieker', 'SculkShrieker'),
        'Shelf': ('vanilla_mcdoc.world.block.container.Shelf', 'Shelf'),
        'Sign': ('vanilla_mcdoc.world.block.sign.Sign', 'Sign'),
        'Skull': ('vanilla_mcdoc.world.block.head.Skull', 'Skull'),
        'Spawner': ('vanilla_mcdoc.world.block.spawner.Spawner', 'Spawner'),
        'StructureBlock': ('vanilla_mcdoc.world.block.structure_block.StructureBlock', 'StructureBlock'),
        'TestBlock': ('vanilla_mcdoc.world.block.test_block.TestBlock', 'TestBlock'),
        'TestInstanceBlock': ('vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlock', 'TestInstanceBlock'),
        'TrialSpawner': ('vanilla_mcdoc.world.block.spawner.TrialSpawner', 'TrialSpawner'),
        'Vault': ('vanilla_mcdoc.world.block.vault.Vault', 'Vault'),
    },
    'vanilla_mcdoc.data.sulfur_cube_archetype.ContactDamage': {
        'FloatProvider': ('vanilla_mcdoc.data.worldgen.FloatProvider', 'FloatProvider'),
    },
    'vanilla_mcdoc.data.sulfur_cube_archetype.SoundSettings': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.sulfur_cube_archetype.SulfurCubeArchetype': {
        'AttributeEntry': ('vanilla_mcdoc.data.sulfur_cube_archetype.AttributeEntry', 'AttributeEntry'),
        'ContactDamage': ('vanilla_mcdoc.data.sulfur_cube_archetype.ContactDamage', 'ContactDamage'),
        'ExplosionData': ('vanilla_mcdoc.data.sulfur_cube_archetype.ExplosionData', 'ExplosionData'),
        'KnockbackModifiers': ('vanilla_mcdoc.data.sulfur_cube_archetype.KnockbackModifiers', 'KnockbackModifiers'),
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
        'SoundSettings': ('vanilla_mcdoc.data.sulfur_cube_archetype.SoundSettings', 'SoundSettings'),
    },
    'vanilla_mcdoc.data.tag.Tag': {
        'TagEntry': ('vanilla_mcdoc.data.tag.TagEntry', 'TagEntry'),
    },
    'vanilla_mcdoc.data.timeline.AttributeTrackBase': {
        'EasingType': ('vanilla_mcdoc.data.timeline.EasingType', 'EasingType'),
    },
    'vanilla_mcdoc.data.timeline.EasingType': {
        'CubicBezierEase': ('vanilla_mcdoc.data.timeline.CubicBezierEase', 'CubicBezierEase'),
        'SimpleEasingType': ('vanilla_mcdoc.data.timeline.SimpleEasingType', 'SimpleEasingType'),
    },
    'vanilla_mcdoc.data.timeline.EnvironmentAttributeTrackMap': {
        'AmbientParticle': ('vanilla_mcdoc.data.worldgen.attribute.AmbientParticle', 'AmbientParticle'),
        'AmbientSounds': ('vanilla_mcdoc.data.worldgen.attribute.AmbientSounds', 'AmbientSounds'),
        'BackgroundMusic': ('vanilla_mcdoc.data.worldgen.attribute.BackgroundMusic', 'BackgroundMusic'),
        'BedRule': ('vanilla_mcdoc.data.worldgen.attribute.BedRule', 'BedRule'),
        'BlendToGray': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray', 'BlendToGray'),
        'BooleanModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanModifierType', 'BooleanModifierType'),
        'ColorModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType', 'ColorModifierType'),
        'FloatModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.FloatModifierType', 'FloatModifierType'),
        'FloatWithAlpha': ('vanilla_mcdoc.data.worldgen.attribute.modifier.FloatWithAlpha', 'FloatWithAlpha'),
        'KnownEnvironmentAttributeId': ('vanilla_mcdoc.registry.KnownEnvironmentAttributeId', 'KnownEnvironmentAttributeId'),
        'ListModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifierType', 'ListModifierType'),
        'MergeableModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifierType', 'MergeableModifierType'),
        'MoonPhase': ('vanilla_mcdoc.data.util.MoonPhase', 'MoonPhase'),
        'NaturalMobSpawns': ('vanilla_mcdoc.data.worldgen.biome.NaturalMobSpawns', 'NaturalMobSpawns'),
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
        'StringARGB': ('vanilla_mcdoc.util.color.StringARGB', 'StringARGB'),
        'StringRGB': ('vanilla_mcdoc.util.color.StringRGB', 'StringRGB'),
        'TriState': ('vanilla_mcdoc.data.worldgen.attribute.TriState', 'TriState'),
    },
    'vanilla_mcdoc.data.timeline.TimeMarkerMap': {
        'TimeMarker': ('vanilla_mcdoc.data.timeline.TimeMarker', 'TimeMarker'),
    },
    'vanilla_mcdoc.data.timeline.Timeline': {
        'EnvironmentAttributeTrackMap': ('vanilla_mcdoc.data.timeline.EnvironmentAttributeTrackMap', 'EnvironmentAttributeTrackMap'),
        'TimeMarkerMap': ('vanilla_mcdoc.data.timeline.TimeMarkerMap', 'TimeMarkerMap'),
    },
    'vanilla_mcdoc.data.trade_set.TradeSet': {
        'IntNumberProvider': ('vanilla_mcdoc.data.number_provider.IntNumberProvider', 'IntNumberProvider'),
    },
    'vanilla_mcdoc.data.trial_spawner.TrialSpawnerConfig': {
        'SpawnPotential': ('vanilla_mcdoc.world.block.spawner.SpawnPotential', 'SpawnPotential'),
        'WeightedList': ('vanilla_mcdoc.util.WeightedList', 'WeightedList'),
    },
    'vanilla_mcdoc.data.trim.OldTrimMaterialOverrides': {
        'ArmorMaterial': ('vanilla_mcdoc.data.trim.ArmorMaterial', 'ArmorMaterial'),
    },
    'vanilla_mcdoc.data.trim.TrimMaterial': {
        'PaletteRef': ('vanilla_mcdoc.assets.atlas.PaletteRef', 'PaletteRef'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.trim.TrimPattern': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.util.ContextNbtProvider': {
        'NbtContextTarget': ('vanilla_mcdoc.data.util.NbtContextTarget', 'NbtContextTarget'),
    },
    'vanilla_mcdoc.data.util.ContextScoreProvider': {
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
    },
    'vanilla_mcdoc.data.util.NbtContextTarget': {
        'BlockEntityTarget': ('vanilla_mcdoc.data.loot.BlockEntityTarget', 'BlockEntityTarget'),
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
    },
    'vanilla_mcdoc.data.util.NbtProvider': {
        'NbtContextTarget': ('vanilla_mcdoc.data.util.NbtContextTarget', 'NbtContextTarget'),
    },
    'vanilla_mcdoc.data.util.RandomIntGenerator': {
        'RandomIntGeneratorType': ('vanilla_mcdoc.data.util.RandomIntGeneratorType', 'RandomIntGeneratorType'),
    },
    'vanilla_mcdoc.data.util.ScoreProvider': {
        'EntityTarget': ('vanilla_mcdoc.data.loot.EntityTarget', 'EntityTarget'),
    },
    'vanilla_mcdoc.data.variants.MoonBrightnessCheck': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.data.variants.SpawnPrioritySelector': {
        'SpawnCondition': ('vanilla_mcdoc.data.variants.SpawnCondition', 'SpawnCondition'),
    },
    'vanilla_mcdoc.data.variants.SpawnPrioritySelectors': {
        'SpawnPrioritySelector': ('vanilla_mcdoc.data.variants.SpawnPrioritySelector', 'SpawnPrioritySelector'),
    },
    'vanilla_mcdoc.data.variants.cat.CatSounds': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.variants.chicken.ChickenSounds': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.variants.chicken.ChickenVariant': {
        'ChickenModelType': ('vanilla_mcdoc.data.variants.chicken.ChickenModelType', 'ChickenModelType'),
    },
    'vanilla_mcdoc.data.variants.cow.CowSounds': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.variants.cow.CowVariant': {
        'CowModelType': ('vanilla_mcdoc.data.variants.cow.CowModelType', 'CowModelType'),
    },
    'vanilla_mcdoc.data.variants.instrument.Instrument': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.variants.jukebox_song.JukeboxSong': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.variants.painting.PaintingVariant': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.variants.pig.PigSounds': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.variants.pig.PigVariant': {
        'PigModelType': ('vanilla_mcdoc.data.variants.pig.PigModelType', 'PigModelType'),
    },
    'vanilla_mcdoc.data.variants.wolf.WolfSounds': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.variants.wolf.WolfVariant': {
        'WolfVariantAssetInfo': ('vanilla_mcdoc.data.variants.wolf.WolfVariantAssetInfo', 'WolfVariantAssetInfo'),
    },
    'vanilla_mcdoc.data.variants.zombie_nautilus.ZombieNautilusVariant': {
        'ZombieNautilusModelType': ('vanilla_mcdoc.data.variants.zombie_nautilus.ZombieNautilusModelType', 'ZombieNautilusModelType'),
    },
    'vanilla_mcdoc.data.villager_trade.TradeCost': {
        'IntNumberProvider': ('vanilla_mcdoc.data.number_provider.IntNumberProvider', 'IntNumberProvider'),
    },
    'vanilla_mcdoc.data.villager_trade.VillagerTrade': {
        'FloatNumberProvider': ('vanilla_mcdoc.data.number_provider.FloatNumberProvider', 'FloatNumberProvider'),
        'IntNumberProvider': ('vanilla_mcdoc.data.number_provider.IntNumberProvider', 'IntNumberProvider'),
        'ItemModifierWithoutRootRef': ('vanilla_mcdoc.data.item_modifier.ItemModifierWithoutRootRef', 'ItemModifierWithoutRootRef'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
        'Predicate': ('vanilla_mcdoc.data.predicate.Predicate', 'Predicate'),
        'TradeCost': ('vanilla_mcdoc.data.villager_trade.TradeCost', 'TradeCost'),
    },
    'vanilla_mcdoc.data.worldgen.ClampedIntProvider': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.ConstantHeightProvider': {
        'VerticalAnchor': ('vanilla_mcdoc.data.worldgen.VerticalAnchor', 'VerticalAnchor'),
    },
    'vanilla_mcdoc.data.worldgen.HeightProvider': {
        'VerticalAnchor': ('vanilla_mcdoc.data.worldgen.VerticalAnchor', 'VerticalAnchor'),
    },
    'vanilla_mcdoc.data.worldgen.UniformHeightProvider': {
        'VerticalAnchor': ('vanilla_mcdoc.data.worldgen.VerticalAnchor', 'VerticalAnchor'),
    },
    'vanilla_mcdoc.data.worldgen.WeightListHeightProvider': {
        'HeightProvider': ('vanilla_mcdoc.data.worldgen.HeightProvider', 'HeightProvider'),
        'NonEmptyWeightedList': ('vanilla_mcdoc.util.NonEmptyWeightedList', 'NonEmptyWeightedList'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.ARGBColorAttribute': {
        'BlendToGray': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray', 'BlendToGray'),
        'ColorModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType', 'ColorModifierType'),
        'StringARGB': ('vanilla_mcdoc.util.color.StringARGB', 'StringARGB'),
        'StringRGB': ('vanilla_mcdoc.util.color.StringRGB', 'StringRGB'),
        'TranslucentColorAttributeModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier', 'TranslucentColorAttributeModifier'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.AmbientParticle': {
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.AmbientSounds': {
        'BiomeSoundAdditions': ('vanilla_mcdoc.data.worldgen.biome.BiomeSoundAdditions', 'BiomeSoundAdditions'),
        'MoodSound': ('vanilla_mcdoc.data.worldgen.biome.MoodSound', 'MoodSound'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.BackgroundMusic': {
        'BiomeMusic': ('vanilla_mcdoc.data.worldgen.biome.BiomeMusic', 'BiomeMusic'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.BedRule': {
        'BedRuleType': ('vanilla_mcdoc.data.worldgen.attribute.BedRuleType', 'BedRuleType'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.BooleanAttribute': {
        'BooleanAttributeModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanAttributeModifier', 'BooleanAttributeModifier'),
        'BooleanModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanModifierType', 'BooleanModifierType'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.DiscreteAttribute': {
        'OverrideModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.OverrideModifier', 'OverrideModifier'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.EnvironmentAttributeMap': {
        'AmbientParticle': ('vanilla_mcdoc.data.worldgen.attribute.AmbientParticle', 'AmbientParticle'),
        'AmbientSounds': ('vanilla_mcdoc.data.worldgen.attribute.AmbientSounds', 'AmbientSounds'),
        'BackgroundMusic': ('vanilla_mcdoc.data.worldgen.attribute.BackgroundMusic', 'BackgroundMusic'),
        'BedRule': ('vanilla_mcdoc.data.worldgen.attribute.BedRule', 'BedRule'),
        'BooleanAttributeModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanAttributeModifier', 'BooleanAttributeModifier'),
        'ColorAttributeModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ColorAttributeModifier', 'ColorAttributeModifier'),
        'FloatAttributeModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.FloatAttributeModifier', 'FloatAttributeModifier'),
        'ListModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifier', 'ListModifier'),
        'MergeableModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifier', 'MergeableModifier'),
        'MoonPhase': ('vanilla_mcdoc.data.util.MoonPhase', 'MoonPhase'),
        'NaturalMobSpawns': ('vanilla_mcdoc.data.worldgen.biome.NaturalMobSpawns', 'NaturalMobSpawns'),
        'OverrideModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.OverrideModifier', 'OverrideModifier'),
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
        'StringARGB': ('vanilla_mcdoc.util.color.StringARGB', 'StringARGB'),
        'StringRGB': ('vanilla_mcdoc.util.color.StringRGB', 'StringRGB'),
        'TranslucentColorAttributeModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier', 'TranslucentColorAttributeModifier'),
        'TriState': ('vanilla_mcdoc.data.worldgen.attribute.TriState', 'TriState'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.FloatAttribute': {
        'FloatAttributeModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.FloatAttributeModifier', 'FloatAttributeModifier'),
        'FloatModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.FloatModifierType', 'FloatModifierType'),
        'FloatWithAlpha': ('vanilla_mcdoc.data.worldgen.attribute.modifier.FloatWithAlpha', 'FloatWithAlpha'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.ListAttribute': {
        'ListModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifier', 'ListModifier'),
        'ListModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifierType', 'ListModifierType'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.MergeableAttribute': {
        'MergeableModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifier', 'MergeableModifier'),
        'MergeableModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifierType', 'MergeableModifierType'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.RGBColorAttribute': {
        'BlendToGray': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray', 'BlendToGray'),
        'ColorAttributeModifier': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ColorAttributeModifier', 'ColorAttributeModifier'),
        'ColorModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType', 'ColorModifierType'),
        'StringARGB': ('vanilla_mcdoc.util.color.StringARGB', 'StringARGB'),
        'StringRGB': ('vanilla_mcdoc.util.color.StringRGB', 'StringRGB'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanAttributeModifier': {
        'BooleanModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BooleanModifierType', 'BooleanModifierType'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.modifier.ColorAttributeModifier': {
        'BlendToGray': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray', 'BlendToGray'),
        'ColorModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType', 'ColorModifierType'),
        'StringARGB': ('vanilla_mcdoc.util.color.StringARGB', 'StringARGB'),
        'StringRGB': ('vanilla_mcdoc.util.color.StringRGB', 'StringRGB'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.modifier.FloatAttributeModifier': {
        'FloatModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.FloatModifierType', 'FloatModifierType'),
        'FloatWithAlpha': ('vanilla_mcdoc.data.worldgen.attribute.modifier.FloatWithAlpha', 'FloatWithAlpha'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifier': {
        'ListModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ListModifierType', 'ListModifierType'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifier': {
        'MergeableModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.MergeableModifierType', 'MergeableModifierType'),
    },
    'vanilla_mcdoc.data.worldgen.attribute.modifier.TranslucentColorAttributeModifier': {
        'BlendToGray': ('vanilla_mcdoc.data.worldgen.attribute.modifier.BlendToGray', 'BlendToGray'),
        'ColorModifierType': ('vanilla_mcdoc.data.worldgen.attribute.modifier.ColorModifierType', 'ColorModifierType'),
        'StringARGB': ('vanilla_mcdoc.util.color.StringARGB', 'StringARGB'),
        'StringRGB': ('vanilla_mcdoc.util.color.StringRGB', 'StringRGB'),
    },
    'vanilla_mcdoc.data.worldgen.biome.Biome': {
        'BiomeEffects': ('vanilla_mcdoc.data.worldgen.biome.BiomeEffects', 'BiomeEffects'),
        'CarverListRef': ('vanilla_mcdoc.data.worldgen.carver.CarverListRef', 'CarverListRef'),
        'PlacedFeatureRef': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef', 'PlacedFeatureRef'),
        'PositionalEnvironmentAttributeMap': ('vanilla_mcdoc.data.worldgen.attribute.PositionalEnvironmentAttributeMap', 'PositionalEnvironmentAttributeMap'),
        'TemperatureModifier': ('vanilla_mcdoc.data.worldgen.biome.TemperatureModifier', 'TemperatureModifier'),
    },
    'vanilla_mcdoc.data.worldgen.biome.BiomeEffects': {
        'GrassColorModifier': ('vanilla_mcdoc.data.worldgen.biome.GrassColorModifier', 'GrassColorModifier'),
        'StringRGB': ('vanilla_mcdoc.util.color.StringRGB', 'StringRGB'),
    },
    'vanilla_mcdoc.data.worldgen.biome.BiomeMusic': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.worldgen.biome.BiomeParticle': {
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
    },
    'vanilla_mcdoc.data.worldgen.biome.BiomeSoundAdditions': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.worldgen.biome.CarversPerStep': {
        'CarveStep': ('vanilla_mcdoc.data.worldgen.CarveStep', 'CarveStep'),
        'CarverListRef': ('vanilla_mcdoc.data.worldgen.carver.CarverListRef', 'CarverListRef'),
    },
    'vanilla_mcdoc.data.worldgen.biome.MoodSound': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.data.worldgen.biome.NaturalMobSpawns': {
        'KnownEntityId': ('vanilla_mcdoc.registry.KnownEntityId', 'KnownEntityId'),
        'MobSpawnCost': ('vanilla_mcdoc.data.worldgen.biome.MobSpawnCost', 'MobSpawnCost'),
        'SpawnerDataMap': ('vanilla_mcdoc.data.worldgen.biome.SpawnerDataMap', 'SpawnerDataMap'),
    },
    'vanilla_mcdoc.data.worldgen.biome.SpawnerData': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.biome.SpawnerDataMap': {
        'FlatWeightedList': ('vanilla_mcdoc.util.FlatWeightedList', 'FlatWeightedList'),
        'MobCategory': ('vanilla_mcdoc.data.worldgen.biome.MobCategory', 'MobCategory'),
        'SpawnerData': ('vanilla_mcdoc.data.worldgen.biome.SpawnerData', 'SpawnerData'),
    },
    'vanilla_mcdoc.data.worldgen.carver.CanyonConfig': {
        'CanyonShape': ('vanilla_mcdoc.data.worldgen.carver.CanyonShape', 'CanyonShape'),
        'FloatProvider': ('vanilla_mcdoc.data.worldgen.FloatProvider', 'FloatProvider'),
    },
    'vanilla_mcdoc.data.worldgen.carver.CanyonShape': {
        'FloatProvider': ('vanilla_mcdoc.data.worldgen.FloatProvider', 'FloatProvider'),
    },
    'vanilla_mcdoc.data.worldgen.carver.CarverConfigBase': {
        'HeightProvider': ('vanilla_mcdoc.data.worldgen.HeightProvider', 'HeightProvider'),
    },
    'vanilla_mcdoc.data.worldgen.carver.CarverDebugSettings': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.carver.CarverListRef': {
        'ConfiguredCarver': ('vanilla_mcdoc.data.worldgen.carver.ConfiguredCarver', 'ConfiguredCarver'),
    },
    'vanilla_mcdoc.data.worldgen.carver.CarverRef': {
        'ConfiguredCarver': ('vanilla_mcdoc.data.worldgen.carver.ConfiguredCarver', 'ConfiguredCarver'),
    },
    'vanilla_mcdoc.data.worldgen.carver.CaveConfig': {
        'FloatProvider': ('vanilla_mcdoc.data.worldgen.FloatProvider', 'FloatProvider'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Clamp': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
        'NoiseRange': ('vanilla_mcdoc.data.worldgen.density_function.NoiseRange', 'NoiseRange'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Constant': {
        'NoiseRange': ('vanilla_mcdoc.data.worldgen.density_function.NoiseRange', 'NoiseRange'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.CubicSpline': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
        'SplinePoint': ('vanilla_mcdoc.data.worldgen.density_function.SplinePoint', 'SplinePoint'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.DensityFunction': {
        'NoiseRange': ('vanilla_mcdoc.data.worldgen.density_function.NoiseRange', 'NoiseRange'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef': {
        'DensityFunction': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunction', 'DensityFunction'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.DistanceToPoint': {
        'DistanceMetric': ('vanilla_mcdoc.data.worldgen.density_function.DistanceMetric', 'DistanceMetric'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.FindTopSurface': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Gradient': {
        'Axis': ('vanilla_mcdoc.util.direction.Axis', 'Axis'),
        'NoiseRange': ('vanilla_mcdoc.data.worldgen.density_function.NoiseRange', 'NoiseRange'),
        'TilingMode': ('vanilla_mcdoc.data.worldgen.density_function.TilingMode', 'TilingMode'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.InvervalSelect': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
        'NoiseRange': ('vanilla_mcdoc.data.worldgen.density_function.NoiseRange', 'NoiseRange'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Lerp': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Noise': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
        'NoiseParametersRef': ('vanilla_mcdoc.data.worldgen.density_function.NoiseParametersRef', 'NoiseParametersRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.NoiseParametersRef': {
        'NoiseParameters': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters', 'NoiseParameters'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.OneArgument': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Pow': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.RangeChoice': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
        'NoiseRange': ('vanilla_mcdoc.data.worldgen.density_function.NoiseRange', 'NoiseRange'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Round': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Shift': {
        'NoiseParametersRef': ('vanilla_mcdoc.data.worldgen.density_function.NoiseParametersRef', 'NoiseParametersRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.ShiftedNoise': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Slice': {
        'Axis': ('vanilla_mcdoc.util.direction.Axis', 'Axis'),
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.Spline': {
        'CubicSpline': ('vanilla_mcdoc.data.worldgen.density_function.CubicSpline', 'CubicSpline'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.SplinePoint': {
        'CubicSpline': ('vanilla_mcdoc.data.worldgen.density_function.CubicSpline', 'CubicSpline'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.TerrainShaperSpline': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
        'NoiseRange': ('vanilla_mcdoc.data.worldgen.density_function.NoiseRange', 'NoiseRange'),
        'SplineType': ('vanilla_mcdoc.data.worldgen.density_function.SplineType', 'SplineType'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.TwoArguments': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.WeirdScaledSampler': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
        'NoiseParametersRef': ('vanilla_mcdoc.data.worldgen.density_function.NoiseParametersRef', 'NoiseParametersRef'),
        'RarityType': ('vanilla_mcdoc.data.worldgen.density_function.RarityType', 'RarityType'),
    },
    'vanilla_mcdoc.data.worldgen.density_function.YClampedGradient': {
        'NoiseRange': ('vanilla_mcdoc.data.worldgen.density_function.NoiseRange', 'NoiseRange'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.Dimension': {
        'ChunkGenerator': ('vanilla_mcdoc.data.worldgen.dimension.chunk_generator.ChunkGenerator', 'ChunkGenerator'),
        'DimensionTypeRef': ('vanilla_mcdoc.data.worldgen.dimension.DimensionTypeRef', 'DimensionTypeRef'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.DimensionType': {
        'CardinalLightType': ('vanilla_mcdoc.data.worldgen.dimension.CardinalLightType', 'CardinalLightType'),
        'GlobalEnvironmentAttributeMap': ('vanilla_mcdoc.data.worldgen.attribute.GlobalEnvironmentAttributeMap', 'GlobalEnvironmentAttributeMap'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
        'SkyboxType': ('vanilla_mcdoc.data.worldgen.dimension.SkyboxType', 'SkyboxType'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.biome_source.BiomeNoiseEntry': {
        'ClimateParameters': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameters', 'ClimateParameters'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameters': {
        'ClimateParameter': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameter', 'ClimateParameter'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.biome_source.DirectMultiNoise': {
        'ClimateParameters': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameters', 'ClimateParameters'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.biome_source.MultiNoiseBiomeSourceParameterList': {
        'MultiNoisePreset': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.MultiNoisePreset', 'MultiNoisePreset'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.chunk_generator.Flat': {
        'FlatGeneratorSettings': ('vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings', 'FlatGeneratorSettings'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorLayer': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings': {
        'FlatGeneratorLayer': ('vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorLayer', 'FlatGeneratorLayer'),
    },
    'vanilla_mcdoc.data.worldgen.dimension.chunk_generator.Noise': {
        'BiomeSource': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.BiomeSource', 'BiomeSource'),
        'NoiseGeneratorSettingsRef': ('vanilla_mcdoc.data.worldgen.noise_settings.NoiseGeneratorSettingsRef', 'NoiseGeneratorSettingsRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.BlockBlobConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.BlockColumnConfig': {
        'BlockColumnLayer': ('vanilla_mcdoc.data.worldgen.feature.BlockColumnLayer', 'BlockColumnLayer'),
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
    },
    'vanilla_mcdoc.data.worldgen.feature.BlockColumnLayer': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.BlockPileConfig': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.BlockStateRuleProviderEntry': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.ColumnPlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.ColumnsConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.ConfiguredFeatureRef': {
        'ConfiguredFeature': ('vanilla_mcdoc.data.worldgen.feature.ConfiguredFeature', 'ConfiguredFeature'),
    },
    'vanilla_mcdoc.data.worldgen.feature.CoralConfig': {
        'PlacedFeatureRef': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef', 'PlacedFeatureRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.DecoratedConfig': {
        'ConfiguredDecorator': ('vanilla_mcdoc.data.worldgen.feature.decorator.ConfiguredDecorator', 'ConfiguredDecorator'),
        'FeatureRef': ('vanilla_mcdoc.data.worldgen.feature.FeatureRef', 'FeatureRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.DeltaConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.DiskConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.EmeraldOreConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.EndSpikeConfig': {
        'EndSpike': ('vanilla_mcdoc.data.worldgen.feature.EndSpike', 'EndSpike'),
    },
    'vanilla_mcdoc.data.worldgen.feature.FillLayerConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.ForestRockConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.FossilConfig': {
        'ProcessorListRef': ('vanilla_mcdoc.data.worldgen.processor_list.ProcessorListRef', 'ProcessorListRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.GeodeBlockSettings': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.GeodeConfig': {
        'GeodeBlockSettings': ('vanilla_mcdoc.data.worldgen.feature.GeodeBlockSettings', 'GeodeBlockSettings'),
        'GeodeCrackSettings': ('vanilla_mcdoc.data.worldgen.feature.GeodeCrackSettings', 'GeodeCrackSettings'),
        'GeodeLayerSettings': ('vanilla_mcdoc.data.worldgen.feature.GeodeLayerSettings', 'GeodeLayerSettings'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.GrowingPlantConfig': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'WeightedList': ('vanilla_mcdoc.util.WeightedList', 'WeightedList'),
    },
    'vanilla_mcdoc.data.worldgen.feature.HugeFungusConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.HugeMushroomConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.IcebergConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.LakeConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.LargeSpeleothemConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'FloatProvider': ('vanilla_mcdoc.data.worldgen.FloatProvider', 'FloatProvider'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.ModernPatchConfig': {
        'FeatureRef': ('vanilla_mcdoc.data.worldgen.feature.FeatureRef', 'FeatureRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.MultifaceGrowthConfig': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
        'MultifaceBlock': ('vanilla_mcdoc.data.worldgen.feature.MultifaceBlock', 'MultifaceBlock'),
    },
    'vanilla_mcdoc.data.worldgen.feature.NetherForestVegetationConfig': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.NetherrackReplaceBlobsConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.OldPatchConfig': {
        'BlockPlacer': ('vanilla_mcdoc.data.worldgen.feature.BlockPlacer', 'BlockPlacer'),
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.OldSimpleBlockConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.OptionalSimpleBlockConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.OreConfig': {
        'TargetBlock': ('vanilla_mcdoc.data.worldgen.feature.TargetBlock', 'TargetBlock'),
    },
    'vanilla_mcdoc.data.worldgen.feature.OverlayConfig': {
        'PlacedFeatureListRef': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureListRef', 'PlacedFeatureListRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.ProjectedSquareConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.RandomBooleanSelector': {
        'FeatureRef': ('vanilla_mcdoc.data.worldgen.feature.FeatureRef', 'FeatureRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.RandomFeatureEntry': {
        'FeatureRef': ('vanilla_mcdoc.data.worldgen.feature.FeatureRef', 'FeatureRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.RandomNeighborSpreadConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.RandomPatchConfig': {
        'FeatureRef': ('vanilla_mcdoc.data.worldgen.feature.FeatureRef', 'FeatureRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.RandomSelector': {
        'FeatureRef': ('vanilla_mcdoc.data.worldgen.feature.FeatureRef', 'FeatureRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.ReplaceSingleBlockConfig': {
        'TargetBlock': ('vanilla_mcdoc.data.worldgen.feature.TargetBlock', 'TargetBlock'),
    },
    'vanilla_mcdoc.data.worldgen.feature.RootSystemConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'FeatureRef': ('vanilla_mcdoc.data.worldgen.feature.FeatureRef', 'FeatureRef'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.RuleBasedBlockStateProvider': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SeaPickleConfig': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SequenceConfig': {
        'PlacedFeatureListRef': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureListRef', 'PlacedFeatureListRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SimpleBlockConfig': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SimpleRandomSelectorConfig': {
        'PlacedFeatureListRef': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureListRef', 'PlacedFeatureListRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SingleBlockPillarConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'PlacedFeatureRef': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef', 'PlacedFeatureRef'),
        'VerticalDirection': ('vanilla_mcdoc.util.direction.VerticalDirection', 'VerticalDirection'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'FloatProvider': ('vanilla_mcdoc.data.worldgen.FloatProvider', 'FloatProvider'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
        'SpeleothemBaseBlockTransformer': ('vanilla_mcdoc.data.worldgen.feature.SpeleothemBaseBlockTransformer', 'SpeleothemBaseBlockTransformer'),
        'SpeleothemClusterPlacementMode': ('vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterPlacementMode', 'SpeleothemClusterPlacementMode'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterPlacementOptions': {
        'SpeleothemBaseBlockTransformer': ('vanilla_mcdoc.data.worldgen.feature.SpeleothemBaseBlockTransformer', 'SpeleothemBaseBlockTransformer'),
        'SpeleothemClusterPlacementMode': ('vanilla_mcdoc.data.worldgen.feature.SpeleothemClusterPlacementMode', 'SpeleothemClusterPlacementMode'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SpeleothemConfig': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SpikeConfig': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.SpringConfig': {
        'FluidState': ('vanilla_mcdoc.util.fluid_state.FluidState', 'FluidState'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.TargetBlock': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'RuleTest': ('vanilla_mcdoc.data.worldgen.processor_list.RuleTest', 'RuleTest'),
    },
    'vanilla_mcdoc.data.worldgen.feature.TemplateConfig': {
        'ProcessorListRef': ('vanilla_mcdoc.data.worldgen.processor_list.ProcessorListRef', 'ProcessorListRef'),
        'TemplateEntry': ('vanilla_mcdoc.data.worldgen.feature.TemplateEntry', 'TemplateEntry'),
        'WeightedList': ('vanilla_mcdoc.util.WeightedList', 'WeightedList'),
    },
    'vanilla_mcdoc.data.worldgen.feature.TemplateEntry': {
        'Rotation': ('vanilla_mcdoc.util.Rotation', 'Rotation'),
    },
    'vanilla_mcdoc.data.worldgen.feature.VegetationPatchConfig': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'CaveSurface': ('vanilla_mcdoc.data.worldgen.CaveSurface', 'CaveSurface'),
        'FeatureRef': ('vanilla_mcdoc.data.worldgen.feature.FeatureRef', 'FeatureRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.WeightedRandomFeatureConfig': {
        'PlacedFeatureRef': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef', 'PlacedFeatureRef'),
        'WeightedList': ('vanilla_mcdoc.util.WeightedList', 'WeightedList'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.BelowHeightmapPredicate': {
        'HeightmapType': ('vanilla_mcdoc.data.worldgen.HeightmapType', 'HeightmapType'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.CombiningPredicate': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.HasSturdyFacePredicate': {
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.HeightRangePredicate': {
        'VerticalAnchor': ('vanilla_mcdoc.data.worldgen.VerticalAnchor', 'VerticalAnchor'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.MatchingBlockTagPredicate': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.MatchingBlocksPredicate': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.NotPredicate': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.VolumeMatchPredicate': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_predicate.WouldSurvivePredicate': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.BaseNoiseProvider': {
        'NoiseParameters': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters', 'NoiseParameters'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProvider': {
        'FullBlockState': ('vanilla_mcdoc.util.block_state.FullBlockState', 'FullBlockState'),
        'TypedBlockStateProvider': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.TypedBlockStateProvider', 'TypedBlockStateProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef': {
        'BlockStateProvider': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProvider', 'BlockStateProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.CopyPropertiesProvider': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.DualNoiseProvider': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'InclusiveRange': ('vanilla_mcdoc.util.InclusiveRange', 'InclusiveRange'),
        'NoiseParameters': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.NoiseParameters', 'NoiseParameters'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.NoiseProvider': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.NoiseThresholdProvider': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.RandomBlockStateProvider': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.RandomizedIntStateProvider': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.RotatedStateProvider': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.SimpleStateProvider': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.feature.block_state_provider.WeightedBlockStateProvider': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'NonEmptyWeightedList': ('vanilla_mcdoc.util.NonEmptyWeightedList', 'NonEmptyWeightedList'),
    },
    'vanilla_mcdoc.data.worldgen.feature.decorator.CarvingMaskConfig': {
        'CarveStep': ('vanilla_mcdoc.data.worldgen.CarveStep', 'CarveStep'),
    },
    'vanilla_mcdoc.data.worldgen.feature.decorator.ConfiguredDecorator': {
        'CarvingMaskConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.CarvingMaskConfig', 'CarvingMaskConfig'),
        'CaveSurface': ('vanilla_mcdoc.data.worldgen.feature.decorator.CaveSurface', 'CaveSurface'),
        'ChanceConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.ChanceConfig', 'ChanceConfig'),
        'CountConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.CountConfig', 'CountConfig'),
        'CountExtraConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.CountExtraConfig', 'CountExtraConfig'),
        'CountNoiseBiasedConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.CountNoiseBiasedConfig', 'CountNoiseBiasedConfig'),
        'CountNoiseConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.CountNoiseConfig', 'CountNoiseConfig'),
        'DecoratedConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.DecoratedConfig', 'DecoratedConfig'),
        'HeightmapConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.HeightmapConfig', 'HeightmapConfig'),
        'RangeConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.RangeConfig', 'RangeConfig'),
        'WaterDepthThresholdConfig': ('vanilla_mcdoc.data.worldgen.feature.decorator.WaterDepthThresholdConfig', 'WaterDepthThresholdConfig'),
    },
    'vanilla_mcdoc.data.worldgen.feature.decorator.CountConfig': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.decorator.DecoratedConfig': {
        'ConfiguredDecorator': ('vanilla_mcdoc.data.worldgen.feature.decorator.ConfiguredDecorator', 'ConfiguredDecorator'),
    },
    'vanilla_mcdoc.data.worldgen.feature.decorator.HeightmapConfig': {
        'HeightmapType': ('vanilla_mcdoc.data.worldgen.HeightmapType', 'HeightmapType'),
    },
    'vanilla_mcdoc.data.worldgen.feature.decorator.RangeConfig': {
        'HeightProvider': ('vanilla_mcdoc.data.worldgen.HeightProvider', 'HeightProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.BlockPredicateFilter': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.CarvingMaskModifier': {
        'CarveStep': ('vanilla_mcdoc.data.worldgen.CarveStep', 'CarveStep'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.CountModifier': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.CountOnEveryLayerModifier': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.CuboidModifier': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.EnvironmentScanModifier': {
        'BlockPredicate': ('vanilla_mcdoc.data.worldgen.feature.block_predicate.BlockPredicate', 'BlockPredicate'),
        'VerticalDirection': ('vanilla_mcdoc.util.direction.VerticalDirection', 'VerticalDirection'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.HeightRangeModifier': {
        'HeightProvider': ('vanilla_mcdoc.data.worldgen.HeightProvider', 'HeightProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.HeightmapModifier': {
        'HeightmapType': ('vanilla_mcdoc.data.worldgen.HeightmapType', 'HeightmapType'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.OffsetModifier': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature': {
        'ConfiguredFeatureRef': ('vanilla_mcdoc.data.worldgen.feature.ConfiguredFeatureRef', 'ConfiguredFeatureRef'),
        'PlacementModifier': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacementModifier', 'PlacementModifier'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureListRef': {
        'PlacedFeature': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature', 'PlacedFeature'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef': {
        'PlacedFeature': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeature', 'PlacedFeature'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.RandomOffsetModifier': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.RandomlySelectedModifier': {
        'PlacementModifier': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacementModifier', 'PlacementModifier'),
    },
    'vanilla_mcdoc.data.worldgen.feature.placement.SurfaceRelativeThresholdFilter': {
        'HeightmapType': ('vanilla_mcdoc.data.worldgen.HeightmapType', 'HeightmapType'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.AboveRootPlacement': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.AlterGroundTreeDecorator': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.AttachedToLeavesTreeDecorator': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.AttachedToLogsTreeDecorator': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.BendingTrunkPlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.CherryFoliagePlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.CherryTrunkPlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'UniformIntProvider': ('vanilla_mcdoc.data.worldgen.UniformIntProvider', 'UniformIntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.FallenTreeConfig': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'TreeDecorator': ('vanilla_mcdoc.data.worldgen.feature.tree.TreeDecorator', 'TreeDecorator'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.FoliagePlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.MangroveRootPlacement': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.MangroveRootPlacer': {
        'MangroveRootPlacement': ('vanilla_mcdoc.data.worldgen.feature.tree.MangroveRootPlacement', 'MangroveRootPlacement'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.MegaPineFoliagePlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.PineFoliagePlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.PlaceOnGroundTreeDecorator': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.PoplarFoliagePlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.PoplarTrunkPlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.RandomSpreadFoliagePlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.RootPlacer': {
        'AboveRootPlacement': ('vanilla_mcdoc.data.worldgen.feature.tree.AboveRootPlacement', 'AboveRootPlacement'),
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.SprucePineFoliagePlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.TreeConfig': {
        'BlockStateProviderRef': ('vanilla_mcdoc.data.worldgen.feature.block_state_provider.BlockStateProviderRef', 'BlockStateProviderRef'),
        'FeatureSize': ('vanilla_mcdoc.data.worldgen.feature.tree.FeatureSize', 'FeatureSize'),
        'FoliagePlacer': ('vanilla_mcdoc.data.worldgen.feature.tree.FoliagePlacer', 'FoliagePlacer'),
        'RootPlacer': ('vanilla_mcdoc.data.worldgen.feature.tree.RootPlacer', 'RootPlacer'),
        'TreeDecorator': ('vanilla_mcdoc.data.worldgen.feature.tree.TreeDecorator', 'TreeDecorator'),
        'TrunkPlacer': ('vanilla_mcdoc.data.worldgen.feature.tree.TrunkPlacer', 'TrunkPlacer'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.TrunkPlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
    },
    'vanilla_mcdoc.data.worldgen.feature.tree.UpwardsBranchingTrunkPlacer': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.material_condition.MaterialConditionRef': {
        'KnownMaterialConditionId': ('vanilla_mcdoc.registry.KnownMaterialConditionId', 'KnownMaterialConditionId'),
        'MaterialCondition': ('vanilla_mcdoc.data.worldgen.material_condition.MaterialCondition', 'MaterialCondition'),
    },
    'vanilla_mcdoc.data.worldgen.material_condition.NotCondition': {
        'MaterialConditionRef': ('vanilla_mcdoc.data.worldgen.material_condition.MaterialConditionRef', 'MaterialConditionRef'),
    },
    'vanilla_mcdoc.data.worldgen.material_condition.StoneDepthCondition': {
        'CaveSurface': ('vanilla_mcdoc.data.worldgen.CaveSurface', 'CaveSurface'),
    },
    'vanilla_mcdoc.data.worldgen.material_condition.VerticalGradientCondition': {
        'VerticalAnchor': ('vanilla_mcdoc.data.worldgen.VerticalAnchor', 'VerticalAnchor'),
    },
    'vanilla_mcdoc.data.worldgen.material_condition.YAboveCondition': {
        'VerticalAnchor': ('vanilla_mcdoc.data.worldgen.VerticalAnchor', 'VerticalAnchor'),
    },
    'vanilla_mcdoc.data.worldgen.material_rule.BlockRule': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.material_rule.ConditionRule': {
        'MaterialConditionRef': ('vanilla_mcdoc.data.worldgen.material_condition.MaterialConditionRef', 'MaterialConditionRef'),
        'MaterialRuleRef': ('vanilla_mcdoc.data.worldgen.material_rule.MaterialRuleRef', 'MaterialRuleRef'),
    },
    'vanilla_mcdoc.data.worldgen.material_rule.MaterialRuleRef': {
        'KnownMaterialRuleId': ('vanilla_mcdoc.registry.KnownMaterialRuleId', 'KnownMaterialRuleId'),
        'MaterialRule': ('vanilla_mcdoc.data.worldgen.material_rule.MaterialRule', 'MaterialRule'),
    },
    'vanilla_mcdoc.data.worldgen.material_rule.OreVeinifier': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.material_rule.SequenceRule': {
        'MaterialRuleRef': ('vanilla_mcdoc.data.worldgen.material_rule.MaterialRuleRef', 'MaterialRuleRef'),
    },
    'vanilla_mcdoc.data.worldgen.noise_settings.Aquifer': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.noise_settings.DebugFunctionEntry': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.noise_settings.NoiseGeneratorSettings': {
        'Aquifer': ('vanilla_mcdoc.data.worldgen.noise_settings.Aquifer', 'Aquifer'),
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'DebugFunctionEntry': ('vanilla_mcdoc.data.worldgen.noise_settings.DebugFunctionEntry', 'DebugFunctionEntry'),
        'MaterialRuleRef': ('vanilla_mcdoc.data.worldgen.material_rule.MaterialRuleRef', 'MaterialRuleRef'),
        'NoiseRouter': ('vanilla_mcdoc.data.worldgen.noise_settings.NoiseRouter', 'NoiseRouter'),
        'NoiseSettings': ('vanilla_mcdoc.data.worldgen.noise_settings.NoiseSettings', 'NoiseSettings'),
        'SpawnTargetPoint': ('vanilla_mcdoc.data.worldgen.noise_settings.SpawnTargetPoint', 'SpawnTargetPoint'),
    },
    'vanilla_mcdoc.data.worldgen.noise_settings.NoiseRouter': {
        'DensityFunctionRef': ('vanilla_mcdoc.data.worldgen.density_function.DensityFunctionRef', 'DensityFunctionRef'),
    },
    'vanilla_mcdoc.data.worldgen.noise_settings.SpawnTargetPoint': {
        'ClimateParameter': ('vanilla_mcdoc.data.worldgen.dimension.biome_source.ClimateParameter', 'ClimateParameter'),
    },
    'vanilla_mcdoc.data.worldgen.noise_settings.StructureSettings': {
        'ConcentricRingsPlacement': ('vanilla_mcdoc.data.worldgen.structure_set.ConcentricRingsPlacement', 'ConcentricRingsPlacement'),
        'RandomSpreadPlacement': ('vanilla_mcdoc.data.worldgen.structure_set.RandomSpreadPlacement', 'RandomSpreadPlacement'),
    },
    'vanilla_mcdoc.data.worldgen.noise_settings.TerrainShaper': {
        'CubicSpline': ('vanilla_mcdoc.data.worldgen.density_function.CubicSpline', 'CubicSpline'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.AxisAlignedLinearPos': {
        'Axis': ('vanilla_mcdoc.util.direction.Axis', 'Axis'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.BlockIgnore': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.BlockMatch': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.BlockRot': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.BlockStateMatch': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.Capped': {
        'IntProvider': ('vanilla_mcdoc.data.worldgen.IntProvider', 'IntProvider'),
        'Processor': ('vanilla_mcdoc.data.worldgen.processor_list.Processor', 'Processor'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.CompositeMatch': {
        'RuleTest': ('vanilla_mcdoc.data.worldgen.processor_list.RuleTest', 'RuleTest'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.Gravity': {
        'HeightmapType': ('vanilla_mcdoc.data.worldgen.HeightmapType', 'HeightmapType'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.InvertedMatch': {
        'RuleTest': ('vanilla_mcdoc.data.worldgen.processor_list.RuleTest', 'RuleTest'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.ProcessorList': {
        'Processor': ('vanilla_mcdoc.data.worldgen.processor_list.Processor', 'Processor'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.ProcessorListObject': {
        'Processor': ('vanilla_mcdoc.data.worldgen.processor_list.Processor', 'Processor'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.ProcessorListRef': {
        'ProcessorList': ('vanilla_mcdoc.data.worldgen.processor_list.ProcessorList', 'ProcessorList'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.ProcessorRule': {
        'BlockEntityModifier': ('vanilla_mcdoc.data.worldgen.processor_list.BlockEntityModifier', 'BlockEntityModifier'),
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'PosRuleTest': ('vanilla_mcdoc.data.worldgen.processor_list.PosRuleTest', 'PosRuleTest'),
        'RuleTest': ('vanilla_mcdoc.data.worldgen.processor_list.RuleTest', 'RuleTest'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.ProtectedBlocks': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.RandomBlockMatch': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.RandomBlockStateMatch': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.Rule': {
        'ProcessorRule': ('vanilla_mcdoc.data.worldgen.processor_list.ProcessorRule', 'ProcessorRule'),
    },
    'vanilla_mcdoc.data.worldgen.processor_list.TagMatch': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.data.worldgen.structure.Jigsaw': {
        'HeightProvider': ('vanilla_mcdoc.data.worldgen.HeightProvider', 'HeightProvider'),
        'HeightmapType': ('vanilla_mcdoc.data.worldgen.HeightmapType', 'HeightmapType'),
        'JigsawDistanceLimits': ('vanilla_mcdoc.data.worldgen.structure.JigsawDistanceLimits', 'JigsawDistanceLimits'),
        'LiquidSettings': ('vanilla_mcdoc.data.worldgen.structure.LiquidSettings', 'LiquidSettings'),
        'PoolAlias': ('vanilla_mcdoc.data.worldgen.structure.PoolAlias', 'PoolAlias'),
    },
    'vanilla_mcdoc.data.worldgen.structure.Mineshaft': {
        'MineshaftType': ('vanilla_mcdoc.data.worldgen.structure.MineshaftType', 'MineshaftType'),
    },
    'vanilla_mcdoc.data.worldgen.structure.NetherFossil': {
        'HeightProvider': ('vanilla_mcdoc.data.worldgen.HeightProvider', 'HeightProvider'),
    },
    'vanilla_mcdoc.data.worldgen.structure.OceanRuin': {
        'BiomeTemperature': ('vanilla_mcdoc.data.worldgen.structure.BiomeTemperature', 'BiomeTemperature'),
    },
    'vanilla_mcdoc.data.worldgen.structure.RandomGroupPoolAlias': {
        'NonEmptyWeightedList': ('vanilla_mcdoc.util.NonEmptyWeightedList', 'NonEmptyWeightedList'),
        'PoolAlias': ('vanilla_mcdoc.data.worldgen.structure.PoolAlias', 'PoolAlias'),
    },
    'vanilla_mcdoc.data.worldgen.structure.RandomPoolAlias': {
        'NonEmptyWeightedList': ('vanilla_mcdoc.util.NonEmptyWeightedList', 'NonEmptyWeightedList'),
    },
    'vanilla_mcdoc.data.worldgen.structure.RuinedPortal': {
        'RuinedPortalSetup': ('vanilla_mcdoc.data.worldgen.structure.RuinedPortalSetup', 'RuinedPortalSetup'),
    },
    'vanilla_mcdoc.data.worldgen.structure.RuinedPortalSetup': {
        'RuinedPortalPlacement': ('vanilla_mcdoc.data.worldgen.structure.RuinedPortalPlacement', 'RuinedPortalPlacement'),
    },
    'vanilla_mcdoc.data.worldgen.structure.SpawnOverride': {
        'BoundingBox': ('vanilla_mcdoc.data.worldgen.structure.BoundingBox', 'BoundingBox'),
        'FlatWeightedList': ('vanilla_mcdoc.util.FlatWeightedList', 'FlatWeightedList'),
        'SpawnerData': ('vanilla_mcdoc.data.worldgen.biome.SpawnerData', 'SpawnerData'),
    },
    'vanilla_mcdoc.data.worldgen.structure.Structure': {
        'DecorationStep': ('vanilla_mcdoc.data.worldgen.DecorationStep', 'DecorationStep'),
        'MobCategory': ('vanilla_mcdoc.data.worldgen.biome.MobCategory', 'MobCategory'),
        'SpawnOverride': ('vanilla_mcdoc.data.worldgen.structure.SpawnOverride', 'SpawnOverride'),
        'TerrainAdaptation': ('vanilla_mcdoc.data.worldgen.structure.TerrainAdaptation', 'TerrainAdaptation'),
    },
    'vanilla_mcdoc.data.worldgen.structure.StructureRef': {
        'Structure': ('vanilla_mcdoc.data.worldgen.structure.Structure', 'Structure'),
    },
    'vanilla_mcdoc.data.worldgen.structure.TrickyTrialsStructureConfig': {
        'LiquidSettings': ('vanilla_mcdoc.data.worldgen.structure.LiquidSettings', 'LiquidSettings'),
    },
    'vanilla_mcdoc.data.worldgen.structure.WildUpdateStructureConfig': {
        'HeightProvider': ('vanilla_mcdoc.data.worldgen.HeightProvider', 'HeightProvider'),
        'HeightmapType': ('vanilla_mcdoc.data.worldgen.HeightmapType', 'HeightmapType'),
        'JigsawDistanceLimits': ('vanilla_mcdoc.data.worldgen.structure.JigsawDistanceLimits', 'JigsawDistanceLimits'),
    },
    'vanilla_mcdoc.data.worldgen.structure_set.ExclusionZone': {
        'StructureSetRef': ('vanilla_mcdoc.data.worldgen.structure_set.StructureSetRef', 'StructureSetRef'),
    },
    'vanilla_mcdoc.data.worldgen.structure_set.RandomSpreadPlacement': {
        'SpreadType': ('vanilla_mcdoc.data.worldgen.structure_set.SpreadType', 'SpreadType'),
    },
    'vanilla_mcdoc.data.worldgen.structure_set.SpreadingPlacementBase': {
        'ExclusionZone': ('vanilla_mcdoc.data.worldgen.structure_set.ExclusionZone', 'ExclusionZone'),
        'FrequencyReductionMethod': ('vanilla_mcdoc.data.worldgen.structure_set.FrequencyReductionMethod', 'FrequencyReductionMethod'),
    },
    'vanilla_mcdoc.data.worldgen.structure_set.StructureSet': {
        'StructurePlacement': ('vanilla_mcdoc.data.worldgen.structure_set.StructurePlacement', 'StructurePlacement'),
        'StructureSetElement': ('vanilla_mcdoc.data.worldgen.structure_set.StructureSetElement', 'StructureSetElement'),
    },
    'vanilla_mcdoc.data.worldgen.structure_set.StructureSetRef': {
        'StructureSet': ('vanilla_mcdoc.data.worldgen.structure_set.StructureSet', 'StructureSet'),
    },
    'vanilla_mcdoc.data.worldgen.surface_builder.Config': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.surface_builder.ConfiguredSurfaceBuilder': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.data.worldgen.surface_builder.ConfiguredSurfaceBuilderRef': {
        'ConfiguredSurfaceBuilder': ('vanilla_mcdoc.data.worldgen.surface_builder.ConfiguredSurfaceBuilder', 'ConfiguredSurfaceBuilder'),
    },
    'vanilla_mcdoc.data.worldgen.template_pool.ElementBase': {
        'Projection': ('vanilla_mcdoc.data.worldgen.template_pool.Projection', 'Projection'),
    },
    'vanilla_mcdoc.data.worldgen.template_pool.FeatureElement': {
        'PlacedFeatureRef': ('vanilla_mcdoc.data.worldgen.feature.placement.PlacedFeatureRef', 'PlacedFeatureRef'),
    },
    'vanilla_mcdoc.data.worldgen.template_pool.ListElement': {
        'Element': ('vanilla_mcdoc.data.worldgen.template_pool.Element', 'Element'),
    },
    'vanilla_mcdoc.data.worldgen.template_pool.SingleElement': {
        'LiquidSettings': ('vanilla_mcdoc.data.worldgen.structure.LiquidSettings', 'LiquidSettings'),
        'ProcessorListRef': ('vanilla_mcdoc.data.worldgen.processor_list.ProcessorListRef', 'ProcessorListRef'),
    },
    'vanilla_mcdoc.data.worldgen.template_pool.TemplatePool': {
        'WeightedElement': ('vanilla_mcdoc.data.worldgen.template_pool.WeightedElement', 'WeightedElement'),
    },
    'vanilla_mcdoc.data.worldgen.template_pool.WeightedElement': {
        'Element': ('vanilla_mcdoc.data.worldgen.template_pool.Element', 'Element'),
    },
    'vanilla_mcdoc.data.worldgen.world_preset.FlatGeneratorPreset': {
        'FlatGeneratorSettings': ('vanilla_mcdoc.data.worldgen.dimension.chunk_generator.FlatGeneratorSettings', 'FlatGeneratorSettings'),
    },
    'vanilla_mcdoc.data.worldgen.world_preset.WorldPreset': {
        'Dimension': ('vanilla_mcdoc.data.worldgen.dimension.Dimension', 'Dimension'),
    },
    'vanilla_mcdoc.pack.Pack': {
        'InclusiveRange': ('vanilla_mcdoc.util.InclusiveRange', 'InclusiveRange'),
        'PackFeatures': ('vanilla_mcdoc.pack.PackFeatures', 'PackFeatures'),
        'PackFilter': ('vanilla_mcdoc.pack.PackFilter', 'PackFilter'),
        'PackFormat': ('vanilla_mcdoc.pack.PackFormat', 'PackFormat'),
        'PackOverlays': ('vanilla_mcdoc.pack.PackOverlays', 'PackOverlays'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.pack.PackBase': {
        'InclusiveRange': ('vanilla_mcdoc.util.InclusiveRange', 'InclusiveRange'),
        'PackFormat': ('vanilla_mcdoc.pack.PackFormat', 'PackFormat'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.pack.PackFeatures': {
        'FeatureFlag': ('vanilla_mcdoc.pack.FeatureFlag', 'FeatureFlag'),
    },
    'vanilla_mcdoc.pack.PackFilter': {
        'BlockPattern': ('vanilla_mcdoc.pack.BlockPattern', 'BlockPattern'),
    },
    'vanilla_mcdoc.pack.PackOverlay': {
        'InclusiveRange': ('vanilla_mcdoc.util.InclusiveRange', 'InclusiveRange'),
        'PackFormat': ('vanilla_mcdoc.pack.PackFormat', 'PackFormat'),
    },
    'vanilla_mcdoc.pack.PackOverlays': {
        'PackOverlay': ('vanilla_mcdoc.pack.PackOverlay', 'PackOverlay'),
    },
    'vanilla_mcdoc.util.FlatWeightedList': {
        'FlatWeightedEntry': ('vanilla_mcdoc.util.FlatWeightedEntry', 'FlatWeightedEntry'),
    },
    'vanilla_mcdoc.util.NonEmptyFlatWeightedList': {
        'FlatWeightedEntry': ('vanilla_mcdoc.util.FlatWeightedEntry', 'FlatWeightedEntry'),
    },
    'vanilla_mcdoc.util.NonEmptyWeightedList': {
        'WeightedEntry': ('vanilla_mcdoc.util.WeightedEntry', 'WeightedEntry'),
    },
    'vanilla_mcdoc.util.WeightedList': {
        'WeightedEntry': ('vanilla_mcdoc.util.WeightedEntry', 'WeightedEntry'),
    },
    'vanilla_mcdoc.util.avatar.Profile': {
        'PlayerModelType': ('vanilla_mcdoc.util.avatar.PlayerModelType', 'PlayerModelType'),
        'ProfileProperty': ('vanilla_mcdoc.util.avatar.ProfileProperty', 'ProfileProperty'),
        'ProfilePropertyMap': ('vanilla_mcdoc.util.avatar.ProfilePropertyMap', 'ProfilePropertyMap'),
    },
    'vanilla_mcdoc.util.block_state.BlockState': {
        'FullBlockState': ('vanilla_mcdoc.util.block_state.FullBlockState', 'FullBlockState'),
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.util.block_state.FullBlockState': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.util.effect.ModernMobEffect': {
        'MobEffectInstance': ('vanilla_mcdoc.util.effect.MobEffectInstance', 'MobEffectInstance'),
    },
    'vanilla_mcdoc.util.effect.OldMobEffect': {
        'EffectId': ('vanilla_mcdoc.util.effect.EffectId', 'EffectId'),
        'MobEffectInstance': ('vanilla_mcdoc.util.effect.MobEffectInstance', 'MobEffectInstance'),
    },
    'vanilla_mcdoc.util.game_event.VibrationListener': {
        'PositionSource': ('vanilla_mcdoc.util.game_event.PositionSource', 'PositionSource'),
        'ReceivingEvent': ('vanilla_mcdoc.util.game_event.ReceivingEvent', 'ReceivingEvent'),
    },
    'vanilla_mcdoc.util.memory.Home': {
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
    },
    'vanilla_mcdoc.util.memory.JobSite': {
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
    },
    'vanilla_mcdoc.util.memory.LikedNoteblock': {
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
    },
    'vanilla_mcdoc.util.memory.MeetingPoint': {
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
    },
    'vanilla_mcdoc.util.memory.Memories': {
        'AdmiringDisable': ('vanilla_mcdoc.util.memory.AdmiringDisable', 'AdmiringDisable'),
        'AdmiringItem': ('vanilla_mcdoc.util.memory.AdmiringItem', 'AdmiringItem'),
        'AngryAt': ('vanilla_mcdoc.util.memory.AngryAt', 'AngryAt'),
        'AttackTargetCooldown': ('vanilla_mcdoc.util.memory.AttackTargetCooldown', 'AttackTargetCooldown'),
        'BreezeJumpCooldown': ('vanilla_mcdoc.util.memory.BreezeJumpCooldown', 'BreezeJumpCooldown'),
        'BreezeJumpInhaling': ('vanilla_mcdoc.util.memory.BreezeJumpInhaling', 'BreezeJumpInhaling'),
        'BreezeJumpTarget': ('vanilla_mcdoc.util.memory.BreezeJumpTarget', 'BreezeJumpTarget'),
        'BreezeLeavingWater': ('vanilla_mcdoc.util.memory.BreezeLeavingWater', 'BreezeLeavingWater'),
        'BreezeShoot': ('vanilla_mcdoc.util.memory.BreezeShoot', 'BreezeShoot'),
        'BreezeShootCharging': ('vanilla_mcdoc.util.memory.BreezeShootCharging', 'BreezeShootCharging'),
        'BreezeShootCooldown': ('vanilla_mcdoc.util.memory.BreezeShootCooldown', 'BreezeShootCooldown'),
        'BreezeShootRecover': ('vanilla_mcdoc.util.memory.BreezeShootRecover', 'BreezeShootRecover'),
        'ChargeCooldownTicks': ('vanilla_mcdoc.util.memory.ChargeCooldownTicks', 'ChargeCooldownTicks'),
        'DangerDetectedRecently': ('vanilla_mcdoc.util.memory.DangerDetectedRecently', 'DangerDetectedRecently'),
        'DigCooldown': ('vanilla_mcdoc.util.memory.DigCooldown', 'DigCooldown'),
        'GazeCooldownTicks': ('vanilla_mcdoc.util.memory.GazeCooldownTicks', 'GazeCooldownTicks'),
        'GolemDetectedRecently': ('vanilla_mcdoc.util.memory.GolemDetectedRecently', 'GolemDetectedRecently'),
        'HasHuntingCooldown': ('vanilla_mcdoc.util.memory.HasHuntingCooldown', 'HasHuntingCooldown'),
        'Home': ('vanilla_mcdoc.util.memory.Home', 'Home'),
        'HuntedRecently': ('vanilla_mcdoc.util.memory.HuntedRecently', 'HuntedRecently'),
        'IsEmerging': ('vanilla_mcdoc.util.memory.IsEmerging', 'IsEmerging'),
        'IsInWater': ('vanilla_mcdoc.util.memory.IsInWater', 'IsInWater'),
        'IsPanicking': ('vanilla_mcdoc.util.memory.IsPanicking', 'IsPanicking'),
        'IsPregnant': ('vanilla_mcdoc.util.memory.IsPregnant', 'IsPregnant'),
        'IsSniffing': ('vanilla_mcdoc.util.memory.IsSniffing', 'IsSniffing'),
        'ItemPickupCooldownTicks': ('vanilla_mcdoc.util.memory.ItemPickupCooldownTicks', 'ItemPickupCooldownTicks'),
        'JobSite': ('vanilla_mcdoc.util.memory.JobSite', 'JobSite'),
        'LastSlept': ('vanilla_mcdoc.util.memory.LastSlept', 'LastSlept'),
        'LastWoken': ('vanilla_mcdoc.util.memory.LastWoken', 'LastWoken'),
        'LastWorkedAtPoi': ('vanilla_mcdoc.util.memory.LastWorkedAtPoi', 'LastWorkedAtPoi'),
        'LikedNoteblock': ('vanilla_mcdoc.util.memory.LikedNoteblock', 'LikedNoteblock'),
        'LikedNoteblockCooldownTicks': ('vanilla_mcdoc.util.memory.LikedNoteblockCooldownTicks', 'LikedNoteblockCooldownTicks'),
        'LikedPlayer': ('vanilla_mcdoc.util.memory.LikedPlayer', 'LikedPlayer'),
        'LongJumpCoolingDown': ('vanilla_mcdoc.util.memory.LongJumpCoolingDown', 'LongJumpCoolingDown'),
        'MeetingPoint': ('vanilla_mcdoc.util.memory.MeetingPoint', 'MeetingPoint'),
        'PlayDeadTicks': ('vanilla_mcdoc.util.memory.PlayDeadTicks', 'PlayDeadTicks'),
        'PotentialJobSite': ('vanilla_mcdoc.util.memory.PotentialJobSite', 'PotentialJobSite'),
        'RamCooldownTicks': ('vanilla_mcdoc.util.memory.RamCooldownTicks', 'RamCooldownTicks'),
        'RecentProjectile': ('vanilla_mcdoc.util.memory.RecentProjectile', 'RecentProjectile'),
        'RoarSoundCooldown': ('vanilla_mcdoc.util.memory.RoarSoundCooldown', 'RoarSoundCooldown'),
        'RoarSoundDelay': ('vanilla_mcdoc.util.memory.RoarSoundDelay', 'RoarSoundDelay'),
        'SniffCooldown': ('vanilla_mcdoc.util.memory.SniffCooldown', 'SniffCooldown'),
        'SnifferExploredPositions': ('vanilla_mcdoc.util.memory.SnifferExploredPositions', 'SnifferExploredPositions'),
        'SonicBoomCooldown': ('vanilla_mcdoc.util.memory.SonicBoomCooldown', 'SonicBoomCooldown'),
        'SonicBoomSoundCooldown': ('vanilla_mcdoc.util.memory.SonicBoomSoundCooldown', 'SonicBoomSoundCooldown'),
        'SonicBoomSoundDelay': ('vanilla_mcdoc.util.memory.SonicBoomSoundDelay', 'SonicBoomSoundDelay'),
        'TemptationCooldownTicks': ('vanilla_mcdoc.util.memory.TemptationCooldownTicks', 'TemptationCooldownTicks'),
        'TouchCooldown': ('vanilla_mcdoc.util.memory.TouchCooldown', 'TouchCooldown'),
        'UniversalAnger': ('vanilla_mcdoc.util.memory.UniversalAnger', 'UniversalAnger'),
        'UnreachableTransportBlockPositions': ('vanilla_mcdoc.util.memory.UnreachableTransportBlockPositions', 'UnreachableTransportBlockPositions'),
        'VibrationCooldown': ('vanilla_mcdoc.util.memory.VibrationCooldown', 'VibrationCooldown'),
        'VisitedBlockPositions': ('vanilla_mcdoc.util.memory.VisitedBlockPositions', 'VisitedBlockPositions'),
    },
    'vanilla_mcdoc.util.memory.PotentialJobSite': {
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
    },
    'vanilla_mcdoc.util.memory.UnreachableTransportBlockPositions': {
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
    },
    'vanilla_mcdoc.util.memory.VisitedBlockPositions': {
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
    },
    'vanilla_mcdoc.util.particle.BlockParticle': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.util.particle.DustColorTransitionParticle': {
        'DustColor': ('vanilla_mcdoc.util.particle.DustColor', 'DustColor'),
    },
    'vanilla_mcdoc.util.particle.DustParticle': {
        'DustColor': ('vanilla_mcdoc.util.particle.DustColor', 'DustColor'),
    },
    'vanilla_mcdoc.util.particle.EffectParticle': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.util.particle.EntityEffectParticle': {
        'TranslucentParticle': ('vanilla_mcdoc.util.particle.TranslucentParticle', 'TranslucentParticle'),
    },
    'vanilla_mcdoc.util.particle.FlashParticle': {
        'TranslucentParticle': ('vanilla_mcdoc.util.particle.TranslucentParticle', 'TranslucentParticle'),
    },
    'vanilla_mcdoc.util.particle.ItemParticle': {
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.util.particle.OldDustTransition': {
        'DustColor': ('vanilla_mcdoc.util.particle.DustColor', 'DustColor'),
    },
    'vanilla_mcdoc.util.particle.TintedLeavesParticle': {
        'RGBA': ('vanilla_mcdoc.util.color.RGBA', 'RGBA'),
    },
    'vanilla_mcdoc.util.particle.TrailParticle': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.util.particle.VibrationParticleData': {
        'SafePositionSource': ('vanilla_mcdoc.util.particle.SafePositionSource', 'SafePositionSource'),
    },
    'vanilla_mcdoc.util.registry_ref.BlockListRef': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.util.registry_ref.ItemListRef': {
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.util.text.EntityHoverContent': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.util.text.EntityTooltipInfo': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.util.text.ItemHoverContent': {
        'DataComponentPatch': ('vanilla_mcdoc.world.component.DataComponentPatch', 'DataComponentPatch'),
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.util.text.KeybindText': {
        'Keybind': ('vanilla_mcdoc.util.text.Keybind', 'Keybind'),
    },
    'vanilla_mcdoc.util.text.ObjectTextConfig': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.util.text.PlayerHeadText': {
        'Profile': ('vanilla_mcdoc.util.avatar.Profile', 'Profile'),
    },
    'vanilla_mcdoc.util.text.SelectorText': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.util.text.ShowDialog': {
        'Dialog': ('vanilla_mcdoc.data.dialog.Dialog', 'Dialog'),
        'KnownDialogId': ('vanilla_mcdoc.registry.KnownDialogId', 'KnownDialogId'),
    },
    'vanilla_mcdoc.util.text.ShowEntity': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.util.text.ShowText': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.util.text.Text': {
        'TextObject': ('vanilla_mcdoc.util.text.TextObject', 'TextObject'),
    },
    'vanilla_mcdoc.util.text.TextBase': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.util.text.TextNbtBase': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.util.text.TextObject': {
        'Keybind': ('vanilla_mcdoc.util.text.Keybind', 'Keybind'),
        'Profile': ('vanilla_mcdoc.util.avatar.Profile', 'Profile'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
        'TranslationArg': ('vanilla_mcdoc.util.text.TranslationArg', 'TranslationArg'),
    },
    'vanilla_mcdoc.util.text.TextStyle': {
        'ClickEvent': ('vanilla_mcdoc.util.text.ClickEvent', 'ClickEvent'),
        'HoverEvent': ('vanilla_mcdoc.util.text.HoverEvent', 'HoverEvent'),
        'RGBA': ('vanilla_mcdoc.util.color.RGBA', 'RGBA'),
        'TextColor': ('vanilla_mcdoc.util.text.TextColor', 'TextColor'),
    },
    'vanilla_mcdoc.util.text.TranslatedText': {
        'TranslationArg': ('vanilla_mcdoc.util.text.TranslationArg', 'TranslationArg'),
    },
    'vanilla_mcdoc.util.text.TranslationArg': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.block.BlockEntity': {
        'DataComponentPatch': ('vanilla_mcdoc.world.component.DataComponentPatch', 'DataComponentPatch'),
    },
    'vanilla_mcdoc.world.block.Lockable': {
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
    },
    'vanilla_mcdoc.world.block.Nameable': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.block.banner.Banner': {
        'BannerPatternLayer': ('vanilla_mcdoc.world.block.banner.BannerPatternLayer', 'BannerPatternLayer'),
    },
    'vanilla_mcdoc.world.block.banner.BannerPatternLayer': {
        'BannerPattern': ('vanilla_mcdoc.data.variants.banner_pattern.BannerPattern', 'BannerPattern'),
        'DyeColor': ('vanilla_mcdoc.util.DyeColor', 'DyeColor'),
    },
    'vanilla_mcdoc.world.block.beehive.Bee': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
    },
    'vanilla_mcdoc.world.block.beehive.Beehive': {
        'Bee': ('vanilla_mcdoc.world.block.beehive.Bee', 'Bee'),
    },
    'vanilla_mcdoc.world.block.beehive.LegacyBee': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
    },
    'vanilla_mcdoc.world.block.brewing_stand.BrewingStand': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.block.brushable_block.BrushableBlock': {
        'DirectionByte': ('vanilla_mcdoc.util.direction.DirectionByte', 'DirectionByte'),
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.block.campfire.Campfire': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.block.chiseled_bookshelf.ChiseledBookshelf': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.block.command_block.BaseCommandBlock': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.block.container.Container27': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.block.container.Container9': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.block.container.Hopper': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.block.container.Shelf': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.block.decorated_pot.DecoratedPot': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
        'PotDecorations': ('vanilla_mcdoc.world.component.block.PotDecorations', 'PotDecorations'),
    },
    'vanilla_mcdoc.world.block.furnace.Furnace': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.block.head.Properties': {
        'Texture': ('vanilla_mcdoc.world.block.head.Texture', 'Texture'),
    },
    'vanilla_mcdoc.world.block.head.Skull': {
        'Profile': ('vanilla_mcdoc.util.avatar.Profile', 'Profile'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.block.head.SkullOwner': {
        'Properties': ('vanilla_mcdoc.world.block.head.Properties', 'Properties'),
    },
    'vanilla_mcdoc.world.block.jigsaw.Jigsaw': {
        'JointType': ('vanilla_mcdoc.world.block.jigsaw.JointType', 'JointType'),
    },
    'vanilla_mcdoc.world.block.jukebox.Jukebox': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.block.lectern.Lectern': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.block.moving_piston.MovingPiston': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'DirectionByte': ('vanilla_mcdoc.util.direction.DirectionByte', 'DirectionByte'),
    },
    'vanilla_mcdoc.world.block.sculk_catalyst.ChargeCursor': {
        'Direction': ('vanilla_mcdoc.util.direction.Direction', 'Direction'),
    },
    'vanilla_mcdoc.world.block.sculk_catalyst.SculkCatalyst': {
        'ChargeCursor': ('vanilla_mcdoc.world.block.sculk_catalyst.ChargeCursor', 'ChargeCursor'),
    },
    'vanilla_mcdoc.world.block.sculk_sensor.SculkSensor': {
        'VibrationListener': ('vanilla_mcdoc.util.game_event.VibrationListener', 'VibrationListener'),
    },
    'vanilla_mcdoc.world.block.sculk_shrieker.SculkShrieker': {
        'VibrationListener': ('vanilla_mcdoc.util.game_event.VibrationListener', 'VibrationListener'),
    },
    'vanilla_mcdoc.world.block.sign.OldSign': {
        'DyeColor': ('vanilla_mcdoc.util.color.DyeColor', 'DyeColor'),
    },
    'vanilla_mcdoc.world.block.sign.Sign': {
        'SignText': ('vanilla_mcdoc.world.component.block.SignText', 'SignText'),
    },
    'vanilla_mcdoc.world.block.spawner.CustomSpawnRules': {
        'InclusiveRange': ('vanilla_mcdoc.util.InclusiveRange', 'InclusiveRange'),
    },
    'vanilla_mcdoc.world.block.spawner.SpawnEquipment': {
        'EquipmentSlot': ('vanilla_mcdoc.util.slot.EquipmentSlot', 'EquipmentSlot'),
    },
    'vanilla_mcdoc.world.block.spawner.Spawner': {
        'SpawnPotential': ('vanilla_mcdoc.world.block.spawner.SpawnPotential', 'SpawnPotential'),
        'SpawnerEntry': ('vanilla_mcdoc.world.block.spawner.SpawnerEntry', 'SpawnerEntry'),
    },
    'vanilla_mcdoc.world.block.spawner.SpawnerEntry': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
        'CustomSpawnRules': ('vanilla_mcdoc.world.block.spawner.CustomSpawnRules', 'CustomSpawnRules'),
        'SpawnEquipment': ('vanilla_mcdoc.world.block.spawner.SpawnEquipment', 'SpawnEquipment'),
    },
    'vanilla_mcdoc.world.block.spawner.TrialSpawner': {
        'SpawnerEntry': ('vanilla_mcdoc.world.block.spawner.SpawnerEntry', 'SpawnerEntry'),
        'TrialSpawnerConfig': ('vanilla_mcdoc.data.trial_spawner.TrialSpawnerConfig', 'TrialSpawnerConfig'),
    },
    'vanilla_mcdoc.world.block.structure_block.StructureBlock': {
        'Mirror': ('vanilla_mcdoc.world.block.structure_block.Mirror', 'Mirror'),
        'Mode': ('vanilla_mcdoc.world.block.structure_block.Mode', 'Mode'),
        'Rotation': ('vanilla_mcdoc.world.block.structure_block.Rotation', 'Rotation'),
    },
    'vanilla_mcdoc.world.block.test_block.TestBlock': {
        'TestBlockMode': ('vanilla_mcdoc.world.block.test_block.TestBlockMode', 'TestBlockMode'),
    },
    'vanilla_mcdoc.world.block.test_instance_block.ErrorMarker': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlock': {
        'KnownTestInstanceId': ('vanilla_mcdoc.registry.KnownTestInstanceId', 'KnownTestInstanceId'),
        'Rotation': ('vanilla_mcdoc.util.Rotation', 'Rotation'),
        'TestInstanceBlockStatus': ('vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlockStatus', 'TestInstanceBlockStatus'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlockData': {
        'KnownTestInstanceId': ('vanilla_mcdoc.registry.KnownTestInstanceId', 'KnownTestInstanceId'),
        'Rotation': ('vanilla_mcdoc.util.Rotation', 'Rotation'),
        'TestInstanceBlockStatus': ('vanilla_mcdoc.world.block.test_instance_block.TestInstanceBlockStatus', 'TestInstanceBlockStatus'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.block.vault.Config': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.block.vault.ServerData': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.block.vault.SharedData': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.block.vault.Vault': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.component.CustomData': {
        'CustomDataMap': ('vanilla_mcdoc.world.component.CustomDataMap', 'CustomDataMap'),
    },
    'vanilla_mcdoc.world.component.DataComponentExactPredicate': {
        'AdventureModePredicate': ('vanilla_mcdoc.world.component.item.AdventureModePredicate', 'AdventureModePredicate'),
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
        'AttackRange': ('vanilla_mcdoc.world.component.item.AttackRange', 'AttackRange'),
        'AttributeModifier': ('vanilla_mcdoc.world.component.item.AttributeModifier', 'AttributeModifier'),
        'AxolotlVariant': ('vanilla_mcdoc.world.component.entity.AxolotlVariant', 'AxolotlVariant'),
        'BannerPatternLayer': ('vanilla_mcdoc.world.block.banner.BannerPatternLayer', 'BannerPatternLayer'),
        'BlockEntityData': ('vanilla_mcdoc.world.block.BlockEntityData', 'BlockEntityData'),
        'BrewingFuel': ('vanilla_mcdoc.world.component.item.BrewingFuel', 'BrewingFuel'),
        'BucketEntityData': ('vanilla_mcdoc.world.component.item.BucketEntityData', 'BucketEntityData'),
        'Compostable': ('vanilla_mcdoc.world.component.item.Compostable', 'Compostable'),
        'Consumable': ('vanilla_mcdoc.world.component.item.Consumable', 'Consumable'),
        'ContainerLoot': ('vanilla_mcdoc.world.component.block.ContainerLoot', 'ContainerLoot'),
        'ContainerSlot': ('vanilla_mcdoc.world.component.block.ContainerSlot', 'ContainerSlot'),
        'CookingFuel': ('vanilla_mcdoc.world.component.item.CookingFuel', 'CookingFuel'),
        'CustomData': ('vanilla_mcdoc.world.component.CustomData', 'CustomData'),
        'CustomModelData': ('vanilla_mcdoc.world.component.item.CustomModelData', 'CustomModelData'),
        'DamageResistant': ('vanilla_mcdoc.world.component.item.DamageResistant', 'DamageResistant'),
        'DamageType': ('vanilla_mcdoc.data.damage_type.DamageType', 'DamageType'),
        'DeathProtection': ('vanilla_mcdoc.world.component.item.DeathProtection', 'DeathProtection'),
        'DebugStickState': ('vanilla_mcdoc.world.component.item.DebugStickState', 'DebugStickState'),
        'DyeColor': ('vanilla_mcdoc.util.color.DyeColor', 'DyeColor'),
        'Enchantable': ('vanilla_mcdoc.world.component.item.Enchantable', 'Enchantable'),
        'EnchantmentLevels': ('vanilla_mcdoc.world.component.item.EnchantmentLevels', 'EnchantmentLevels'),
        'Equippable': ('vanilla_mcdoc.world.component.item.Equippable', 'Equippable'),
        'Explosion': ('vanilla_mcdoc.world.component.item.Explosion', 'Explosion'),
        'Fireworks': ('vanilla_mcdoc.world.component.item.Fireworks', 'Fireworks'),
        'Food': ('vanilla_mcdoc.world.component.item.Food', 'Food'),
        'FoxType': ('vanilla_mcdoc.world.component.entity.FoxType', 'FoxType'),
        'HorseVariant': ('vanilla_mcdoc.world.component.entity.HorseVariant', 'HorseVariant'),
        'Instrument': ('vanilla_mcdoc.data.variants.instrument.Instrument', 'Instrument'),
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
        'KineticWeapon': ('vanilla_mcdoc.world.component.item.KineticWeapon', 'KineticWeapon'),
        'LlamaVariant': ('vanilla_mcdoc.world.component.entity.LlamaVariant', 'LlamaVariant'),
        'LodestoneTracker': ('vanilla_mcdoc.world.component.item.LodestoneTracker', 'LodestoneTracker'),
        'MapDecorations': ('vanilla_mcdoc.world.component.item.MapDecorations', 'MapDecorations'),
        'MobVisibility': ('vanilla_mcdoc.world.component.item.MobVisibility', 'MobVisibility'),
        'MooshroomType': ('vanilla_mcdoc.world.component.entity.MooshroomType', 'MooshroomType'),
        'Occupant': ('vanilla_mcdoc.world.component.block.Occupant', 'Occupant'),
        'ParrotVariant': ('vanilla_mcdoc.world.component.entity.ParrotVariant', 'ParrotVariant'),
        'PersistentDataComponent': ('vanilla_mcdoc.world.component.PersistentDataComponent', 'PersistentDataComponent'),
        'PiercingWeapon': ('vanilla_mcdoc.world.component.item.PiercingWeapon', 'PiercingWeapon'),
        'PotDecorations': ('vanilla_mcdoc.world.component.block.PotDecorations', 'PotDecorations'),
        'PotionContents': ('vanilla_mcdoc.world.component.item.PotionContents', 'PotionContents'),
        'Profile': ('vanilla_mcdoc.util.avatar.Profile', 'Profile'),
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
        'RabbitVariant': ('vanilla_mcdoc.world.component.entity.RabbitVariant', 'RabbitVariant'),
        'Rarity': ('vanilla_mcdoc.world.component.item.Rarity', 'Rarity'),
        'Repairable': ('vanilla_mcdoc.world.component.item.Repairable', 'Repairable'),
        'SalmonType': ('vanilla_mcdoc.world.component.entity.SalmonType', 'SalmonType'),
        'SignText': ('vanilla_mcdoc.world.component.block.SignText', 'SignText'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
        'SuspiciousStewEffect': ('vanilla_mcdoc.world.component.item.SuspiciousStewEffect', 'SuspiciousStewEffect'),
        'SwingAnimation': ('vanilla_mcdoc.world.component.item.SwingAnimation', 'SwingAnimation'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
        'Tool': ('vanilla_mcdoc.world.component.item.Tool', 'Tool'),
        'TooltipDisplay': ('vanilla_mcdoc.world.component.item.TooltipDisplay', 'TooltipDisplay'),
        'Trim': ('vanilla_mcdoc.world.component.item.Trim', 'Trim'),
        'TropicalFishPattern': ('vanilla_mcdoc.world.component.entity.TropicalFishPattern', 'TropicalFishPattern'),
        'Unbreakable': ('vanilla_mcdoc.world.component.item.Unbreakable', 'Unbreakable'),
        'UseCooldown': ('vanilla_mcdoc.world.component.item.UseCooldown', 'UseCooldown'),
        'UseEffects': ('vanilla_mcdoc.world.component.item.UseEffects', 'UseEffects'),
        'VillagerFood': ('vanilla_mcdoc.world.component.item.VillagerFood', 'VillagerFood'),
        'Weapon': ('vanilla_mcdoc.world.component.item.Weapon', 'Weapon'),
        'WritableBookContent': ('vanilla_mcdoc.world.component.item.WritableBookContent', 'WritableBookContent'),
        'WrittenBookContent': ('vanilla_mcdoc.world.component.item.WrittenBookContent', 'WrittenBookContent'),
        'blocks_attacks': ('vanilla_mcdoc.world.component.item.blocks_attacks', 'blocks_attacks'),
    },
    'vanilla_mcdoc.world.component.DataComponentPatch': {
        'AdventureModePredicate': ('vanilla_mcdoc.world.component.item.AdventureModePredicate', 'AdventureModePredicate'),
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
        'AttackRange': ('vanilla_mcdoc.world.component.item.AttackRange', 'AttackRange'),
        'AttributeModifier': ('vanilla_mcdoc.world.component.item.AttributeModifier', 'AttributeModifier'),
        'AxolotlVariant': ('vanilla_mcdoc.world.component.entity.AxolotlVariant', 'AxolotlVariant'),
        'BannerPatternLayer': ('vanilla_mcdoc.world.block.banner.BannerPatternLayer', 'BannerPatternLayer'),
        'BlockEntityData': ('vanilla_mcdoc.world.block.BlockEntityData', 'BlockEntityData'),
        'BrewingFuel': ('vanilla_mcdoc.world.component.item.BrewingFuel', 'BrewingFuel'),
        'BucketEntityData': ('vanilla_mcdoc.world.component.item.BucketEntityData', 'BucketEntityData'),
        'Compostable': ('vanilla_mcdoc.world.component.item.Compostable', 'Compostable'),
        'Consumable': ('vanilla_mcdoc.world.component.item.Consumable', 'Consumable'),
        'ContainerLoot': ('vanilla_mcdoc.world.component.block.ContainerLoot', 'ContainerLoot'),
        'ContainerSlot': ('vanilla_mcdoc.world.component.block.ContainerSlot', 'ContainerSlot'),
        'CookingFuel': ('vanilla_mcdoc.world.component.item.CookingFuel', 'CookingFuel'),
        'CustomData': ('vanilla_mcdoc.world.component.CustomData', 'CustomData'),
        'CustomModelData': ('vanilla_mcdoc.world.component.item.CustomModelData', 'CustomModelData'),
        'DamageResistant': ('vanilla_mcdoc.world.component.item.DamageResistant', 'DamageResistant'),
        'DamageType': ('vanilla_mcdoc.data.damage_type.DamageType', 'DamageType'),
        'DeathProtection': ('vanilla_mcdoc.world.component.item.DeathProtection', 'DeathProtection'),
        'DebugStickState': ('vanilla_mcdoc.world.component.item.DebugStickState', 'DebugStickState'),
        'DyeColor': ('vanilla_mcdoc.util.color.DyeColor', 'DyeColor'),
        'Enchantable': ('vanilla_mcdoc.world.component.item.Enchantable', 'Enchantable'),
        'EnchantmentLevels': ('vanilla_mcdoc.world.component.item.EnchantmentLevels', 'EnchantmentLevels'),
        'Equippable': ('vanilla_mcdoc.world.component.item.Equippable', 'Equippable'),
        'Explosion': ('vanilla_mcdoc.world.component.item.Explosion', 'Explosion'),
        'Fireworks': ('vanilla_mcdoc.world.component.item.Fireworks', 'Fireworks'),
        'Food': ('vanilla_mcdoc.world.component.item.Food', 'Food'),
        'FoxType': ('vanilla_mcdoc.world.component.entity.FoxType', 'FoxType'),
        'HorseVariant': ('vanilla_mcdoc.world.component.entity.HorseVariant', 'HorseVariant'),
        'Instrument': ('vanilla_mcdoc.data.variants.instrument.Instrument', 'Instrument'),
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
        'KineticWeapon': ('vanilla_mcdoc.world.component.item.KineticWeapon', 'KineticWeapon'),
        'LlamaVariant': ('vanilla_mcdoc.world.component.entity.LlamaVariant', 'LlamaVariant'),
        'LodestoneTracker': ('vanilla_mcdoc.world.component.item.LodestoneTracker', 'LodestoneTracker'),
        'MapDecorations': ('vanilla_mcdoc.world.component.item.MapDecorations', 'MapDecorations'),
        'MobVisibility': ('vanilla_mcdoc.world.component.item.MobVisibility', 'MobVisibility'),
        'MooshroomType': ('vanilla_mcdoc.world.component.entity.MooshroomType', 'MooshroomType'),
        'Occupant': ('vanilla_mcdoc.world.component.block.Occupant', 'Occupant'),
        'ParrotVariant': ('vanilla_mcdoc.world.component.entity.ParrotVariant', 'ParrotVariant'),
        'PiercingWeapon': ('vanilla_mcdoc.world.component.item.PiercingWeapon', 'PiercingWeapon'),
        'PotDecorations': ('vanilla_mcdoc.world.component.block.PotDecorations', 'PotDecorations'),
        'PotionContents': ('vanilla_mcdoc.world.component.item.PotionContents', 'PotionContents'),
        'Profile': ('vanilla_mcdoc.util.avatar.Profile', 'Profile'),
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
        'RabbitVariant': ('vanilla_mcdoc.world.component.entity.RabbitVariant', 'RabbitVariant'),
        'Rarity': ('vanilla_mcdoc.world.component.item.Rarity', 'Rarity'),
        'Repairable': ('vanilla_mcdoc.world.component.item.Repairable', 'Repairable'),
        'SalmonType': ('vanilla_mcdoc.world.component.entity.SalmonType', 'SalmonType'),
        'SignText': ('vanilla_mcdoc.world.component.block.SignText', 'SignText'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
        'SuspiciousStewEffect': ('vanilla_mcdoc.world.component.item.SuspiciousStewEffect', 'SuspiciousStewEffect'),
        'SwingAnimation': ('vanilla_mcdoc.world.component.item.SwingAnimation', 'SwingAnimation'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
        'Tool': ('vanilla_mcdoc.world.component.item.Tool', 'Tool'),
        'TooltipDisplay': ('vanilla_mcdoc.world.component.item.TooltipDisplay', 'TooltipDisplay'),
        'Trim': ('vanilla_mcdoc.world.component.item.Trim', 'Trim'),
        'TropicalFishPattern': ('vanilla_mcdoc.world.component.entity.TropicalFishPattern', 'TropicalFishPattern'),
        'Unbreakable': ('vanilla_mcdoc.world.component.item.Unbreakable', 'Unbreakable'),
        'UseCooldown': ('vanilla_mcdoc.world.component.item.UseCooldown', 'UseCooldown'),
        'UseEffects': ('vanilla_mcdoc.world.component.item.UseEffects', 'UseEffects'),
        'VillagerFood': ('vanilla_mcdoc.world.component.item.VillagerFood', 'VillagerFood'),
        'Weapon': ('vanilla_mcdoc.world.component.item.Weapon', 'Weapon'),
        'WritableBookContent': ('vanilla_mcdoc.world.component.item.WritableBookContent', 'WritableBookContent'),
        'WrittenBookContent': ('vanilla_mcdoc.world.component.item.WrittenBookContent', 'WrittenBookContent'),
        'blocks_attacks': ('vanilla_mcdoc.world.component.item.blocks_attacks', 'blocks_attacks'),
    },
    'vanilla_mcdoc.world.component.DataComponentPredicate': {
        'AttributeModifiersPredicate': ('vanilla_mcdoc.world.component.predicate.AttributeModifiersPredicate', 'AttributeModifiersPredicate'),
        'BundleContentsPredicate': ('vanilla_mcdoc.world.component.predicate.BundleContentsPredicate', 'BundleContentsPredicate'),
        'ContainerPredicate': ('vanilla_mcdoc.world.component.predicate.ContainerPredicate', 'ContainerPredicate'),
        'CustomData': ('vanilla_mcdoc.world.component.CustomData', 'CustomData'),
        'EnchantmentPredicate': ('vanilla_mcdoc.data.advancement.predicate.EnchantmentPredicate', 'EnchantmentPredicate'),
        'FireworkExplosionPredicate': ('vanilla_mcdoc.world.component.predicate.FireworkExplosionPredicate', 'FireworkExplosionPredicate'),
        'FireworksPredicate': ('vanilla_mcdoc.world.component.predicate.FireworksPredicate', 'FireworksPredicate'),
        'ItemDamagePredicate': ('vanilla_mcdoc.world.component.predicate.ItemDamagePredicate', 'ItemDamagePredicate'),
        'JukeboxPlayablePredicate': ('vanilla_mcdoc.world.component.predicate.JukeboxPlayablePredicate', 'JukeboxPlayablePredicate'),
        'PotionsPredicate': ('vanilla_mcdoc.world.component.predicate.PotionsPredicate', 'PotionsPredicate'),
        'TrimPredicate': ('vanilla_mcdoc.world.component.predicate.TrimPredicate', 'TrimPredicate'),
        'WritableBookPredicate': ('vanilla_mcdoc.world.component.predicate.WritableBookPredicate', 'WritableBookPredicate'),
        'WrittenBookPredicate': ('vanilla_mcdoc.world.component.predicate.WrittenBookPredicate', 'WrittenBookPredicate'),
    },
    'vanilla_mcdoc.world.component.block.ContainerSlot': {
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.world.component.block.Occupant': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
    },
    'vanilla_mcdoc.world.component.block.PotDecorations': {
        'ItemStackTemplate': ('vanilla_mcdoc.world.item.ItemStackTemplate', 'ItemStackTemplate'),
    },
    'vanilla_mcdoc.world.component.block.SignLines': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.component.block.SignText': {
        'DyeColor': ('vanilla_mcdoc.util.color.DyeColor', 'DyeColor'),
        'SignLines': ('vanilla_mcdoc.world.component.block.SignLines', 'SignLines'),
    },
    'vanilla_mcdoc.world.component.item.AdventureModePredicate': {
        'BlockPredicate': ('vanilla_mcdoc.data.advancement.predicate.BlockPredicate', 'BlockPredicate'),
    },
    'vanilla_mcdoc.world.component.item.ApplyEffectsConsumeEffect': {
        'MobEffectInstance': ('vanilla_mcdoc.util.effect.MobEffectInstance', 'MobEffectInstance'),
    },
    'vanilla_mcdoc.world.component.item.AttributeDisplayTextOverride': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.component.item.AttributeModifier': {
        'AttributeDisplay': ('vanilla_mcdoc.world.component.item.AttributeDisplay', 'AttributeDisplay'),
        'AttributeOperation': ('vanilla_mcdoc.util.attribute.AttributeOperation', 'AttributeOperation'),
        'EquipmentSlotGroup': ('vanilla_mcdoc.util.slot.EquipmentSlotGroup', 'EquipmentSlotGroup'),
    },
    'vanilla_mcdoc.world.component.item.AttributeModifiers': {
        'AttributeModifier': ('vanilla_mcdoc.world.component.item.AttributeModifier', 'AttributeModifier'),
    },
    'vanilla_mcdoc.world.component.item.BrewingFuel': {
        'KnownContextFloatProviderId': ('vanilla_mcdoc.registry.KnownContextFloatProviderId', 'KnownContextFloatProviderId'),
        'KnownContextIntProviderId': ('vanilla_mcdoc.registry.KnownContextIntProviderId', 'KnownContextIntProviderId'),
    },
    'vanilla_mcdoc.world.component.item.Compostable': {
        'KnownContextIntProviderId': ('vanilla_mcdoc.registry.KnownContextIntProviderId', 'KnownContextIntProviderId'),
    },
    'vanilla_mcdoc.world.component.item.Consumable': {
        'ConsumeEffect': ('vanilla_mcdoc.world.component.item.ConsumeEffect', 'ConsumeEffect'),
        'ItemUseAnimation': ('vanilla_mcdoc.world.component.item.ItemUseAnimation', 'ItemUseAnimation'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.world.component.item.CookingFuel': {
        'KnownContextFloatProviderId': ('vanilla_mcdoc.registry.KnownContextFloatProviderId', 'KnownContextFloatProviderId'),
        'KnownContextIntProviderId': ('vanilla_mcdoc.registry.KnownContextIntProviderId', 'KnownContextIntProviderId'),
    },
    'vanilla_mcdoc.world.component.item.CustomModelData': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.world.component.item.DeathProtection': {
        'ConsumeEffect': ('vanilla_mcdoc.world.component.item.ConsumeEffect', 'ConsumeEffect'),
    },
    'vanilla_mcdoc.world.component.item.DebugStickState': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.world.component.item.Enchantments': {
        'EnchantmentLevels': ('vanilla_mcdoc.world.component.item.EnchantmentLevels', 'EnchantmentLevels'),
    },
    'vanilla_mcdoc.world.component.item.Equippable': {
        'EquipmentSlot': ('vanilla_mcdoc.util.slot.EquipmentSlot', 'EquipmentSlot'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.world.component.item.Explosion': {
        'FireworkShape': ('vanilla_mcdoc.world.component.item.FireworkShape', 'FireworkShape'),
    },
    'vanilla_mcdoc.world.component.item.Fireworks': {
        'Explosion': ('vanilla_mcdoc.world.component.item.Explosion', 'Explosion'),
    },
    'vanilla_mcdoc.world.component.item.FoodEffect': {
        'MobEffectInstance': ('vanilla_mcdoc.util.effect.MobEffectInstance', 'MobEffectInstance'),
    },
    'vanilla_mcdoc.world.component.item.KineticWeapon': {
        'KineticWeaponEffectCondition': ('vanilla_mcdoc.world.component.item.KineticWeaponEffectCondition', 'KineticWeaponEffectCondition'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.world.component.item.LodestoneTracker': {
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
    },
    'vanilla_mcdoc.world.component.item.MapDecorations': {
        'MapDecoration': ('vanilla_mcdoc.world.component.item.MapDecoration', 'MapDecoration'),
    },
    'vanilla_mcdoc.world.component.item.PiercingWeapon': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.world.component.item.PlaySoundConsumeEffect': {
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.world.component.item.PotionContents': {
        'MobEffectInstance': ('vanilla_mcdoc.util.effect.MobEffectInstance', 'MobEffectInstance'),
    },
    'vanilla_mcdoc.world.component.item.Repairable': {
        'KnownItemId': ('vanilla_mcdoc.registry.KnownItemId', 'KnownItemId'),
    },
    'vanilla_mcdoc.world.component.item.SwingAnimation': {
        'SwingAnimationType': ('vanilla_mcdoc.world.component.item.SwingAnimationType', 'SwingAnimationType'),
    },
    'vanilla_mcdoc.world.component.item.Tool': {
        'ToolRule': ('vanilla_mcdoc.world.component.item.ToolRule', 'ToolRule'),
    },
    'vanilla_mcdoc.world.component.item.ToolRule': {
        'KnownBlockId': ('vanilla_mcdoc.registry.KnownBlockId', 'KnownBlockId'),
    },
    'vanilla_mcdoc.world.component.item.Trim': {
        'TrimMaterial': ('vanilla_mcdoc.data.trim.TrimMaterial', 'TrimMaterial'),
        'TrimPattern': ('vanilla_mcdoc.data.trim.TrimPattern', 'TrimPattern'),
    },
    'vanilla_mcdoc.world.component.item.WritableBookContent': {
        'Filterable': ('vanilla_mcdoc.util.Filterable', 'Filterable'),
    },
    'vanilla_mcdoc.world.component.item.WrittenBookContent': {
        'BookGeneration': ('vanilla_mcdoc.world.component.item.BookGeneration', 'BookGeneration'),
        'Filterable': ('vanilla_mcdoc.util.Filterable', 'Filterable'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.component.item.blocks_attacks': {
        'DamageReduction': ('vanilla_mcdoc.world.component.item.DamageReduction', 'DamageReduction'),
        'ItemDamageFunction': ('vanilla_mcdoc.world.component.item.ItemDamageFunction', 'ItemDamageFunction'),
        'SoundEventRef': ('vanilla_mcdoc.data.util.SoundEventRef', 'SoundEventRef'),
    },
    'vanilla_mcdoc.world.component.predicate.AttributeModifiersPredicate': {
        'AttributeModifiersPredicateEntry': ('vanilla_mcdoc.world.component.predicate.AttributeModifiersPredicateEntry', 'AttributeModifiersPredicateEntry'),
        'CollectionPredicate': ('vanilla_mcdoc.world.component.predicate.CollectionPredicate', 'CollectionPredicate'),
    },
    'vanilla_mcdoc.world.component.predicate.AttributeModifiersPredicateEntry': {
        'AttributeOperation': ('vanilla_mcdoc.util.attribute.AttributeOperation', 'AttributeOperation'),
        'EquipmentSlotGroup': ('vanilla_mcdoc.util.slot.EquipmentSlotGroup', 'EquipmentSlotGroup'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.world.component.predicate.BundleContentsPredicate': {
        'CollectionPredicate': ('vanilla_mcdoc.world.component.predicate.CollectionPredicate', 'CollectionPredicate'),
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
    },
    'vanilla_mcdoc.world.component.predicate.CollectionCountPredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.world.component.predicate.CollectionPredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.world.component.predicate.ContainerPredicate': {
        'CollectionPredicate': ('vanilla_mcdoc.world.component.predicate.CollectionPredicate', 'CollectionPredicate'),
        'ItemPredicate': ('vanilla_mcdoc.data.advancement.predicate.ItemPredicate', 'ItemPredicate'),
    },
    'vanilla_mcdoc.world.component.predicate.FireworkExplosionPredicate': {
        'FireworkShape': ('vanilla_mcdoc.world.component.item.FireworkShape', 'FireworkShape'),
    },
    'vanilla_mcdoc.world.component.predicate.FireworksPredicate': {
        'CollectionPredicate': ('vanilla_mcdoc.world.component.predicate.CollectionPredicate', 'CollectionPredicate'),
        'FireworkExplosionPredicate': ('vanilla_mcdoc.world.component.predicate.FireworkExplosionPredicate', 'FireworkExplosionPredicate'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.world.component.predicate.ItemDamagePredicate': {
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
    },
    'vanilla_mcdoc.world.component.predicate.PotionsPredicate': {
        'CollectionPredicate': ('vanilla_mcdoc.world.component.predicate.CollectionPredicate', 'CollectionPredicate'),
        'EntityEffectsPredicate': ('vanilla_mcdoc.data.advancement.predicate.EntityEffectsPredicate', 'EntityEffectsPredicate'),
        'PotionTypeMatch': ('vanilla_mcdoc.world.component.predicate.PotionTypeMatch', 'PotionTypeMatch'),
    },
    'vanilla_mcdoc.world.component.predicate.WritableBookPredicate': {
        'CollectionPredicate': ('vanilla_mcdoc.world.component.predicate.CollectionPredicate', 'CollectionPredicate'),
    },
    'vanilla_mcdoc.world.component.predicate.WrittenBookPredicate': {
        'CollectionPredicate': ('vanilla_mcdoc.world.component.predicate.CollectionPredicate', 'CollectionPredicate'),
        'MinMaxBounds': ('vanilla_mcdoc.data.util.MinMaxBounds', 'MinMaxBounds'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.entity.EntityBase': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
        'CustomData': ('vanilla_mcdoc.world.component.CustomData', 'CustomData'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.entity.area_effect_cloud.AreaEffectCloud': {
        'Particle': ('vanilla_mcdoc.util.particle.Particle', 'Particle'),
        'PotionContents': ('vanilla_mcdoc.world.component.item.PotionContents', 'PotionContents'),
    },
    'vanilla_mcdoc.world.entity.boat.ChestBoat': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.entity.cushion.Cushion': {
        'DyeColor': ('vanilla_mcdoc.util.color.DyeColor', 'DyeColor'),
    },
    'vanilla_mcdoc.world.entity.display.BlockDisplay': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.world.entity.display.DecomposedTransformation': {
        'Rotation': ('vanilla_mcdoc.world.entity.display.Rotation', 'Rotation'),
    },
    'vanilla_mcdoc.world.entity.display.DisplayBase': {
        'Billboard': ('vanilla_mcdoc.world.entity.display.Billboard', 'Billboard'),
        'Brightness': ('vanilla_mcdoc.world.entity.display.Brightness', 'Brightness'),
        'Transformation': ('vanilla_mcdoc.world.entity.display.Transformation', 'Transformation'),
    },
    'vanilla_mcdoc.world.entity.display.ItemDisplay': {
        'ItemDisplayContext': ('vanilla_mcdoc.assets.model.ItemDisplayContext', 'ItemDisplayContext'),
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.display.Rotation': {
        'AxisAngle': ('vanilla_mcdoc.world.entity.display.AxisAngle', 'AxisAngle'),
    },
    'vanilla_mcdoc.world.entity.display.TextDisplay': {
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
        'TextAlignment': ('vanilla_mcdoc.world.entity.display.TextAlignment', 'TextAlignment'),
    },
    'vanilla_mcdoc.world.entity.display.Transformation': {
        'Rotation': ('vanilla_mcdoc.world.entity.display.Rotation', 'Rotation'),
    },
    'vanilla_mcdoc.world.entity.eye_of_ender.EyeOfEnder': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.falling_block.FallingBlock': {
        'BlockState': ('vanilla_mcdoc.util.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.world.entity.interaction.Interaction': {
        'Action': ('vanilla_mcdoc.world.entity.interaction.Action', 'Action'),
    },
    'vanilla_mcdoc.world.entity.item.Item': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.item_frame.ItemFrame': {
        'DirectionByte': ('vanilla_mcdoc.util.direction.DirectionByte', 'DirectionByte'),
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.minecart.ChestMinecart': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.entity.minecart.HopperMinecart': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.entity.minecart.Minecart': {
        'BlockState': ('vanilla_mcdoc.util.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.world.entity.minecart.SpawnerMinecart': {
        'SpawnPotential': ('vanilla_mcdoc.world.block.spawner.SpawnPotential', 'SpawnPotential'),
        'SpawnerEntry': ('vanilla_mcdoc.world.block.spawner.SpawnerEntry', 'SpawnerEntry'),
    },
    'vanilla_mcdoc.world.entity.mob.Attribute': {
        'AttributeModifier': ('vanilla_mcdoc.world.entity.mob.AttributeModifier', 'AttributeModifier'),
    },
    'vanilla_mcdoc.world.entity.mob.AttributeModifier': {
        'AttributeOperation': ('vanilla_mcdoc.util.attribute.AttributeOperation', 'AttributeOperation'),
    },
    'vanilla_mcdoc.world.entity.mob.Brain': {
        'Memories': ('vanilla_mcdoc.util.memory.Memories', 'Memories'),
    },
    'vanilla_mcdoc.world.entity.mob.DropChances': {
        'EquipmentSlot': ('vanilla_mcdoc.util.slot.EquipmentSlot', 'EquipmentSlot'),
    },
    'vanilla_mcdoc.world.entity.mob.EntityEquipment': {
        'EquipmentSlot': ('vanilla_mcdoc.util.slot.EquipmentSlot', 'EquipmentSlot'),
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.mob.LivingEntity': {
        'Attribute': ('vanilla_mcdoc.world.entity.mob.Attribute', 'Attribute'),
        'Memories': ('vanilla_mcdoc.util.memory.Memories', 'Memories'),
        'MobEffectInstance': ('vanilla_mcdoc.util.effect.MobEffectInstance', 'MobEffectInstance'),
        'WaypointIcon': ('vanilla_mcdoc.world.entity.mob.WaypointIcon', 'WaypointIcon'),
    },
    'vanilla_mcdoc.world.entity.mob.MobBase': {
        'DropChances': ('vanilla_mcdoc.world.entity.mob.DropChances', 'DropChances'),
        'EntityEquipment': ('vanilla_mcdoc.world.entity.mob.EntityEquipment', 'EntityEquipment'),
    },
    'vanilla_mcdoc.world.entity.mob.ModernAttributeModifier': {
        'AttributeOperation': ('vanilla_mcdoc.util.attribute.AttributeOperation', 'AttributeOperation'),
    },
    'vanilla_mcdoc.world.entity.mob.WaypointIcon': {
        'RGB': ('vanilla_mcdoc.util.color.RGB', 'RGB'),
    },
    'vanilla_mcdoc.world.entity.mob.allay.Allay': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
        'VibrationListener': ('vanilla_mcdoc.util.game_event.VibrationListener', 'VibrationListener'),
    },
    'vanilla_mcdoc.world.entity.mob.armor_stand.ArmorStand': {
        'EntityEquipment': ('vanilla_mcdoc.world.entity.mob.EntityEquipment', 'EntityEquipment'),
        'Pose': ('vanilla_mcdoc.world.entity.mob.armor_stand.Pose', 'Pose'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.armadillo.Armadillo': {
        'ArmadilloState': ('vanilla_mcdoc.world.entity.mob.breedable.armadillo.ArmadilloState', 'ArmadilloState'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.axolotl.Axolotl': {
        'AxolotlVariantInt': ('vanilla_mcdoc.world.entity.mob.breedable.axolotl.AxolotlVariantInt', 'AxolotlVariantInt'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.fox.Fox': {
        'FoxType': ('vanilla_mcdoc.world.component.entity.FoxType', 'FoxType'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.horse.ChestedHorse': {
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.horse.Horse': {
        'HorseVariantAndMarkings': ('vanilla_mcdoc.world.entity.mob.breedable.horse.HorseVariantAndMarkings', 'HorseVariantAndMarkings'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.horse.Llama': {
        'LlamaVariantInt': ('vanilla_mcdoc.world.entity.mob.breedable.horse.LlamaVariantInt', 'LlamaVariantInt'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.mooshroom.Mooshroom': {
        'MooshroomType': ('vanilla_mcdoc.world.component.entity.MooshroomType', 'MooshroomType'),
        'SuspiciousStewEffect': ('vanilla_mcdoc.world.component.item.SuspiciousStewEffect', 'SuspiciousStewEffect'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.panda.Panda': {
        'Gene': ('vanilla_mcdoc.world.entity.mob.breedable.panda.Gene', 'Gene'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.rabbit.Rabbit': {
        'RabbitType': ('vanilla_mcdoc.world.entity.mob.breedable.rabbit.RabbitType', 'RabbitType'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.sheep.Sheep': {
        'DyeColorByte': ('vanilla_mcdoc.util.DyeColorByte', 'DyeColorByte'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.tamable.Cat': {
        'DyeColorByte': ('vanilla_mcdoc.util.DyeColorByte', 'DyeColorByte'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.tamable.Parrot': {
        'ParrotVariantInt': ('vanilla_mcdoc.world.entity.mob.breedable.tamable.ParrotVariantInt', 'ParrotVariantInt'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.tamable.Wolf': {
        'DyeColorByte': ('vanilla_mcdoc.util.DyeColorByte', 'DyeColorByte'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.villager.Offers': {
        'Recipe': ('vanilla_mcdoc.world.entity.mob.breedable.villager.Recipe', 'Recipe'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.villager.PlayerReputationPart': {
        'ReputationPart': ('vanilla_mcdoc.world.entity.mob.breedable.villager.ReputationPart', 'ReputationPart'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.villager.Recipe': {
        'ItemCost': ('vanilla_mcdoc.world.entity.mob.breedable.villager.ItemCost', 'ItemCost'),
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.villager.Villager': {
        'PlayerReputationPart': ('vanilla_mcdoc.world.entity.mob.breedable.villager.PlayerReputationPart', 'PlayerReputationPart'),
        'VillagerData': ('vanilla_mcdoc.world.entity.mob.breedable.villager.VillagerData', 'VillagerData'),
    },
    'vanilla_mcdoc.world.entity.mob.breedable.villager.VillagerBase': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
        'Offers': ('vanilla_mcdoc.world.entity.mob.breedable.villager.Offers', 'Offers'),
    },
    'vanilla_mcdoc.world.entity.mob.copper_golem.CopperGolem': {
        'WeatherState': ('vanilla_mcdoc.world.entity.mob.copper_golem.WeatherState', 'WeatherState'),
    },
    'vanilla_mcdoc.world.entity.mob.ender_dragon.EnderDragon': {
        'DragonPhase': ('vanilla_mcdoc.world.entity.mob.ender_dragon.DragonPhase', 'DragonPhase'),
    },
    'vanilla_mcdoc.world.entity.mob.enderman.Enderman': {
        'BlockState': ('vanilla_mcdoc.util.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.world.entity.mob.fish.Pufferfish': {
        'PuffState': ('vanilla_mcdoc.world.entity.mob.fish.PuffState', 'PuffState'),
    },
    'vanilla_mcdoc.world.entity.mob.fish.Salmon': {
        'SalmonType': ('vanilla_mcdoc.world.component.entity.SalmonType', 'SalmonType'),
    },
    'vanilla_mcdoc.world.entity.mob.mannequin.Mannequin': {
        'EntityEquipment': ('vanilla_mcdoc.world.entity.mob.EntityEquipment', 'EntityEquipment'),
        'HumanoidArm': ('vanilla_mcdoc.util.avatar.HumanoidArm', 'HumanoidArm'),
        'MannequinPose': ('vanilla_mcdoc.world.entity.mob.mannequin.MannequinPose', 'MannequinPose'),
        'PlayerModelPart': ('vanilla_mcdoc.util.avatar.PlayerModelPart', 'PlayerModelPart'),
        'Profile': ('vanilla_mcdoc.util.avatar.Profile', 'Profile'),
        'Text': ('vanilla_mcdoc.util.text.Text', 'Text'),
    },
    'vanilla_mcdoc.world.entity.mob.piglin.Piglin': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.mob.player.Player': {
        'Abilities': ('vanilla_mcdoc.world.entity.mob.player.Abilities', 'Abilities'),
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
        'EnderPearl': ('vanilla_mcdoc.world.entity.mob.player.EnderPearl', 'EnderPearl'),
        'Gamemode': ('vanilla_mcdoc.world.entity.mob.player.Gamemode', 'Gamemode'),
        'GlobalPos': ('vanilla_mcdoc.util.GlobalPos', 'GlobalPos'),
        'PlayerEquipment': ('vanilla_mcdoc.world.entity.mob.player.PlayerEquipment', 'PlayerEquipment'),
        'PlayerSlot': ('vanilla_mcdoc.world.entity.mob.player.PlayerSlot', 'PlayerSlot'),
        'RecipeBook': ('vanilla_mcdoc.world.entity.mob.player.RecipeBook', 'RecipeBook'),
        'Respawn': ('vanilla_mcdoc.world.entity.mob.player.Respawn', 'Respawn'),
        'RootVehicle': ('vanilla_mcdoc.world.entity.mob.player.RootVehicle', 'RootVehicle'),
        'SlottedItem': ('vanilla_mcdoc.util.slot.SlottedItem', 'SlottedItem'),
        'WardenSpawnTracker': ('vanilla_mcdoc.world.entity.mob.player.WardenSpawnTracker', 'WardenSpawnTracker'),
    },
    'vanilla_mcdoc.world.entity.mob.player.PlayerEquipment': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
        'PlayerEquipmentSlot': ('vanilla_mcdoc.world.entity.mob.player.PlayerEquipmentSlot', 'PlayerEquipmentSlot'),
    },
    'vanilla_mcdoc.world.entity.mob.player.RootVehicle': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
    },
    'vanilla_mcdoc.world.entity.mob.raider.Pillager': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.mob.shulker.Shulker': {
        'DirectionByte': ('vanilla_mcdoc.util.direction.DirectionByte', 'DirectionByte'),
        'DyeColorByte': ('vanilla_mcdoc.util.color.DyeColorByte', 'DyeColorByte'),
        'ShulkerColor': ('vanilla_mcdoc.world.entity.mob.shulker.ShulkerColor', 'ShulkerColor'),
    },
    'vanilla_mcdoc.world.entity.mob.warden.AngerManagement': {
        'Suspect': ('vanilla_mcdoc.world.entity.mob.warden.Suspect', 'Suspect'),
    },
    'vanilla_mcdoc.world.entity.mob.warden.Warden': {
        'AngerManagement': ('vanilla_mcdoc.world.entity.mob.warden.AngerManagement', 'AngerManagement'),
        'VibrationListener': ('vanilla_mcdoc.util.game_event.VibrationListener', 'VibrationListener'),
    },
    'vanilla_mcdoc.world.entity.mob.zombie.ZombieVillager': {
        'Offers': ('vanilla_mcdoc.world.entity.mob.breedable.villager.Offers', 'Offers'),
        'PlayerReputationPart': ('vanilla_mcdoc.world.entity.mob.breedable.villager.PlayerReputationPart', 'PlayerReputationPart'),
        'VillagerData': ('vanilla_mcdoc.world.entity.mob.breedable.villager.VillagerData', 'VillagerData'),
    },
    'vanilla_mcdoc.world.entity.ominous_item_spawner.OminousItemSpawner': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.painting.Painting': {
        'HorizontalDirectionByte': ('vanilla_mcdoc.util.direction.HorizontalDirectionByte', 'HorizontalDirectionByte'),
    },
    'vanilla_mcdoc.world.entity.projectile.ProjectileBase': {
        'AdventureModePredicate': ('vanilla_mcdoc.world.component.item.AdventureModePredicate', 'AdventureModePredicate'),
    },
    'vanilla_mcdoc.world.entity.projectile.arrow.ArrowBase': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
        'Pickup': ('vanilla_mcdoc.world.entity.projectile.arrow.Pickup', 'Pickup'),
    },
    'vanilla_mcdoc.world.entity.projectile.fireball.FireballBase': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.projectile.firework_rocket.FireWorkRocket': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.projectile.shulker_bullet.ShulkerBullet': {
        'BulletTarget': ('vanilla_mcdoc.world.entity.projectile.shulker_bullet.BulletTarget', 'BulletTarget'),
        'DirectionByte': ('vanilla_mcdoc.util.direction.DirectionByte', 'DirectionByte'),
    },
    'vanilla_mcdoc.world.entity.projectile.throwable.Potion': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.projectile.throwable.ThrowableItem': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.entity.tnt.Tnt': {
        'BlockState': ('vanilla_mcdoc.util.block_state.BlockState', 'BlockState'),
    },
    'vanilla_mcdoc.world.item.AttributeModifier': {
        'EquipmentSlotGroup': ('vanilla_mcdoc.util.slot.EquipmentSlotGroup', 'EquipmentSlotGroup'),
        'LegacyOperation': ('vanilla_mcdoc.util.attribute.LegacyOperation', 'LegacyOperation'),
    },
    'vanilla_mcdoc.world.item.BlockItem': {
        'BlockEntityData': ('vanilla_mcdoc.world.block.BlockEntityData', 'BlockEntityData'),
    },
    'vanilla_mcdoc.world.item.ItemBase': {
        'AttributeModifier': ('vanilla_mcdoc.world.item.AttributeModifier', 'AttributeModifier'),
        'Display': ('vanilla_mcdoc.world.item.Display', 'Display'),
        'Enchantment': ('vanilla_mcdoc.world.item.Enchantment', 'Enchantment'),
        'Trim': ('vanilla_mcdoc.world.component.item.Trim', 'Trim'),
    },
    'vanilla_mcdoc.world.item.ItemStackTemplate': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.item.book.WrittenBook': {
        'BookGeneration': ('vanilla_mcdoc.world.component.item.BookGeneration', 'BookGeneration'),
        'Filterable': ('vanilla_mcdoc.util.Filterable', 'Filterable'),
    },
    'vanilla_mcdoc.world.item.compass.Compass': {
        'LodestonePos': ('vanilla_mcdoc.world.item.compass.LodestonePos', 'LodestonePos'),
    },
    'vanilla_mcdoc.world.item.crossbow.Crossbow': {
        'ItemStack': ('vanilla_mcdoc.world.item.ItemStack', 'ItemStack'),
    },
    'vanilla_mcdoc.world.item.debug_stick.DebugStick': {
        'DebugStickState': ('vanilla_mcdoc.world.component.item.DebugStickState', 'DebugStickState'),
    },
    'vanilla_mcdoc.world.item.enchanted_book.EnchantedBook': {
        'Enchantment': ('vanilla_mcdoc.world.item.Enchantment', 'Enchantment'),
    },
    'vanilla_mcdoc.world.item.firework.Explosion': {
        'ExplosionType': ('vanilla_mcdoc.world.item.firework.ExplosionType', 'ExplosionType'),
    },
    'vanilla_mcdoc.world.item.firework.FireworkRocket': {
        'Fireworks': ('vanilla_mcdoc.world.item.firework.Fireworks', 'Fireworks'),
    },
    'vanilla_mcdoc.world.item.firework.FireworkStar': {
        'Explosion': ('vanilla_mcdoc.world.item.firework.Explosion', 'Explosion'),
    },
    'vanilla_mcdoc.world.item.firework.Fireworks': {
        'Explosion': ('vanilla_mcdoc.world.item.firework.Explosion', 'Explosion'),
    },
    'vanilla_mcdoc.world.item.fish_bucket.AxolotlBucket': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
    },
    'vanilla_mcdoc.world.item.fish_bucket.BasicFishBucket': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
    },
    'vanilla_mcdoc.world.item.head.PlayerHead': {
        'SkullOwner': ('vanilla_mcdoc.world.block.head.SkullOwner', 'SkullOwner'),
    },
    'vanilla_mcdoc.world.item.leather_armor.LeatherArmor': {
        'ColorDisplay': ('vanilla_mcdoc.world.item.leather_armor.ColorDisplay', 'ColorDisplay'),
    },
    'vanilla_mcdoc.world.item.map.Decoration': {
        'IconByteId': ('vanilla_mcdoc.world.item.map.IconByteId', 'IconByteId'),
    },
    'vanilla_mcdoc.world.item.potion.EffectItem': {
        'MobEffectInstance': ('vanilla_mcdoc.util.effect.MobEffectInstance', 'MobEffectInstance'),
    },
    'vanilla_mcdoc.world.item.shield.BlockEntityTag': {
        'BannerPatternLayer': ('vanilla_mcdoc.world.block.banner.BannerPatternLayer', 'BannerPatternLayer'),
        'DyeColorInt': ('vanilla_mcdoc.util.color.DyeColorInt', 'DyeColorInt'),
    },
    'vanilla_mcdoc.world.item.shield.Shield': {
        'BannerPatternLayer': ('vanilla_mcdoc.world.block.banner.BannerPatternLayer', 'BannerPatternLayer'),
        'DyeColorInt': ('vanilla_mcdoc.util.color.DyeColorInt', 'DyeColorInt'),
    },
    'vanilla_mcdoc.world.item.spawn_item.SpawnItem': {
        'AnyEntity': ('vanilla_mcdoc.world.entity.AnyEntity', 'AnyEntity'),
    },
    'vanilla_mcdoc.world.item.suspicious_stew.Effect': {
        'EffectId': ('vanilla_mcdoc.util.EffectId', 'EffectId'),
    },
    'vanilla_mcdoc.world.item.suspicious_stew.SuspiciousStew': {
        'Effect': ('vanilla_mcdoc.world.item.suspicious_stew.Effect', 'Effect'),
    },
}
