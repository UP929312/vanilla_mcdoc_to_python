"""Generated data and asset symbol packages."""
from vanilla_mcdoc.base import import_annotation_types

import_annotation_types()  # Imports what modules only import under TYPE_CHECKING for real, see base.py for why

__version__ = "26.4.0a10"  # Read by pyproject.toml when building the package
__minecraft_version__ = "26.4-snapshot-10"
__mcdoc_commit__ = "faf645d4290e2d1d12368a7a9e496825f0471a54"
