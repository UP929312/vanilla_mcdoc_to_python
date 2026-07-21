# Generated from symbols.json for ::java::assets::regional_compliancies::RegionalCompliancies
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.assets.regional_compliancies.Code import Code
    from generated_symbols.assets.regional_compliancies.Notification import Notification


type RegionalCompliancies = dict[Code, list[Notification]]


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::regional_compliancies::RegionalCompliancies": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": {
                    "kind": "reference",
                    "path": "::java::assets::regional_compliancies::Code"
                },
                "type": {
                    "kind": "list",
                    "item": {
                        "kind": "reference",
                        "path": "::java::assets::regional_compliancies::Notification"
                    }
                }
            }
        ]
    }
}

