"""
Generated from symbols.json for ::java::data::variants::SpawnPrioritySelectors
Local link to file: vanilla_mcdoc/data/variants/SpawnPrioritySelectors.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from vanilla_mcdoc.base import GeneratedModel

if TYPE_CHECKING:
    from vanilla_mcdoc.data.variants.SpawnPrioritySelector import SpawnPrioritySelector


class SpawnPrioritySelectors(GeneratedModel):
    spawn_conditions: list[SpawnPrioritySelector]  # The spawn conditions for this variant. Selection process: - Conditions for all variants for the given entity type are evaluated for the spawn position - Entries with a priority lower than the maximum priority of the remaining entries are removed - A random entry is picked out of the remaining ones - If no conditions are remaining, the variant remains unchanged from the default


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::data::variants::SpawnPrioritySelectors": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "The spawn conditions for this variant. Selection process:\n- Conditions for all variants for the given entity type are evaluated for the spawn position\n- Entries with a priority lower than the maximum priority of the remaining entries are removed\n- A random entry is picked out of the remaining ones\n- If no conditions are remaining, the variant remains unchanged from the default",
                "key": "spawn_conditions",
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::data::variants::SpawnPrioritySelector"
                    }
                }
            }
        ]
    }
}
