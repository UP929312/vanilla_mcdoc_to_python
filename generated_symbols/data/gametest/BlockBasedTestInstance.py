"""
Generated from symbols.json for ::java::data::gametest::BlockBasedTestInstance
Local link to file: generated_symbols/data/gametest/BlockBasedTestInstance.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import ClassVar

from generated_symbols.data.gametest.TestData import TestData


@dataclass(kw_only=True)
class BlockBasedTestInstance(TestData):
    __resource_dir__: ClassVar[str] = 'test_instance'

    pass


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::gametest::BlockBasedTestInstance": {
        "kind": "struct",
        "fields": [
            {
                "kind": "spread",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::gametest::TestData"
                }
            }
        ]
    }
}

