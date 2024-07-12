from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AvailableReactionsNotModified(BaseModel):
    """
    types.messages.AvailableReactionsNotModified
    ID: 0x9f071957
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.AvailableReactionsNotModified', 'AvailableReactionsNotModified'] = pydantic.Field(
        'types.messages.AvailableReactionsNotModified',
        alias='_'
    )

