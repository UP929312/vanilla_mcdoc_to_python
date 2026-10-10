"""
Generated from symbols.json for ::java::util::avatar::ProfileProperty
Local link to file: vanilla_mcdoc/util/avatar/ProfileProperty.py
"""
# ~~~ CODE ~~~
from typing import Annotated

from pydantic import Field

from vanilla_mcdoc.base import GeneratedModel


class ProfileProperty(GeneratedModel):
    name: Annotated[str, Field(min_length=0, max_length=64)]  # Usually `textures`.
    value: Annotated[str, Field(min_length=0, max_length=32767)]  # Base64 encoded JSON value of the texture index.
    signature: Annotated[str, Field(min_length=0, max_length=1024)] | None = None  # Verifies the hash of the resulting texture.
