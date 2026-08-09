from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Literal, Self, cast


@dataclass(frozen=True, slots=True)
class IdSpec:
    registry: str | None = None
    tags: Literal["allowed", "implicit", "required"] | None = None
    definition: bool = False
    prefix: Literal["!"] | None = None
    path: str | None = None
    empty: Literal["allowed"] | None = None
    exclude: tuple[str, ...] = ()

    @classmethod
    def from_value(cls, value: object) -> Self:
        if value is None:
            return cls()
        if isinstance(value, str):
            return cls(registry=value)
        if not isinstance(value, Mapping):
            raise TypeError(f"Invalid id attribute value: {value!r}")
        options = cast(dict[str, Any], dict(value))
        if exclude := options.get("exclude"):
            options["exclude"] = (exclude,) if isinstance(exclude, str) else tuple(exclude)
        return cls(**options)

    def to_python_code(self) -> str:
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


