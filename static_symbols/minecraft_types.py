"""Hand-written types that generated code uses for some mcdoc attributes, e.g. #[uuid], #[url] and #[id]."""
from collections.abc import Mapping
from dataclasses import dataclass, fields
from enum import Enum
from typing import Annotated, Any, Literal, Self

from pydantic import BeforeValidator, Field, PlainSerializer

type Int32 = Annotated[int, Field(ge=-2**31, le=2**31 - 1)]

# How Minecraft stores a UUID in NBT: 4 signed 32-bit ints, most significant first, e.g. [I; -132296786, 2112623056, ...]
type MinecraftUUID = tuple[Int32, Int32, Int32, Int32]

# A UUID as a string, e.g. "f81d4fae-7dec-11d0-a765-00a0c91e6bf6". Like Java's UUID.fromString (which Minecraft uses),
# this is lenient: any 5 hyphen-separated groups of hex digits.
type MinecraftUUIDString = Annotated[str, Field(pattern=r"^[0-9a-fA-F]+-[0-9a-fA-F]+-[0-9a-fA-F]+-[0-9a-fA-F]+-[0-9a-fA-F]+$")]

# Minecraft only opens http(s) links. Not pydantic's HttpUrl, because that normalises the URL (e.g. adds a trailing /).
# Any case, as the game lowercases the scheme before checking it (Util.parseAndValidateUntrustedUri), so HTTPS:// works too
type MinecraftURL = Annotated[str, Field(pattern=r"^(?i:https?)://")]

# An enum of ids, e.g. a loot table's type. Its values have no namespace (LootContextParamSets.CHEST is "chest"), but vanilla's
# files do ("minecraft:chest"), and both mean the same, so this accepts both, and writes the namespace in JSON (like vanilla)
type NamespacedId[E: Enum] = Annotated[
    E,
    BeforeValidator(lambda value: value.removeprefix("minecraft:") if isinstance(value, str) else value),
    PlainSerializer(lambda member: f"minecraft:{member.value}", when_used="json"),
]


@dataclass(frozen=True, slots=True)
class IdSpec:
    """An #[id] attribute: the string is a resource location from `registry`, e.g. IdSpec(registry='item') for "minecraft:stone".
    Generated code puts it in the metadata, e.g. Annotated[str, IdSpec(registry='item')]"""
    registry: str | None = None
    tags: Literal["allowed", "implicit", "required"] | None = None
    definition: bool = False
    prefix: Literal["!"] | None = None
    path: str | None = None
    empty: Literal["allowed"] | None = None
    exclude: tuple[str, ...] = ()

    @classmethod
    def from_value(cls, value: str | Mapping[str, Any] | None) -> Self:
        if value is None:
            return cls()
        if isinstance(value, str):
            return cls(registry=value)
        options = dict(value)
        if exclude := options.get("exclude"):
            options["exclude"] = tuple(exclude)
        return cls(**options)

    def to_annotation(self) -> str:
        """e.g. IdSpec(registry='item', tags='allowed'), leaving out anything that's still its default"""
        values = {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) != field.default
        }
        return f"IdSpec({', '.join(f'{name}={value!r}' for name, value in values.items())})"
