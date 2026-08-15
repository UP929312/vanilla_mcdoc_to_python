from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from utils import symbol_path_to_import_string_and_name, symbol_path_to_object_name

if TYPE_CHECKING:
    from schema_resolution import SchemaGraph


@dataclass(frozen=True)
class Import:
    relative_module: str
    identifier: str
    type_checking_only: bool
    is_builtin: bool

    @staticmethod
    def to_python_code(entries: set[Import]) -> list[str]:
        runtime_keys = {(entry.relative_module, entry.identifier) for entry in entries if not entry.type_checking_only}
        entries = {
            entry for entry in entries
            if not entry.type_checking_only or (entry.relative_module, entry.identifier) not in runtime_keys
        }

        def build_lines(group: set[Import]) -> list[str]:
            modules = {entry.relative_module for entry in group}
            return [
                f"from {module} import {', '.join(sorted({entry.identifier for entry in group if entry.relative_module == module}, key=lambda name: (not name.isupper(), name)))}"
                for module in sorted(modules)
            ]

        builtins = {entry for entry in entries if entry.is_builtin and not entry.type_checking_only}
        regular = {entry for entry in entries if not entry.is_builtin and not entry.type_checking_only}
        type_checking = {entry for entry in entries if entry.type_checking_only}
        if type_checking:
            builtins.add(Import("typing", "TYPE_CHECKING", False, True))

        lines = build_lines(builtins)
        if lines and regular:
            lines.append("")
        lines.extend(build_lines(regular))
        if type_checking:
            lines.append("\nif TYPE_CHECKING:")
            lines.extend(f"    {line}" for line in build_lines(type_checking))
        return lines + ["\n"]


@dataclass
class SingleSymbolContext:
    """Stores the imports, helper declarations, and rendering options for one generated symbol file."""

    required_imports: set[Import] = field(default_factory=set)
    local_type_params: set[str] = field(default_factory=set)
    additional_dataclasses: list[str] = field(default_factory=list)
    schema_graph: SchemaGraph = field(default_factory=lambda: SchemaGraph.from_symbol_maps({}))
    current_symbol_path: str = ""
    allow_numeric_type_arg_shortcuts: bool = True
    require_runtime_imports: bool = False
    # Stable names per (preferred name, schema/path fingerprint), shared by nested contexts.
    allocated_name_by_identity: dict[tuple[str, str], str] = field(default_factory=dict)
    # Helper class/type names already appended to additional_dataclasses.
    emitted_declaration_names: set[str] = field(default_factory=set)

    def require_annotated(self) -> None:
        self.required_imports.add(Import("typing", "Annotated", type_checking_only=False, is_builtin=True))

    def add_dataclass(self, lines: list[str]) -> None:
        declaration: str = next((line for line in lines if line.startswith(("class ", "type "))), None)  # type: ignore[assignment]
        if (name := declaration.split()[1].split("(", 1)[0]) in self.emitted_declaration_names:
            return
        self.emitted_declaration_names.add(name)
        self.additional_dataclasses.extend(lines + [""])

    def allocate_name(self, preferred: str, fingerprint: str) -> str:
        key = preferred, fingerprint
        if key not in self.allocated_name_by_identity:
            used = set(self.allocated_name_by_identity.values())
            used.add(symbol_path_to_object_name(self.current_symbol_path))
            suffix = 2
            name = preferred
            while name in used:
                name = f"{preferred}{suffix}"
                suffix += 1
            self.allocated_name_by_identity[key] = name
        return self.allocated_name_by_identity[key]

    def add_import_by_symbol_path(self, path: str) -> str:
        """Add the referenced symbol's import and return its collision-safe local name."""
        module, name = symbol_path_to_import_string_and_name(path)
        if path == self.current_symbol_path:
            return name
        if path in self.local_type_params:
            return name
        imported_name = self.allocate_name(name, path)
        identifier = name if imported_name == name else f"{name} as {imported_name}"
        self.required_imports.add(Import(module, identifier, type_checking_only=not self.require_runtime_imports, is_builtin=False))
        return imported_name

    def with_rendering_options(
        self,
        allow_numeric_type_arg_shortcuts: bool = True,
        require_runtime_imports: bool | None = None,
    ) -> SingleSymbolContext:
        """Copy the context with new rendering flags while sharing accumulated generation state."""
        return SingleSymbolContext(
            required_imports=self.required_imports,
            local_type_params=self.local_type_params,
            additional_dataclasses=self.additional_dataclasses,
            current_symbol_path=self.current_symbol_path,
            schema_graph=self.schema_graph,
            allow_numeric_type_arg_shortcuts=allow_numeric_type_arg_shortcuts,
            require_runtime_imports=self.require_runtime_imports if require_runtime_imports is None else require_runtime_imports,
            allocated_name_by_identity=self.allocated_name_by_identity,
            emitted_declaration_names=self.emitted_declaration_names,
        )
