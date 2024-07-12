from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePrivacy(BaseModel):
    """
    types.UpdatePrivacy
    ID: 0xee3b272a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePrivacy', 'UpdatePrivacy'] = pydantic.Field(
        'types.UpdatePrivacy',
        alias='_'
    )

    key: "base.PrivacyKey"
    rules: list["base.PrivacyRule"]
