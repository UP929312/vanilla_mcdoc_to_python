import importlib
import pkgutil

import generated_symbols


def test_every_generated_module_imports() -> None:
    """Catches generated code that can't even be defined, e.g. a field that shadows its own type (`BlockState: BlockState`)."""
    failures: dict[str, str] = {}
    for module_info in pkgutil.walk_packages(generated_symbols.__path__, "generated_symbols."):
        try:
            importlib.import_module(module_info.name)
        except Exception as error:
            failures[module_info.name] = f"{type(error).__name__}: {error}"
    assert not failures, "\n".join(f"{name}: {error}" for name, error in failures.items())
