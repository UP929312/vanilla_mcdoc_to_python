"""
Generated from symbols.json for ::java::data::gametest::BlockBasedTestInstance
Local link to file: vanilla_mcdoc/data/gametest/BlockBasedTestInstance.py
"""
# ~~~ CODE ~~~
from typing import ClassVar

from vanilla_mcdoc.data.gametest.TestData import TestData


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
