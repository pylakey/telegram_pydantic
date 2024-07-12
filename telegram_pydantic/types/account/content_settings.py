from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ContentSettings(BaseModel):
    """
    types.account.ContentSettings
    ID: 0x57e28221
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ContentSettings', 'ContentSettings'] = pydantic.Field(
        'types.account.ContentSettings',
        alias='_'
    )

    sensitive_enabled: typing.Optional[bool] = None
    sensitive_can_change: typing.Optional[bool] = None
