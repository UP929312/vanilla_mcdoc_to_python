# Generated from symbols.json for ::java::assets::item_definition::LocalTime
from dataclasses import dataclass
from generated_symbols.assets.item_definition.SelectCases import SelectCases


@dataclass(kw_only=True)
class LocalTime(SelectCases[str]):
    pattern: str  # Format to use for time formatting. Examples: `yyyy-MM-dd`, `HH:mm:ss`.
    locale: str | None = None  # Defaults to the root locale. Examples: `en_US`, `cs_AU@numbers=thai;calendar=japanese`.
    time_zone: str | None = None  # Defaults to the timezone set on the client. Examples: `Europe/Stockholm`, `GMT+0:45`.


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::assets::item_definition::LocalTime": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "desc": "Format to use for time formatting.\nExamples: `yyyy-MM-dd`, `HH:mm:ss`.",
                "key": "pattern",
                "type": {
                    "kind": "string",
                    "attributes": [
                        {
                            "name": "time_pattern"
                        }
                    ]
                }
            },
            {
                "kind": "pair",
                "desc": "Defaults to the root locale.\nExamples: `en_US`, `cs_AU@numbers=thai;calendar=japanese`.",
                "key": "locale",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "pair",
                "desc": "Defaults to the timezone set on the client.\nExamples: `Europe/Stockholm`, `GMT+0:45`.",
                "key": "time_zone",
                "type": {
                    "kind": "string"
                },
                "optional": True
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "concrete",
                    "child": {
                        "kind": "reference",
                        "path": "::java::assets::item_definition::SelectCases"
                    },
                    "typeArgs": [
                        {
                            "kind": "string"
                        }
                    ]
                }
            }
        ]
    }
}

