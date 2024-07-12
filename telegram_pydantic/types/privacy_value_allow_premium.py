from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowPremium(BaseModel):
    """
    types.PrivacyValueAllowPremium
    ID: 0xece9814b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowPremium', 'PrivacyValueAllowPremium'] = pydantic.Field(
        'types.PrivacyValueAllowPremium',
        alias='_'
    )

