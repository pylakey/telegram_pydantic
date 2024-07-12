from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UrlAuthResultAccepted(BaseModel):
    """
    types.UrlAuthResultAccepted
    ID: 0x8f8c0e4e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UrlAuthResultAccepted', 'UrlAuthResultAccepted'] = pydantic.Field(
        'types.UrlAuthResultAccepted',
        alias='_'
    )

    url: str
