from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyKeyForwards(BaseModel):
    """
    types.InputPrivacyKeyForwards
    ID: 0xa4dd4c08
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyKeyForwards', 'InputPrivacyKeyForwards'] = pydantic.Field(
        'types.InputPrivacyKeyForwards',
        alias='_'
    )

