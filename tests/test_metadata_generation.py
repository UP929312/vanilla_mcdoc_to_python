import unittest

from code_generation import make_python_file_content
from runtime_metadata import IdSpec
from utils import SYMBOLS_MAP


def generated_body(resource_type: str, resource_data: dict[str, object], class_name: str) -> str:
    return make_python_file_content(resource_type, resource_data, class_name).split("\n\n# ~~~ MODEL DUMP ~~~")[0]


class IdMetadataGenerationTests(unittest.TestCase):
    def test_literal_id_attribute(self) -> None:
        content = generated_body(
            "::test::ItemId",
            {
                "kind": "string",
                "attributes": [{
                    "name": "id",
                    "value": {"kind": "literal", "value": {"kind": "string", "value": "item"}},
                }],
            },
            "ItemId",
        )

        self.assertIn("from runtime_metadata import IdSpec", content)
        self.assertIn("type ItemId = Annotated[str, IdSpec(registry='item')]", content)

    def test_bare_id_attribute(self) -> None:
        content = generated_body(
            "::test::ResourceId",
            {"kind": "string", "attributes": [{"name": "id"}]},
            "ResourceId",
        )

        self.assertIn("type ResourceId = Annotated[str, IdSpec()]", content)

    def test_tree_id_attribute_with_exclusions(self) -> None:
        content = generated_body(
            "::java::assets::model::ModelRef",
            SYMBOLS_MAP["mcdoc"]["::java::assets::model::ModelRef"],
            "ModelRef",
        )

        self.assertIn(
            "IdSpec(registry='model', exclude=('builtin/generated', 'builtin/entity'))",
            content,
        )

    def test_id_spec_renders_only_non_default_options(self) -> None:
        spec = IdSpec(registry="texture", tags="allowed", definition=True, path="entity/")

        self.assertEqual(
            spec.to_python_code(),
            "IdSpec(registry='texture', tags='allowed', definition=True, path='entity/')",
        )


class DispatcherSpreadGenerationTests(unittest.TestCase):
    def test_dynamic_spread_generates_correlated_branch_classes(self) -> None:
        content = generated_body(
            "::java::data::advancement::AdvancementCriterion",
            SYMBOLS_MAP["mcdoc"]["::java::data::advancement::AdvancementCriterion"],
            "AdvancementCriterion",
        )

        self.assertIn("class AdvancementCriterionInventoryChanged:", content)
        self.assertIn("trigger: Literal['minecraft:inventory_changed']", content)
        self.assertIn("conditions: InventoryChanged | None = None", content)
        self.assertIn("class AdvancementCriterionTick:", content)
        self.assertIn("trigger: Literal['minecraft:tick']", content)
        self.assertIn("conditions: TriggerBase | None = None", content)
        self.assertIn("type AdvancementCriterion = AdvancementCriterionAllayDropItemOnBlock |", content)

    def test_dynamic_map_branch_does_not_break_distribution(self) -> None:
        content = generated_body(
            "::java::data::advancement::predicate::EntitySubPredicate",
            SYMBOLS_MAP["mcdoc"]["::java::data::advancement::predicate::EntitySubPredicate"],
            "EntitySubPredicate",
        )

        self.assertIn("class EntitySubPredicatePredicates:", content)
        self.assertIn("type: Literal['minecraft:predicates']", content)

if __name__ == "__main__":
    unittest.main()