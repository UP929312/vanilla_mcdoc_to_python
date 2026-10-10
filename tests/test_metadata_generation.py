from pathlib import Path

from pytest import MonkeyPatch

import minecraft_registry
from code_generation import get_schema_graph, make_init_content, make_python_file_content
from context import SingleSymbolContext
from minecraft_registry import make_registry_id_file_content, make_registry_id_files, make_root_resource_registry_content, used_registry_names
from schema_resolution import SchemaGraph
from static_symbols.minecraft_types import IdSpec
from typed_models import IntSchema, ReferenceSchema, UnionSchema
from utils import LATEST_VERSION, SYMBOLS_MAP


def generated_body(resource_type: str, resource_data: dict[str, object], class_name: str) -> str:
    return make_python_file_content(resource_type, resource_data, class_name).split("\n\n# ~~~ MODEL DUMP ~~~")[0]


class TestIdMetadataGeneration:
    def test_empty_enum_generates_valid_class_body(self) -> None:
        content = generated_body(
            "::test::EmptyEnum",
            {"kind": "enum", "enumKind": "string", "values": []},
            "EmptyEnum",
        )

        assert "class EmptyEnum(StrEnum):\n    pass" in content

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

        assert "from vanilla_mcdoc.minecraft_types import IdSpec" in content
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

        assert "from vanilla_mcdoc.registry.KnownEnvironmentAttributeId import KnownEnvironmentAttributeId" in content
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

        assert spec.to_annotation() == "IdSpec(registry='texture', tags='allowed', definition=True, path='entity/')"

    def test_used_registry_names_are_discovered_from_nested_schemas(self) -> None:
        registries = used_registry_names(get_schema_graph())

        assert "block" in registries
        assert "environment_attribute" in registries

    def test_registry_files_skip_dispatchers_without_public_ids(self, tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
        output_directory = tmp_path / "vanilla_mcdoc"

        def make_directory(path: Path) -> None:
            path.mkdir(parents=True, exist_ok=True)

        def registry_names(_: SchemaGraph) -> set[str]:
            return {"block", "missing"}

        monkeypatch.setattr(minecraft_registry, "GENERATED_SYMBOLS_DIRECTORY", output_directory)
        monkeypatch.setattr(minecraft_registry, "manage_directory_and_inits", make_directory)
        monkeypatch.setattr(minecraft_registry, "used_registry_names", registry_names)
        make_registry_id_files(get_schema_graph())

        block_file = output_directory / "registry" / "KnownBlockId.py"
        assert block_file.exists()
        assert "minecraft:%unknown" not in block_file.read_text(encoding="utf-8")
        assert not (output_directory / "registry" / "KnownMissingId.py").exists()


class TestDispatcherSpreadGeneration:
    def test_reference_dispatcher_branch_reuses_referenced_struct(self) -> None:
        content = generated_body(
            "::java::assets::font::GlyphProvider",
            SYMBOLS_MAP["mcdoc"]["::java::assets::font::GlyphProvider"],
            "GlyphProvider",
        )

        assert "class GlyphProviderSpace(SpaceProvider):" in content
        assert "class GlyphProviderSpace:" not in content
        assert "    advances: dict[" not in content.split("class GlyphProviderSpace(SpaceProvider):", 1)[1].split("\n\n", 1)[0]

    def test_literal_dispatcher_fields_get_defaults(self) -> None:
        content = generated_body(
            "::java::world::block::BlockEntityData",
            SYMBOLS_MAP["mcdoc"]["::java::world::block::BlockEntityData"],
            "BlockEntityData",
        )

        assert "class BlockEntityDataBanner(Banner):" in content
        assert "    id: Literal['minecraft:banner', 'banner'] = 'minecraft:banner'" in content

    def test_optional_literal_dispatcher_fields_keep_valid_annotation_order(self) -> None:
        content = generated_body(
            "::java::data::dialog::ButtonListDialogBase",
            SYMBOLS_MAP["mcdoc"]["::java::data::dialog::ButtonListDialogBase"],
            "ButtonListDialogBase",
        )

        assert "class ButtonListDialogBaseClose(GeneratedModel):" in content
        assert "after_action: Literal['minecraft:close', 'close'] | None = 'minecraft:close'" in content

    def test_dynamic_spread_generates_correlated_branch_classes(self) -> None:
        content = generated_body(
            "::java::data::advancement::AdvancementCriterion",
            SYMBOLS_MAP["mcdoc"]["::java::data::advancement::AdvancementCriterion"],
            "AdvancementCriterion",
        )

        assert "class AdvancementCriterionInventoryChanged(InventoryChangeTrigger):" in content
        assert "trigger: Literal['minecraft:inventory_changed', 'inventory_changed']" in content
        assert "class AdvancementCriterionTick(PlayerTrigger):" in content
        assert "trigger: Literal['minecraft:tick', 'tick']" in content
        assert "type AdvancementCriterion = Annotated[\n    AdvancementCriterionAllayDropItemOnBlock |" in content
        assert "Field(discriminator='trigger')" in content

    def test_union_schema_uses_shared_unique_string_literal_discriminator(self) -> None:
        content = generated_body(
            "::test::TaggedUnion",
            {
                "kind": "union",
                "members": [
                    {"kind": "struct", "fields": [{
                        "kind": "pair",
                        "key": "kind",
                        "type": {"kind": "literal", "value": {"kind": "string", "value": "first"}},
                    }]},
                    {"kind": "struct", "fields": [{
                        "kind": "pair",
                        "key": "kind",
                        "type": {"kind": "literal", "value": {"kind": "string", "value": "second"}},
                    }]},
                ],
            },
            "TaggedUnion",
        )

        assert "Field(discriminator='kind')" in content

    def test_union_without_discriminator_remains_plain_union(self) -> None:
        path = "::java::data::structure::StructureNBT"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "StructureNBT")

        assert "type StructureNBT = StructureNBTStruct1 | StructureNBTStruct2" in content
        assert "Field(discriminator=" not in content

    def test_union_with_unresolved_type_parameter_remains_plain_union(self) -> None:
        context = SingleSymbolContext(schema_graph=get_schema_graph())
        context.local_type_params.add("::test::T")
        schema = UnionSchema(kind="union", members=[
            ReferenceSchema(kind="reference", path="::test::T"),
            IntSchema(kind="int"),
        ])

        assert schema.to_python_code("GenericUnion", context) == ["type GenericUnion = T | int"]

    def test_dynamic_map_branch_does_not_break_distribution(self) -> None:
        content = generated_body(
            "::java::data::advancement::predicate::EntitySubPredicate",
            SYMBOLS_MAP["mcdoc"]["::java::data::advancement::predicate::EntitySubPredicate"],
            "EntitySubPredicate",
        )

        assert "class EntitySubPredicatePredicates(GeneratedModel):" in content
        assert "type: Literal['minecraft:predicates', 'predicates']" in content


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

        assert "from vanilla_mcdoc.data.advancement.Advancement import Advancement" in content
        assert "from vanilla_mcdoc.data.worldgen.DecorationStep import DecorationStep" in content
        assert '"Model",' not in content
        assert '"Entity",' not in content
        assert "from vanilla_mcdoc.data.anonymous.Ignored import Ignored" in content
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

        assert "from vanilla_mcdoc.data.loot.function.Conditions import Conditions" in content
        assert '"Reference",' not in content
        assert '"Advancement",' not in content


