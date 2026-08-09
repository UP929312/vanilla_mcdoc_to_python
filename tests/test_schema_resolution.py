import unittest
from typing import cast

from schema_resolution import SchemaGraph
from typed_models import BooleanSchema, DispatcherSchema, FloatSchema, IndexedSchema, IntSchema, PairSchema, RenderContext, StringSchema, StructSchema
from utils import SYMBOLS_MAP


class SchemaResolutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = SchemaGraph.from_symbol_maps({
            "mcdoc": {
                "::test::Alias": {"kind": "reference", "path": "::test::Number"},
                "::test::Number": {"kind": "int"},
            },
            "mcdoc/dispatcher": {
                "test:kind": {
                    "%none": {"kind": "string"},
                    "%unknown": {"kind": "any"},
                    "number": {
                        "kind": "struct",
                        "fields": [
                            {"kind": "pair", "key": "value", "type": {"kind": "int"}},
                        ],
                    },
                    "text": {"kind": "string"},
                    "north": {"kind": "int"},
                    "oak": {"kind": "boolean"},
                    "states": {
                        "kind": "struct",
                        "fields": [{
                            "kind": "pair",
                            "key": {"kind": "string"},
                            "type": {"kind": "boolean"},
                        }],
                    },
                },
            },
        })

    def test_static_parallel_dispatch_selects_each_annotation_candidate(self) -> None:
        schema = DispatcherSchema.model_validate({
            "kind": "dispatcher",
            "registry": "test:kind",
            "parallelIndices": [
                {"kind": "static", "value": "number"},
                {"kind": "static", "value": "text"},
            ],
        })

        candidates = self.graph.annotation_candidates(schema)

        self.assertEqual([type(item).__name__ for item in candidates], ["StructSchema", "StringSchema"])

    def test_dispatcher_annotation_materializes_static_struct_branch(self) -> None:
        schema = DispatcherSchema.model_validate({
            "kind": "dispatcher",
            "registry": "test:kind",
            "parallelIndices": [{"kind": "static", "value": "number"}],
        })
        ctx = RenderContext(schema_graph=self.graph)

        annotation = schema.to_annotation(ctx, "Payload")

        self.assertEqual(annotation, "PayloadKindNumber")
        self.assertIn("class PayloadKindNumber:", "\n".join(ctx.additional_dataclasses))

    def test_dynamic_dispatcher_annotation_unions_all_branches(self) -> None:
        schema = DispatcherSchema.model_validate({
            "kind": "dispatcher",
            "registry": "test:kind",
            "parallelIndices": [{"kind": "dynamic", "accessor": [{"keyword": "key"}]}],
        })
        ctx = RenderContext(schema_graph=self.graph)

        annotation = schema.to_annotation(ctx, "Payload")

        self.assertIn("PayloadKindNumber", annotation)
        self.assertIn("str", annotation)
        self.assertIn("int", annotation)

    def test_indexed_schema_selects_field_after_dispatch(self) -> None:
        schema = IndexedSchema.model_validate({
            "kind": "indexed",
            "child": {
                "kind": "dispatcher",
                "registry": "test:kind",
                "parallelIndices": [{"kind": "static", "value": "number"}],
            },
            "parallelIndices": [{"kind": "static", "value": "value"}],
        })

        candidates = self.graph.annotation_candidates(schema)

        self.assertEqual(len(candidates), 1)
        self.assertIsInstance(candidates[0], IntSchema)
        self.assertEqual(schema.to_annotation(RenderContext(schema_graph=self.graph), "Payload"), "int")

    def test_dynamic_dispatch_includes_all_annotation_candidates(self) -> None:
        schema = DispatcherSchema.model_validate({
            "kind": "dispatcher",
            "registry": "test:kind",
            "parallelIndices": [{"kind": "dynamic", "accessor": ["kind"]}],
        })

        candidates = self.graph.annotation_candidates(schema)

        self.assertTrue(any(isinstance(candidate, StringSchema) for candidate in candidates))
        self.assertTrue(any(isinstance(candidate, IntSchema) for candidate in candidates))
        self.assertTrue(any(isinstance(candidate, BooleanSchema) for candidate in candidates))

    def test_key_accessor_indexes_mapping_field(self) -> None:
        schema = IndexedSchema.model_validate({
            "kind": "indexed",
            "child": {
                "kind": "dispatcher",
                "registry": "test:kind",
                "parallelIndices": [{"kind": "static", "value": "states"}],
            },
            "parallelIndices": [{"kind": "dynamic", "accessor": [{"keyword": "key"}]}],
        })

        candidates = self.graph.annotation_candidates(schema)

        self.assertEqual(len(candidates), 1)
        self.assertIsInstance(candidates[0], BooleanSchema)
        self.assertEqual(schema.to_annotation(RenderContext(schema_graph=self.graph)), "bool")

    def test_reference_resolution(self) -> None:
        result = self.graph.resolve(self.graph.symbols["::test::Alias"])

        self.assertIsInstance(result[0], IntSchema)

    def test_real_dynamic_dispatch_and_template_index(self) -> None:
        graph = SchemaGraph.from_symbol_maps(SYMBOLS_MAP)
        schema = cast(StructSchema, graph.symbols["::java::data::loot::condition::EnvironmentAttributeCheck"])
        self.assertIsInstance(schema, StructSchema)
        value_field = next(
            field
            for field in schema.fields
            if isinstance(field, PairSchema) and field.key == "value"
        )
        assert isinstance(value_field.type, IndexedSchema)
        candidates = graph.annotation_candidates(value_field.type)

        self.assertTrue(any(isinstance(candidate, FloatSchema) for candidate in candidates))


if __name__ == "__main__":
    unittest.main()