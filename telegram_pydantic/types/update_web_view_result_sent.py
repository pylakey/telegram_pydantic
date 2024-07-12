from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateWebViewResultSent(BaseModel):
    """
    types.UpdateWebViewResultSent
    ID: 0x1592b79d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateWebViewResultSent', 'UpdateWebViewResultSent'] = pydantic.Field(
        'types.UpdateWebViewResultSent',
        alias='_'
    )

    query_id: int
