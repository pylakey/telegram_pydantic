from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DhConfigNotModified(BaseModel):
    """
    types.messages.DhConfigNotModified
    ID: 0xc0e24635
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.DhConfigNotModified', 'DhConfigNotModified'] = pydantic.Field(
        'types.messages.DhConfigNotModified',
        alias='_'
    )

    random: Bytes
