"""
Generated from symbols.json for ::java::data::gametest::test_environment::FunctionTestEnvironment
Local link to file: generated_symbols/data/gametest/test_environment/FunctionTestEnvironment.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import Annotated, ClassVar

from minecraft_registry import IdSpec


@dataclass(kw_only=True)
class FunctionTestEnvironment:
    __resource_dir__: ClassVar[str] = 'test_environment'

    setup: Annotated[str, IdSpec(registry='function')] | None = None
    teardown: Annotated[str, IdSpec(registry='function')] | None = None


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::test_environment::FunctionTestEnvironment": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "setup",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "function"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            },
            {
                "kind": "pair",
                "key": "teardown",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "id",
                            "value": {
                                "kind": "literal",
                                "value": {
                                    "kind": "string",
                                    "value": "function"
                                }
                            }
                        }
                    ]
                },
                "optional": True
            }
        ]
    }
}

