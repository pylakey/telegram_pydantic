from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyForwards(BaseModel):
    """
    types.PrivacyKeyForwards
    ID: 0x69ec56a3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyForwards', 'PrivacyKeyForwards'] = pydantic.Field(
        'types.PrivacyKeyForwards',
        alias='_'
    )

