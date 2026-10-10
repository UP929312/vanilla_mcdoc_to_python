"""
Generated from symbols.json for ::java::data::util::ContextScoreProvider
Local link to file: vanilla_mcdoc/data/util/ContextScoreProvider.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.loot.EntityTarget import EntityTarget


class ContextScoreProvider(GeneratedModel):
    target: EntityTarget


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::util::ContextScoreProvider": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "target",
                "type": {
                    "kind": "reference",
                    "path": "::java::data::loot::EntityTarget"
                }
            }
        ]
    }
}
