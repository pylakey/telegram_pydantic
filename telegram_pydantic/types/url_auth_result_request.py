from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UrlAuthResultRequest(BaseModel):
    """
    types.UrlAuthResultRequest
    ID: 0x92d33a0e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UrlAuthResultRequest', 'UrlAuthResultRequest'] = pydantic.Field(
        'types.UrlAuthResultRequest',
        alias='_'
    )

    bot: "base.User"
    domain: str
    request_write_access: typing.Optional[bool] = None
