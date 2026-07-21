# Generated from symbols.json for ::java::util::text::ObjectTextConfig
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from generated_symbols.util.text.Text import Text


@dataclass(kw_only=True)
class ObjectTextConfig:
    fallback: Text | None = None  # Used in places where object component cannot be displayed (for example, server log or narration).


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ObjectTextConfig": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "attributes": [
                    {
                        "name": "since",
                        "value": {
                            "kind": "literal",
                            "value": {
                                "kind": "string",
                                "value": "26.1"
                            }
                        }
                    }
                ],
                "desc": "Used in places where object component cannot be displayed (for example, server log or narration).",
                "key": "fallback",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::Text"
                },
                "optional": True
            }
        ]
    }
}

