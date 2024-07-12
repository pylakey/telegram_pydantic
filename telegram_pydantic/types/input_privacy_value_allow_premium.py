from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowPremium(BaseModel):
    """
    types.InputPrivacyValueAllowPremium
    ID: 0x77cdc9f1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowPremium', 'InputPrivacyValueAllowPremium'] = pydantic.Field(
        'types.InputPrivacyValueAllowPremium',
        alias='_'
    )

