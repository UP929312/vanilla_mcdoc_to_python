"""
Generated from symbols.json for ::java::data::dialog::action::DynamicRunCommand
Local link to file: vanilla_mcdoc/data/dialog/action/DynamicRunCommand.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class DynamicRunCommand(GeneratedModel):
    template: str  # A macro template to be interpred as a command. Special characters (including both `'` and `"`) from text input will be escaped to fit in SNBT literal.
