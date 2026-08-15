from pathlib import Path

import minecraft_registry
from pytest import MonkeyPatch

from code_generation import SCHEMA_GRAPH, make_init_content, make_python_file_content
from context import SingleSymbolContext
from minecraft_registry import IdSpec, make_registry_id_file_content, make_registry_id_files, used_registry_names
from schema_resolution import SchemaGraph
from typed_models import IntSchema, UnionSchema
from utils import LATEST_VERSION, SYMBOLS_MAP


def generated_body(resource_type: str, resource_data: dict[str, object], class_name: str) -> str:
    return make_python_file_content(resource_type, resource_data, class_name).split("\n\n# ~~~ MODEL DUMP ~~~")[0]


class TestIdMetadataGeneration:
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

        assert "from minecraft_registry import IdSpec" in content
        assert "type ItemId = Annotated[str, IdSpec(registry='item')] | KnownItemId" in content

    def test_bare_id_attribute(self) -> None:
        content = generated_body(
            "::test::ResourceId",
            {"kind": "string", "attributes": [{"name": "id"}]},
            "ResourceId",
        )

        assert "type ResourceId = Annotated[str, IdSpec()]" in content

    def test_tree_id_attribute_with_exclusions(self) -> None:
        content = generated_body(
            "::java::assets::model::ModelRef",
            SYMBOLS_MAP["mcdoc"]["::java::assets::model::ModelRef"],
            "ModelRef",
        )

        assert "IdSpec(registry='model', exclude=('builtin/generated', 'builtin/entity'))" in content

    def test_known_registry_ids_are_suggested_with_open_string_fallback(self) -> None:
        path = "::java::data::loot::condition::EnvironmentAttributeCheck"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "EnvironmentAttributeCheck")

        assert "from generated_symbols.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId" in content
        assert "attribute: Annotated[str, IdSpec(registry='environment_attribute')] | KnownEnvironmentAttributeId" in content

        registry_content = make_registry_id_file_content("environment_attribute", [
            "%unknown",
            "gameplay/creaking_active",
            "gameplay/creature_world_gen_spawn_probability",
        ])
        assert "'minecraft:gameplay/creaking_active'" in registry_content
        assert "'minecraft:gameplay/creature_world_gen_spawn_probability'" in registry_content
        assert "minecraft:%unknown" not in registry_content

    def test_id_spec_renders_only_non_default_options(self) -> None:
        spec = IdSpec(registry="texture", tags="allowed", definition=True, path="entity/")

        assert spec.to_python_code() == "IdSpec(registry='texture', tags='allowed', definition=True, path='entity/')"

    def test_used_registry_names_are_discovered_from_nested_schemas(self) -> None:
        registries = used_registry_names(SCHEMA_GRAPH)

        assert "block" in registries
        assert "environment_attribute" in registries

    def test_registry_files_skip_dispatchers_without_public_ids(self, tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
        output_directory = tmp_path / "generated_symbols"

        def make_directory(path: Path) -> None:
            path.mkdir(parents=True, exist_ok=True)

        def registry_names(_: SchemaGraph) -> set[str]:
            return {"block", "missing"}

        monkeypatch.setattr(minecraft_registry, "GENERATED_SYMBOLS_DIRECTORY", output_directory)
        monkeypatch.setattr(minecraft_registry, "manage_directory_and_inits", make_directory)
        monkeypatch.setattr(minecraft_registry, "used_registry_names", registry_names)
        make_registry_id_files(SCHEMA_GRAPH)

        block_file = output_directory / "registry" / "KnownBlockId.py"
        assert block_file.exists()
        assert "minecraft:%unknown" not in block_file.read_text(encoding="utf-8")
        assert not (output_directory / "registry" / "KnownMissingId.py").exists()


class TestDispatcherSpreadGeneration:
    def test_dynamic_spread_generates_correlated_branch_classes(self) -> None:
        content = generated_body(
            "::java::data::advancement::AdvancementCriterion",
            SYMBOLS_MAP["mcdoc"]["::java::data::advancement::AdvancementCriterion"],
            "AdvancementCriterion",
        )

        assert "class AdvancementCriterionInventoryChanged:" in content
        assert "trigger: Literal['minecraft:inventory_changed']" in content
        assert "conditions: InventoryChanged | None = None" in content
        assert "class AdvancementCriterionTick:" in content
        assert "trigger: Literal['minecraft:tick']" in content
        assert "conditions: TriggerBase | None = None" in content
        assert "type AdvancementCriterion = AdvancementCriterionAllayDropItemOnBlock |" in content

    def test_dynamic_map_branch_does_not_break_distribution(self) -> None:
        content = generated_body(
            "::java::data::advancement::predicate::EntitySubPredicate",
            SYMBOLS_MAP["mcdoc"]["::java::data::advancement::predicate::EntitySubPredicate"],
            "EntitySubPredicate",
        )

        assert "class EntitySubPredicatePredicates:" in content
        assert "type: Literal['minecraft:predicates']" in content


class TestRootExportGeneration:
    def test_data_facade_exports_unique_symbols_from_complete_tree(self) -> None:
        content = make_init_content([
            "::java::data::advancement::Advancement",
            "::java::data::loot::function::Conditions",
            "::java::data::advancement::trigger::Conditions",
            "::java::data::worldgen::DecorationStep",
            "::java::assets::model::Model",
            "::java::world::entity::Entity",
            "::java::data::anonymous::Ignored",
        ], ("::java::data::",))

        assert "from generated_symbols.data.advancement.Advancement import Advancement" in content
        assert "from generated_symbols.data.worldgen.DecorationStep import DecorationStep" in content
        assert '"Model",' not in content
        assert '"Entity",' not in content
        assert "from generated_symbols.data.anonymous.Ignored import Ignored" in content
        assert '"Conditions",' not in content
        assert "import_module" not in content
        assert "def __getattr__" not in content

    def test_nested_facade_exports_unique_symbols_from_its_tree(self) -> None:
        content = make_init_content([
            "::java::data::loot::function::Conditions",
            "::java::data::loot::function::Reference",
            "::java::data::loot::condition::Reference",
            "::java::data::advancement::Advancement",
        ], ("::java::data::loot::",))

        assert "from generated_symbols.data.loot.function.Conditions import Conditions" in content
        assert '"Reference",' not in content
        assert '"Advancement",' not in content


class TestRuntimeImportGeneration:
    def test_dataclass_fields_preserve_schema_order(self) -> None:
        path = "::java::data::advancement::Advancement"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "Advancement")
        field_names = ("display", "parent", "criteria", "requirements", "rewards", "sends_telemetry_event")

        positions = [content.index(f"    {name}:") for name in field_names]
        assert positions == sorted(positions)

    def test_mapping_struct_materializes_inline_struct_values(self) -> None:
        content = generated_body(
            "::test::InlineStructMap",
            {
                "kind": "struct",
                "fields": [{
                    "kind": "pair",
                    "key": {"kind": "string"},
                    "type": {
                        "kind": "struct",
                        "fields": [{"kind": "pair", "key": "value", "type": {"kind": "int"}}],
                    },
                }],
            },
            "InlineStructMap",
        )

        assert "class InlineStructMapValueStruct:" in content
        assert "type InlineStructMap = dict[str, InlineStructMapValueStruct]" in content

    def test_discarded_spread_annotations_do_not_add_any_import(self) -> None:
        path = "::java::data::worldgen::processor_list::AppendStatic"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "AppendStatic")

        assert "from typing import Any" not in content
        assert ", Any" not in content

    def test_versioned_union_delegates_to_retained_member(self) -> None:
        version_value = {"kind": "literal", "value": {"kind": "string", "value": LATEST_VERSION}}
        schema = UnionSchema.model_validate({
            "kind": "union",
            "members": [
                {"kind": "int", "attributes": [{"name": "since", "value": version_value}]},
                {"kind": "string", "attributes": [{"name": "until", "value": version_value}]},
            ],
        })

        assert len(schema.members) == 1
        assert isinstance(schema.members[0], IntSchema)
        assert schema.to_python_code("CurrentValue", SingleSymbolContext()) == ["type CurrentValue = int"]

    def test_concrete_alias_dependencies_are_runtime_imports(self) -> None:
        path = "::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "GlobalEnvironmentAttributeMap")

        runtime_import = "from generated_symbols.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap"
        assert runtime_import in content
        assert f"if TYPE_CHECKING:\n    {runtime_import}" not in content

    def test_duplicate_type_parameter_names_are_rendered_once(self) -> None:
        path = "::java::data::worldgen::attribute::FloatAttribute"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "FloatAttribute")

        assert content.count("T = TypeVar('T')") == 1
        assert "Generic[T, T]" not in content
        assert "[T, T]" not in content

    def test_local_type_parameter_spread_remains_a_class(self) -> None:
        path = "::java::util::FlatWeightedEntry"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "FlatWeightedEntry")

        assert "class FlatWeightedEntry(Generic[T]):" in content
        assert "type FlatWeightedEntry =" not in content

    def test_alias_spread_is_distributed(self) -> None:
        path = "::java::data::loot::function::CustomModelDataFlags"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "CustomModelDataFlags")

        assert "class CustomModelDataFlagsAppend:" in content
        assert "class CustomModelDataFlags(ListOperation):" not in content

    def test_union_alias_spread_is_distributed(self) -> None:
        path = "::java::data::structure::StructureNBT"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "StructureNBT")

        assert "class StructureNBTStruct1:" in content
        assert "class StructureNBTStruct2:" in content
        assert "type StructureNBT = StructureNBTStruct1 | StructureNBTStruct2" in content

    def test_generated_declaration_names_are_unique(self) -> None:
        dialog_path = "::java::data::dialog::Dialog"
        dialog = generated_body(dialog_path, SYMBOLS_MAP["mcdoc"][dialog_path], "Dialog")
        assert "class DialogConfirmationNone2:" in dialog

        timeline_path = "::java::data::timeline::EnvironmentAttributeTrackMap"
        timeline = generated_body(timeline_path, SYMBOLS_MAP["mcdoc"][timeline_path], "EnvironmentAttributeTrackMap")
        assert timeline.count("class KeyframesStruct:") == 1
        assert "class KeyframesStruct2:" in timeline

    def test_concrete_dispatcher_instantiates_template_branches(self) -> None:
        path = "::java::data::worldgen::attribute::FloatAttribute"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "FloatAttribute")

        assert "FloatWithAlpha[T]" not in content

    def test_import_and_field_names_do_not_shadow(self) -> None:
        structure_path = "::java::data::structure::StructureBlock"
        structure = generated_body(structure_path, SYMBOLS_MAP["mcdoc"][structure_path], "StructureBlock")
        assert "StructureBlock as StructureBlock2" in structure

        loot_path = "::java::data::loot::function::LootFunction"
        loot = generated_body(loot_path, SYMBOLS_MAP["mcdoc"][loot_path], "LootFunction")
        assert "type_2: Annotated[str, IdSpec(registry='block_entity_type')]" in loot