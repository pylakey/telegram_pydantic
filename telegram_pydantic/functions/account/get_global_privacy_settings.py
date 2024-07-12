from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGlobalPrivacySettings(BaseModel):
    """
    functions.account.GetGlobalPrivacySettings
    ID: 0xeb2b4cf6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetGlobalPrivacySettings', 'GetGlobalPrivacySettings'] = pydantic.Field(
        'functions.account.GetGlobalPrivacySettings',
        alias='_'
    )

