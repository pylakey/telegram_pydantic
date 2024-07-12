from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyPhoneCall(BaseModel):
    """
    types.PrivacyKeyPhoneCall
    ID: 0x3d662b7b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyPhoneCall', 'PrivacyKeyPhoneCall'] = pydantic.Field(
        'types.PrivacyKeyPhoneCall',
        alias='_'
    )

