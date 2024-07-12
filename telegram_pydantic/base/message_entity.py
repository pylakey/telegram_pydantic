from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# MessageEntity - Layer 181
MessageEntity = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputMessageEntityMentionName, pydantic.Tag('InputMessageEntityMentionName')],
        typing.Annotated[types.MessageEntityBankCard, pydantic.Tag('MessageEntityBankCard')],
        typing.Annotated[types.MessageEntityBlockquote, pydantic.Tag('MessageEntityBlockquote')],
        typing.Annotated[types.MessageEntityBold, pydantic.Tag('MessageEntityBold')],
        typing.Annotated[types.MessageEntityBotCommand, pydantic.Tag('MessageEntityBotCommand')],
        typing.Annotated[types.MessageEntityCashtag, pydantic.Tag('MessageEntityCashtag')],
        typing.Annotated[types.MessageEntityCode, pydantic.Tag('MessageEntityCode')],
        typing.Annotated[types.MessageEntityCustomEmoji, pydantic.Tag('MessageEntityCustomEmoji')],
        typing.Annotated[types.MessageEntityEmail, pydantic.Tag('MessageEntityEmail')],
        typing.Annotated[types.MessageEntityHashtag, pydantic.Tag('MessageEntityHashtag')],
        typing.Annotated[types.MessageEntityItalic, pydantic.Tag('MessageEntityItalic')],
        typing.Annotated[types.MessageEntityMention, pydantic.Tag('MessageEntityMention')],
        typing.Annotated[types.MessageEntityMentionName, pydantic.Tag('MessageEntityMentionName')],
        typing.Annotated[types.MessageEntityPhone, pydantic.Tag('MessageEntityPhone')],
        typing.Annotated[types.MessageEntityPre, pydantic.Tag('MessageEntityPre')],
        typing.Annotated[types.MessageEntitySpoiler, pydantic.Tag('MessageEntitySpoiler')],
        typing.Annotated[types.MessageEntityStrike, pydantic.Tag('MessageEntityStrike')],
        typing.Annotated[types.MessageEntityTextUrl, pydantic.Tag('MessageEntityTextUrl')],
        typing.Annotated[types.MessageEntityUnderline, pydantic.Tag('MessageEntityUnderline')],
        typing.Annotated[types.MessageEntityUnknown, pydantic.Tag('MessageEntityUnknown')],
        typing.Annotated[types.MessageEntityUrl, pydantic.Tag('MessageEntityUrl')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
