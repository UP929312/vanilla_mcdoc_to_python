"""Hand-written types that generated code uses for some mcdoc attributes, e.g. #[uuid], #[url] and #[id]."""
import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Annotated, Any, Literal, Self

from pydantic import Field

type Int32 = Annotated[int, Field(ge=-2**31, le=2**31 - 1)]

# How Minecraft stores a UUID in NBT: 4 signed 32-bit ints, most significant first, e.g. [I; -132296786, 2112623056, ...]
type MinecraftUUID = tuple[Int32, Int32, Int32, Int32]

# A UUID as a string, e.g. "f81d4fae-7dec-11d0-a765-00a0c91e6bf6". Like Java's UUID.fromString (which Minecraft uses),
# this is lenient: any 5 hyphen-separated groups of hex digits.
type MinecraftUUIDString = Annotated[str, Field(pattern=r"^[0-9a-fA-F]+-[0-9a-fA-F]+-[0-9a-fA-F]+-[0-9a-fA-F]+-[0-9a-fA-F]+$")]

# Minecraft only opens http(s) links. Not pydantic's HttpUrl, because that normalises the URL (e.g. adds a trailing /).
type MinecraftURL = Annotated[str, Field(pattern=r"^https?://")]  # Starts with http:// or https://


def uuid_to_int_array(value: uuid.UUID) -> tuple[int, int, int, int]:
    """Convert a Python UUID (e.g. uuid.uuid4()) to Minecraft's 4 signed ints."""
    words = [(value.int >> shift) & 0xFFFFFFFF for shift in (96, 64, 32, 0)]
    first, second, third, fourth = (word - 2**32 if word >= 2**31 else word for word in words)
    return first, second, third, fourth


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
        values: list[tuple[str, object]] = [
            ("registry", self.registry),
            ("tags", self.tags),
            ("definition", self.definition if self.definition else None),
            ("prefix", self.prefix),
            ("path", self.path),
            ("empty", self.empty),
            ("exclude", self.exclude if self.exclude else None),
        ]
        arguments = ", ".join(f"{name}={value!r}" for name, value in values if value is not None)
        return f"IdSpec({arguments})"
