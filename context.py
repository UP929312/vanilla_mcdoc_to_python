import sys
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from utils import GENERATED_SYMBOLS_DIRECTORY, symbol_path_to_import_string_and_name, symbol_path_to_object_name

if TYPE_CHECKING:
    from schema_resolution import SchemaGraph


@dataclass(frozen=True)
class Import:
    relative_module: str
    identifier: str
    type_checking_only: bool

    @property
    def is_builtin(self) -> bool:
        """Python's standard library (e.g. typing, enum), as opposed to third party packages like pydantic."""
        return self.relative_module.split(".")[0] in sys.stdlib_module_names

    @property
    def is_local(self) -> bool:
        """Our own modules, as opposed to third party packages like pydantic (each gets its own group of imports)."""
        return self.relative_module.split(".")[0] in {GENERATED_SYMBOLS_DIRECTORY.name, "minecraft_registry"}

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

        runtime = {entry for entry in entries if not entry.type_checking_only}
        builtins = {entry for entry in runtime if entry.is_builtin}
        type_checking = {entry for entry in entries if entry.type_checking_only}
        if type_checking:
            builtins.add(Import("typing", "TYPE_CHECKING", False))
        # Builtins, then third party packages, then local imports, with a blank line between each group
        lines: list[str] = []
        group_lines = [
            build_lines(builtins),
            build_lines({entry for entry in runtime if not entry.is_builtin and not entry.is_local}),  # Third party (e.g. pydantic)
            build_lines({entry for entry in runtime if entry.is_local}),  # Local
        ]
        for group_lines in group_lines:
            if group_lines:
                lines.extend(([""] if lines else []) + group_lines)
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
    # The datapack/resourcepack directory (e.g. "recipe") if this symbol is a root resource, for its __resource_dir__.
    resource_dir: str | None = None
    # Stable names per (preferred name, schema/path fingerprint), shared by nested contexts.
    allocated_name_by_identity: dict[tuple[str, str], str] = field(default_factory=dict)
    # Helper class/type names already appended to additional_dataclasses.
    emitted_declaration_names: set[str] = field(default_factory=set)

    def require_annotated(self) -> None:
        self.required_imports.add(Import("typing", "Annotated", type_checking_only=False))

    def type_params_suffix(self) -> str:
        """The local type params to put after a generic name, e.g. `[K, V]`, or "" if there aren't any."""
        type_param_names = sorted({symbol_path_to_object_name(path) for path in self.local_type_params})
        return f"[{', '.join(type_param_names)}]" if type_param_names else ""

    def add_dataclass(self, lines: list[str]) -> None:
        """Adds the given dataclass declaration lines to the context, if not already emitted."""
        dataclass_name = lines[0].split()[1].split("(", 1)[0]
        if dataclass_name in self.emitted_declaration_names:
            return
        self.emitted_declaration_names.add(dataclass_name)
        self.additional_dataclasses.extend(lines + [""])

    def allocate_name(self, preferred: str, fingerprint: str) -> str:
        """Gives the dataclass a name that is stable across nested contexts and avoids collisions with other names in the same context."""
        key = preferred, fingerprint
        if key not in self.allocated_name_by_identity:
            used = set(self.allocated_name_by_identity.values())
            used.add(symbol_path_to_object_name(self.current_symbol_path))
            suffix = 2  # TODO: Remind myself why it starts at 2
            name = preferred
            while name in used:
                name = f"{preferred}{suffix}"
                suffix += 1
            self.allocated_name_by_identity[key] = name
        return self.allocated_name_by_identity[key]

    def add_import_by_symbol_path(self, path: str) -> str:
        """Add the referenced symbol's import and return its collision-safe local name."""
        module, name = symbol_path_to_import_string_and_name(path)
        if path == self.current_symbol_path or path in self.local_type_params:
            return name
        imported_name = self.allocate_name(name, path)
        identifier = name if imported_name == name else f"{name} as {imported_name}"
        self.required_imports.add(Import(module, identifier, type_checking_only=not self.require_runtime_imports))
        return imported_name

    def copy(self) -> SingleSymbolContext:
        """Copy the context with new values while sharing accumulated generation state.
        This is normally so we can temporarily disable attributes like:
        - allow_numeric_type_arg_shortcuts
        - require_runtime_imports
        - resource_dir
        """
        return SingleSymbolContext(
            required_imports=self.required_imports,
            local_type_params=self.local_type_params,
            additional_dataclasses=self.additional_dataclasses,
            current_symbol_path=self.current_symbol_path,
            schema_graph=self.schema_graph,
            allow_numeric_type_arg_shortcuts=self.allow_numeric_type_arg_shortcuts,
            require_runtime_imports=self.require_runtime_imports,
            resource_dir=self.resource_dir,
            allocated_name_by_identity=self.allocated_name_by_identity,
            emitted_declaration_names=self.emitted_declaration_names,
        )
