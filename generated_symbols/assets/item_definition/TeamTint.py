# Generated from symbols.json for ::java::assets::item_definition::TeamTint
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


@dataclass(kw_only=True)
class TeamTint:
    default: RGB  # Tint to apply when there is no context entity, entity is not in a team or the team has no color.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::TeamTint": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Tint to apply when there is no context entity, entity is not in a team or the team has no color.",
                "key": "default",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::color::RGB"
                }
            }
        ]
    }
}

