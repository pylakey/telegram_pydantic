from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PollAnswer(BaseModel):
    """
    types.PollAnswer
    ID: 0xff16e2ca
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PollAnswer', 'PollAnswer'] = pydantic.Field(
        'types.PollAnswer',
        alias='_'
    )

    text: "base.TextWithEntities"
    option: Bytes
