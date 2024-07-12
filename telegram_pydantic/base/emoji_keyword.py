from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# EmojiKeyword - Layer 181
EmojiKeyword = typing.Annotated[
    typing.Union[
        typing.Annotated[types.EmojiKeyword, pydantic.Tag('EmojiKeyword')],
        typing.Annotated[types.EmojiKeywordDeleted, pydantic.Tag('EmojiKeywordDeleted')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
