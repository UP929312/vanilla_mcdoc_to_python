"""
Generated from symbols.json for ::java::util::text::ClickEvent
Local link to file: generated_symbols/util/text/ClickEvent.py
"""
# ~~~ CODE ~~~
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Any, Literal

from runtime_metadata import IdSpec

if TYPE_CHECKING:
    from generated_symbols.data.dialog.Dialog import Dialog


@dataclass(kw_only=True)
class ClickEventChangePage:
    action: Literal['minecraft:change_page']
    page: Annotated[int, 'Range | Min `1` and above | inclusive']  # The page number to go to.


@dataclass(kw_only=True)
class ClickEventCopyToClipboard:
    action: Literal['minecraft:copy_to_clipboard']
    value: str  # The text value to copy to the clipboard.


@dataclass(kw_only=True)
class ClickEventCustom:
    action: Literal['minecraft:custom']
    id: Annotated[str, IdSpec()]  # ID of a custom action. Has no functionality on vanilla servers.
    payload: Any | None = None


@dataclass(kw_only=True)
class ClickEventOpenUrl:
    action: Literal['minecraft:open_url']
    url: str


@dataclass(kw_only=True)
class ClickEventRunCommand:
    action: Literal['minecraft:run_command']
    command: str


@dataclass(kw_only=True)
class ClickEventShowDialog:
    action: Literal['minecraft:show_dialog']
    dialog: Annotated[str, IdSpec(registry='dialog')] | Dialog


@dataclass(kw_only=True)
class ClickEventSuggestCommand:
    action: Literal['minecraft:suggest_command']
    command: str


type ClickEvent = ClickEventChangePage | ClickEventCopyToClipboard | ClickEventCustom | ClickEventOpenUrl | ClickEventRunCommand | ClickEventShowDialog | ClickEventSuggestCommand


# ~~~ MODEL DUMP ~~~
_ = {
    "::java::util::text::ClickEvent": {
        "kind": "struct",
        "fields": [
            {
                "kind": "pair",
                "key": "action",
                "type": {
                    "kind": "reference",
                    "path": "::java::util::text::ClickEventAction"
                }
            },
            {
                "kind": "spread",
                "type": {
                    "kind": "dispatcher",
                    "parallelIndices": [
                        {
                            "kind": "dynamic",
                            "accessor": [
                                "action"
                            ]
                        }
                    ],
                    "registry": "minecraft:click_event"
                }
            }
        ]
    }
}

