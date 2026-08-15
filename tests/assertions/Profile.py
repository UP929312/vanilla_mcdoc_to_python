# ~~~ WHAT ARE WE TESTING ~~~

# Making sure for only 1 struct generated, we don't number it

# ~~~ FILE CONTENT ~~~
"""
Generated from symbols.json for ::java::util::avatar::Profile
Local link to file: generated_symbols/util/avatar/Profile.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated

from minecraft_registry import IdSpec

if TYPE_CHECKING:
    from generated_symbols.util.avatar.PlayerModelType import PlayerModelType
    from generated_symbols.util.avatar.ProfileProperty import ProfileProperty
    from generated_symbols.util.avatar.ProfilePropertyMap import ProfilePropertyMap


@dataclass(kw_only=True)
class ProfileStruct:
    name: str | None = None  # Username of a player profile. If `id` doesn't exist, this field is used to fetch the current skin of the profile.
    id: tuple[int, int, int, int] | None = None  # UUID of the player profile. If `name` doesn't exist, this field is used to fetch the current skin of the profile.
    properties: Annotated[list[ProfileProperty], 'Length = 0-16 (both inclusive)'] | ProfilePropertyMap | None = None  # Resolved textures hosted on the minecraft CDN.
    texture: Annotated[str, IdSpec(registry='texture')] | None = None  # Skin texture override.
    cape: Annotated[str, IdSpec(registry='texture')] | None = None  # Cape texture override.
    elytra: Annotated[str, IdSpec(registry='texture')] | None = None  # Elytra texture override. If this texture is not present either as override or in player profile, the cape texture is used. If the cape texture is also not present, the default elytra texture is used.
    model: PlayerModelType | None = None  # Model type override.


type Profile = ProfileStruct | str
