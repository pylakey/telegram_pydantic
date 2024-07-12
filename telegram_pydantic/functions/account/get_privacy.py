from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPrivacy(BaseModel):
    """
    functions.account.GetPrivacy
    ID: 0xdadbc950
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetPrivacy', 'GetPrivacy'] = pydantic.Field(
        'functions.account.GetPrivacy',
        alias='_'
    )

    key: "base.InputPrivacyKey"
