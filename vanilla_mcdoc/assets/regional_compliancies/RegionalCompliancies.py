"""
Generated from symbols.json for ::java::assets::regional_compliancies::RegionalCompliancies
Local link to file: vanilla_mcdoc/assets/regional_compliancies/RegionalCompliancies.py
"""
# ~~~ CODE ~~~
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vanilla_mcdoc.assets.regional_compliancies.Code import Code
    from vanilla_mcdoc.assets.regional_compliancies.Notification import Notification


type RegionalCompliancies = dict[Code, list[Notification]]
