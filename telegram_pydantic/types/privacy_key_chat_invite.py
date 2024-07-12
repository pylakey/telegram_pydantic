from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyChatInvite(BaseModel):
    """
    types.PrivacyKeyChatInvite
    ID: 0x500e6dfa
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyChatInvite', 'PrivacyKeyChatInvite'] = pydantic.Field(
        'types.PrivacyKeyChatInvite',
        alias='_'
    )

