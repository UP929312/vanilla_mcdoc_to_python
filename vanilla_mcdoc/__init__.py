"""Generated data and asset symbol packages."""
from vanilla_mcdoc.base import import_annotation_types

import_annotation_types()  # Imports what modules only import under TYPE_CHECKING for real, see base.py for why

__version__ = "26.4.0a6"  # Read by pyproject.toml when building the package
__minecraft_version__ = "26.4-snapshot-6"
__mcdoc_commit__ = "5aab1da2ff00955cdb66f0d6c2a1154ef691a015"
