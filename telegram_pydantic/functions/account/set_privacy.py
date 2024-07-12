from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetPrivacy(BaseModel):
    """
    functions.account.SetPrivacy
    ID: 0xc9f81ce8
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SetPrivacy', 'SetPrivacy'] = pydantic.Field(
        'functions.account.SetPrivacy',
        alias='_'
    )

    key: "base.InputPrivacyKey"
    rules: list["base.InputPrivacyRule"]
