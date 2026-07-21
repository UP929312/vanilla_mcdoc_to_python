# Generated from symbols.json for ::java::data::variants::SpawnPrioritySelectors
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.data.variants.SpawnPrioritySelector import SpawnPrioritySelector


@dataclass(kw_only=True)
class SpawnPrioritySelectors:
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

