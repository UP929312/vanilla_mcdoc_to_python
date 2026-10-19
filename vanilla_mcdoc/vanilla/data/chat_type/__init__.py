"""Vanilla's data/chat_type/ files"""
from vanilla_mcdoc.data.chat_type.ChatDecoration import ChatDecoration
from vanilla_mcdoc.data.chat_type.ChatDecorationParameter import ChatDecorationParameter
from vanilla_mcdoc.data.chat_type.ChatType import ChatType
from vanilla_mcdoc.util.text.TextColor import TextColor
from vanilla_mcdoc.util.text.TextStyle import TextStyle

CHAT = ChatType(
    chat=ChatDecoration(
        translation_key='chat.type.text',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
    narration=ChatDecoration(
        translation_key='chat.type.text.narrate',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
)

EMOTE_COMMAND = ChatType(
    chat=ChatDecoration(
        translation_key='chat.type.emote',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
    narration=ChatDecoration(
        translation_key='chat.type.emote',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
)

MSG_COMMAND_INCOMING = ChatType(
    chat=ChatDecoration(
        translation_key='commands.message.display.incoming',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
        style=TextStyle(color=TextColor.GRAY, italic=True),
    ),
    narration=ChatDecoration(
        translation_key='chat.type.text.narrate',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
)

MSG_COMMAND_OUTGOING = ChatType(
    chat=ChatDecoration(
        translation_key='commands.message.display.outgoing',
        parameters=[ChatDecorationParameter.TARGET, ChatDecorationParameter.CONTENT],
        style=TextStyle(color=TextColor.GRAY, italic=True),
    ),
    narration=ChatDecoration(
        translation_key='chat.type.text.narrate',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
)

SAY_COMMAND = ChatType(
    chat=ChatDecoration(
        translation_key='chat.type.announcement',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
    narration=ChatDecoration(
        translation_key='chat.type.text.narrate',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
)

TEAM_MSG_COMMAND_INCOMING = ChatType(
    chat=ChatDecoration(
        translation_key='chat.type.team.text',
        parameters=[ChatDecorationParameter.TARGET, ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
    narration=ChatDecoration(
        translation_key='chat.type.text.narrate',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
)

TEAM_MSG_COMMAND_OUTGOING = ChatType(
    chat=ChatDecoration(
        translation_key='chat.type.team.sent',
        parameters=[ChatDecorationParameter.TARGET, ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
    narration=ChatDecoration(
        translation_key='chat.type.text.narrate',
        parameters=[ChatDecorationParameter.SENDER, ChatDecorationParameter.CONTENT],
    ),
)
