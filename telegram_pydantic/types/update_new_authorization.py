from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateNewAuthorization(BaseModel):
    """
    types.UpdateNewAuthorization
    ID: 0x8951abef
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateNewAuthorization', 'UpdateNewAuthorization'] = pydantic.Field(
        'types.UpdateNewAuthorization',
        alias='_'
    )

    hash: int
    unconfirmed: typing.Optional[bool] = None
    date: Datetime
    device: typing.Optional[str] = None
    location: typing.Optional[str] = None