class TestRootResourceMetadata:
    def test_root_resource_models_expose_resource_dirs(self) -> None:
        content = generated_body(
            "::java::data::advancement::Advancement",
            SYMBOLS_MAP["mcdoc"]["::java::data::advancement::Advancement"],
            "Advancement",
        )

        assert "__resource_dir__: ClassVar[str] = 'advancement'" in content

    def test_root_resource_aliases_do_not_crash_generation(self) -> None:
        content = generated_body(
            "::java::assets::credits::Credits",
            SYMBOLS_MAP["mcdoc"]["::java::assets::credits::Credits"],
            "Credits",
        )

        assert "type Credits = list[CreditsStruct]" in content
        assert "__resource_dir__" not in content

    def test_recipe_serializer_branches_are_serializable_root_resources(self) -> None:
        content = generated_body(
            "::java::data::recipe::CraftingShaped",
            SYMBOLS_MAP["mcdoc"]["::java::data::recipe::CraftingShaped"],
            "CraftingShaped",
        )

        assert "__resource_dir__: ClassVar[str] = 'recipe'" in content

        registry_content = make_root_resource_registry_content([
            "::java::data::advancement::Advancement",
            "::java::data::recipe::Recipe",
            "::java::data::recipe::CraftingShaped",
            "::java::data::advancement::predicate::FoodPredicate",
        ])
        assert "CraftingShaped" in registry_content
        assert "FoodPredicate" not in registry_content

    def test_generic_sound_variant_template_is_not_a_root_resource(self) -> None:
        lookup = minecraft_registry.get_resource_lookup_map()
        assert lookup.get("::java::data::variants::SoundVariant") is None
        assert lookup.get("::java::data::variants::wolf::WolfSounds") == "wolf_sound_variant"

    def test_root_resource_registry_lists_datapack_and_pack_classes(self) -> None:
        content = make_root_resource_registry_content([
            "::java::data::advancement::Advancement",
            "::java::data::recipe::Recipe",
            "::java::assets::atlas::Atlas",
            "::java::data::advancement::predicate::FoodPredicate",
        ])

        assert "ROOT_DATAPACK_CLASSES" in content
        assert "Advancement" in content
        assert "Recipe" in content
        assert "ROOT_RESOURCE_PACK_CLASSES" in content
        assert "Atlas" in content
        assert "FoodPredicate" not in content


