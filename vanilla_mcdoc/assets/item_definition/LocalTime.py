"""
Generated from symbols.json for ::java::assets::item_definition::LocalTime
Local link to file: vanilla_mcdoc/assets/item_definition/LocalTime.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.assets.item_definition.SelectCases import SelectCases


class LocalTime(SelectCases[str]):
    pattern: str  # Format to use for time formatting. Examples: `yyyy-MM-dd`, `HH:mm:ss`.
    locale: str | None = None  # Defaults to the root locale. Examples: `en_US`, `cs_AU@numbers=thai;calendar=japanese`.
    time_zone: str | None = None  # Defaults to the timezone set on the client. Examples: `Europe/Stockholm`, `GMT+0:45`.
