from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SentCodeSuccess(BaseModel):
    """
    types.auth.SentCodeSuccess
    ID: 0x2390fe44
    Layer: 181
    """
    QUALNAME: typing.Literal['types.auth.SentCodeSuccess', 'SentCodeSuccess'] = pydantic.Field(
        'types.auth.SentCodeSuccess',
        alias='_'
    )

    authorization: "base.auth.Authorization"
