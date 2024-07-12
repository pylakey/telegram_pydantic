from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeTypeSmsPhrase(BaseModel):
    """
    types.auth.SentCodeTypeSmsPhrase
    ID: 0xb37794af
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeTypeSmsPhrase', 'SentCodeTypeSmsPhrase'] = pydantic.Field(
        'types.auth.SentCodeTypeSmsPhrase',
        alias='_'
    )

    beginning: typing.Optional[str] = None
