from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# account.EmojiStatuses - Layer 181
EmojiStatuses = typing.Annotated[
    typing.Union[
        typing.Annotated[types.account.EmojiStatuses, pydantic.Tag('account.EmojiStatuses')],
        typing.Annotated[types.account.EmojiStatusesNotModified, pydantic.Tag('account.EmojiStatusesNotModified')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
