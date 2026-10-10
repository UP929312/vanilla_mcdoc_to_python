"""
Generated from symbols.json for ::java::assets::shader::program::Defines
Local link to file: vanilla_mcdoc/assets/shader/program/Defines.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Defines(GeneratedModel):
    values: dict[str, str] | None = None  # Values that will be injected as `#define <key> <value>` at the top of the file.
    flags: list[str] | None = None  # Flags that will be injected as `#define <key>` at the top of the file.
