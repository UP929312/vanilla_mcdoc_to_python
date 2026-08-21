"""
Generated from symbols.json for ::java::world::block::test_instance_block::TestInstanceBlockStatus
Local link to file: generated_symbols/world/block/test_instance_block/TestInstanceBlockStatus.py
"""
# ~~~ CODE ~~~
from enum import StrEnum


class TestInstanceBlockStatus(StrEnum):
    CLEARED = "cleared"
    RUNNING = "running"
    FINISHED = "finished"


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::world::block::test_instance_block::TestInstanceBlockStatus": {
        "kind": "enum",
        "enumKind": "string",
        "values": [
            {
                "identifier": "Cleared",
                "value": "cleared"
            },
            {
                "identifier": "Running",
                "value": "running"
            },
            {
                "identifier": "Finished",
                "value": "finished"
            }
        ]
    }
}

