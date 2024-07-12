from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyProfilePhoto(BaseModel):
    """
    types.PrivacyKeyProfilePhoto
    ID: 0x96151fed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyProfilePhoto', 'PrivacyKeyProfilePhoto'] = pydantic.Field(
        'types.PrivacyKeyProfilePhoto',
        alias='_'
    )

