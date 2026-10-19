"""Generated data and asset symbol packages."""
from vanilla_mcdoc.base import import_annotation_types

import_annotation_types()  # Imports what modules only import under TYPE_CHECKING for real, see base.py for why

__version__ = "26.4.0a4"  # Read by pyproject.toml when building the package
__minecraft_version__ = "26.4-snapshot-4"
__mcdoc_commit__ = "3a968482defd547a7405919a7816c0bbb9112af9"
