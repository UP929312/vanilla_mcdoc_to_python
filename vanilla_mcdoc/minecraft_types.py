"""Hand-written types that generated code uses for some mcdoc attributes, e.g. #[uuid] and #[url]."""
import uuid
from typing import Annotated

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
