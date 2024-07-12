from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveAutoDownloadSettings(BaseModel):
    """
    functions.account.SaveAutoDownloadSettings
    ID: 0x76f36233
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveAutoDownloadSettings', 'SaveAutoDownloadSettings'] = pydantic.Field(
        'functions.account.SaveAutoDownloadSettings',
        alias='_'
    )

    settings: "base.AutoDownloadSettings"
    low: typing.Optional[bool] = None
    high: typing.Optional[bool] = None
