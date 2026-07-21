# Generated from symbols.json for ::java::data::worldgen::feature::FossilConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from generated_symbols.data.worldgen.processor_list.ProcessorListRef import ProcessorListRef


@dataclass(kw_only=True)
class FossilConfig:
    max_empty_corners_allowed: Annotated[int, 'Range | `0`-`7` | both inclusive']  # If more corners are exposed to air, feature placement is cancelled.
    fossil_structures: list[str]
    overlay_structures: list[str]
    fossil_processors: ProcessorListRef
    overlay_processors: ProcessorListRef


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::worldgen::feature::FossilConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "If more corners are exposed to air, feature placement is cancelled.",
                "key": "max_empty_corners_allowed",
                "type": {
                    "kind": "int",
                    "valueRange": {
                        "kind": 0,
                        "min": 0,
                        "max": 7
                    }
                }
            },
            {
                "kind": "pair",
                "key": "fossil_structures",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "structure"
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            {
                "kind": "pair",
                "key": "overlay_structures",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "string",
                        "attributes": [
                            {
                                "name": "id",
                                "value": {
                                    "kind": "literal",
                                    "value": {
                                        "kind": "string",
                                        "value": "structure"
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            {
                "kind": "pair",
                "key": "fossil_processors",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::ProcessorListRef"
                }
            },
            {
                "kind": "pair",
                "key": "overlay_processors",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::worldgen::processor_list::ProcessorListRef"
                }
            }
        ]
    }
}

