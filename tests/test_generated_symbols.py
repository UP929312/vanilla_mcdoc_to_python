import importlib
import pkgutil

import vanilla_mcdoc


def test_every_generated_module_imports() -> None:
    """Catches generated code that can't even be defined, e.g. a field that shadows its own type (`BlockState: BlockState`)."""
    failures: dict[str, str] = {}
    for module_info in pkgutil.walk_packages(vanilla_mcdoc.__path__, "vanilla_mcdoc."):
        try:
            importlib.import_module(module_info.name)
        except Exception as error:  # pylint: disable=broad-exception-caught
            failures[module_info.name] = f"{type(error).__name__}: {error}"
    assert not failures, "\n".join(f"{name}: {error}" for name, error in failures.items())
