"""
Generated from symbols.json for ::java::assets::item_definition::TeamTint
Local link to file: generated_symbols/assets/item_definition/TeamTint.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

from generated_symbols.base import GeneratedModel

if TYPE_CHECKING:
    from generated_symbols.util.color.RGB import RGB


class TeamTint(GeneratedModel):
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
