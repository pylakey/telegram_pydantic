from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AutoDownloadSettings(BaseModel):
    """
    types.account.AutoDownloadSettings
    ID: 0x63cacf26
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.AutoDownloadSettings', 'AutoDownloadSettings'] = pydantic.Field(
        'types.account.AutoDownloadSettings',
        alias='_'
    )

    low: "base.AutoDownloadSettings"
    medium: "base.AutoDownloadSettings"
    high: "base.AutoDownloadSettings"
