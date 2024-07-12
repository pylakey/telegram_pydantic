from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SponsoredMessagesEmpty(BaseModel):
    """
    types.messages.SponsoredMessagesEmpty
    ID: 0x1839490f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.SponsoredMessagesEmpty', 'SponsoredMessagesEmpty'] = pydantic.Field(
        'types.messages.SponsoredMessagesEmpty',
        alias='_'
    )

