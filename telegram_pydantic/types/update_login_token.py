from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateLoginToken(BaseModel):
    """
    types.UpdateLoginToken
    ID: 0x564fe691
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateLoginToken', 'UpdateLoginToken'] = pydantic.Field(
        'types.UpdateLoginToken',
        alias='_'
    )

