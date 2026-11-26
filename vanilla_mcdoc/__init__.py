"""Generated data and asset symbol packages."""
from vanilla_mcdoc.base import import_annotation_types

import_annotation_types()  # Imports what modules only import under TYPE_CHECKING for real, see base.py for why

__version__ = "26.4.0b1"  # Read by pyproject.toml when building the package
__minecraft_version__ = "26.4-pre-1"
__mcdoc_commit__ = "c0dd53f5e9af300344b5d3449957d2208398637b"
