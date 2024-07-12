from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetGlobalPrivacySettings(BaseModel):
    """
    functions.account.SetGlobalPrivacySettings
    ID: 0x1edaaac2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetGlobalPrivacySettings', 'SetGlobalPrivacySettings'] = pydantic.Field(
        'functions.account.SetGlobalPrivacySettings',
        alias='_'
    )

    settings: "base.GlobalPrivacySettings"
