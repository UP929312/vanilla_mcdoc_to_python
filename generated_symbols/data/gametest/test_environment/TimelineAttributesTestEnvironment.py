# Generated from symbols.json for ::java::data::gametest::test_environment::TimelineAttributesTestEnvironment
from dataclasses import dataclass


@dataclass(kw_only=True)
class TimelineAttributesTestEnvironment:
    timelines: list[str]


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

