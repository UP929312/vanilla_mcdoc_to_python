"""Vanilla's data/advancement/recipes/ files"""
from vanilla_mcdoc.data.advancement.Advancement import Advancement
from vanilla_mcdoc.data.advancement.AdvancementCriterion import AdvancementCriterionImpossible

ROOT = Advancement(
    criteria={'impossible': AdvancementCriterionImpossible(trigger='minecraft:impossible')},
    requirements=[['impossible']],
)
