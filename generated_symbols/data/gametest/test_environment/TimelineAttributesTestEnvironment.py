"""
Generated from symbols.json for ::java::data::gametest::test_environment::TimelineAttributesTestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/TimelineAttributesTestEnvironment.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated

from runtime_metadata import IdSpec


@dataclass(kw_only=True)
class TimelineAttributesTestEnvironment:
    timelines: list[Annotated[str, IdSpec(registry='timeline')]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::TimelineAttributesTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "timelines",
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
                                        "value": "timeline"
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
}

