# Generated from symbols.json for ::java::data::gametest::BlockBasedTestInstance
from dataclasses import dataclass
from generated_symbols.data.gametest.TestData import TestData


@dataclass(kw_only=True)
class BlockBasedTestInstance(TestData):
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

