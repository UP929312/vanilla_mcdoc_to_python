from typing import cast

import pytest

from context import SingleSymbolContext
from schema_resolution import SchemaGraph
from typed_models import (
    DispatcherSchema,
    FloatSchema,
    IndexedSchema,
    PairSchema,
    ReferenceSchema,
    SpreadFieldSchema,
    StringSchema,
    StructSchema,
)
from utils import SYMBOLS_MAP


@pytest.fixture(scope="module")
def graph() -> SchemaGraph:
    return SchemaGraph.from_symbol_maps(SYMBOLS_MAP)


def test_dynamic_dispatcher_candidates_from_sprite_source(graph: SchemaGraph) -> None:
    path = "::java::assets::atlas::SpriteSource"
    schema = cast(StructSchema, graph.symbols[path])
    spread = next(field for field in schema.fields if isinstance(field, SpreadFieldSchema))
    assert isinstance(spread.type, DispatcherSchema)

    candidates = graph.annotation_candidates(spread.type)

    assert all(isinstance(candidate, ReferenceSchema) for candidate in candidates)
    assert [
        candidate.path.rsplit("::", 1)[-1]
        for candidate in candidates
        if isinstance(candidate, ReferenceSchema)
    ] == [
        "Directory",
        "Filter",
        "PalettedPermutations",
        "Single",
        "Unstitch",
    ]


def test_dynamic_dispatcher_annotation_uses_generation_context(graph: SchemaGraph) -> None:
    path = "::java::assets::atlas::SpriteSource"
    schema = cast(StructSchema, graph.symbols[path])
    spread = next(field for field in schema.fields if isinstance(field, SpreadFieldSchema))
    assert isinstance(spread.type, DispatcherSchema)
    ctx = SingleSymbolContext(current_symbol_path=path, schema_graph=graph)

    annotation = spread.type.to_annotation(ctx, "SpriteSource")

    assert annotation == "Directory | Filter | PalettedPermutations | Single | Unstitch"


def test_fallback_dispatcher_resolves_all_registry_candidates(graph: SchemaGraph) -> None:
    path = "::java::assets::item_definition::BlockState"
    schema = cast(StructSchema, graph.symbols[path])
    field = next(field for field in schema.fields if isinstance(field, PairSchema))
    assert isinstance(field.type, DispatcherSchema)

    candidates = graph.annotation_candidates(field.type)

    assert len(candidates) == 1
    assert isinstance(candidates[0], StringSchema)
    ctx = SingleSymbolContext(current_symbol_path=path, schema_graph=graph)
    assert field.type.to_annotation(ctx) == "str"


def test_real_reference_resolution(graph: SchemaGraph) -> None:
    reference = graph.symbols["::java::data::loot::LootCondition"]
    assert isinstance(reference, ReferenceSchema)

    resolved = graph.resolve(reference)

    assert len(resolved) == 1
    assert not isinstance(resolved[0], ReferenceSchema)


def test_real_dynamic_dispatch_and_template_index(graph: SchemaGraph) -> None:
    path = "::java::data::loot::condition::EnvironmentAttributeCheck"
    schema = cast(StructSchema, graph.symbols[path])
    value_field = next(
        field
        for field in schema.fields
        if isinstance(field, PairSchema) and field.key == "value"
    )
    assert isinstance(value_field.type, IndexedSchema)

    candidates = graph.annotation_candidates(value_field.type)

    assert any(isinstance(candidate, FloatSchema) for candidate in candidates)
