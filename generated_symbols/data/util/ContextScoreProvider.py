# Generated from symbols.json for ::java::data::util::ContextScoreProvider
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.loot.EntityTarget import EntityTarget


@dataclass(kw_only=True)
class ContextScoreProvider:
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

