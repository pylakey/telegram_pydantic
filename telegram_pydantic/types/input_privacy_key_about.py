from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyAbout(BaseModel):
    """
    types.InputPrivacyKeyAbout
    ID: 0x3823cc40
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyAbout', 'InputPrivacyKeyAbout'] = pydantic.Field(
        'types.InputPrivacyKeyAbout',
        alias='_'
    )

