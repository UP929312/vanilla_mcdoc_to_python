"""
Generated from symbols.json for ::java::assets::regional_compliancies::Notification
Local link to file: vanilla_mcdoc/assets/regional_compliancies/Notification.py
"""
# ~~~ CODE ~~~
from vanilla_mcdoc.base import GeneratedModel


class Notification(GeneratedModel):
    delay: int | None = None
    period: int
    title: str
    message: str