class TestRuntimeImportGeneration:
    def test_concrete_struct_type_argument_is_materialized(self) -> None:
        path = "::java::data::advancement::trigger::AnyBlockInteractionTrigger"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "AnyBlockInteractionTrigger")

        assert "class AnyBlockInteractionTriggerTypeArg(PlayerConditions):" in content
        assert "location: AdvancementLocationPredicate | None = None" in content
        assert "AnyBlockInteractionTrigger = AllOptional[AnyBlockInteractionTriggerTypeArg]" in content

    def test_pydantic_fields_preserve_schema_order(self) -> None:
        path = "::java::data::advancement::Advancement"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "Advancement")
        field_names = ("parent", "display", "criteria", "requirements", "rewards", "sends_telemetry_event")

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

        assert "class InlineStructMapValueStruct(GeneratedModel):" in content
        assert "type InlineStructMap = dict[str, InlineStructMapValueStruct]" in content

    def test_dispatcher_mapping_key_preserves_registry_metadata(self) -> None:
        path = "::java::data::advancement::predicate::BlockPredicateState"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "BlockPredicateState")

        assert "from typing import TYPE_CHECKING, Annotated" in content
        assert "type BlockPredicateState = dict[Annotated[str, 'Registry(\"block_state_keys\")'], MinMaxBounds[str]]" in content

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
        assert schema.to_python_code("CurrentValue", SingleSymbolContext(current_symbol_path="CurrentValue", schema_graph=get_schema_graph())) == [
            "type CurrentValue = int",
        ]

    def test_concrete_alias_dependencies_are_runtime_imports(self) -> None:
        path = "::java::data::worldgen::attribute::GlobalEnvironmentAttributeMap"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "GlobalEnvironmentAttributeMap")

        runtime_import = "from vanilla_mcdoc.data.worldgen.attribute.EnvironmentAttributeMap import EnvironmentAttributeMap"
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

        assert "class FlatWeightedEntry(GeneratedModel, Generic[T]):" in content
        assert "type FlatWeightedEntry =" not in content

    def test_alias_spread_is_distributed(self) -> None:
        path = "::java::data::loot::function::CustomModelDataFlags"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "CustomModelDataFlags")

        assert "class CustomModelDataFlagsAppend(GeneratedModel):" in content
        assert "class CustomModelDataFlags(ListOperation):" not in content

    def test_union_alias_spread_is_distributed(self) -> None:
        path = "::java::data::structure::StructureNBT"
        content = generated_body(path, SYMBOLS_MAP["mcdoc"][path], "StructureNBT")

        assert "class StructureNBTStruct1(GeneratedModel):" in content
        assert "class StructureNBTStruct2(GeneratedModel):" in content
        assert "type StructureNBT = StructureNBTStruct1 | StructureNBTStruct2" in content

    def test_generated_declaration_names_are_unique(self) -> None:
        dialog_path = "::java::data::dialog::Dialog"
        dialog = generated_body(dialog_path, SYMBOLS_MAP["mcdoc"][dialog_path], "Dialog")
        assert "class DialogConfirmationNone2(GeneratedModel):" in dialog

        timeline_path = "::java::data::timeline::EnvironmentAttributeTrackMap"
        timeline = generated_body(timeline_path, SYMBOLS_MAP["mcdoc"][timeline_path], "EnvironmentAttributeTrackMap")
        assert timeline.count("class KeyframesStruct(GeneratedModel):") == 1
        assert "class KeyframesStruct2(GeneratedModel):" in timeline

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
        assert "class LootFunctionCopyCustomData(CopyNbt):" in loot
