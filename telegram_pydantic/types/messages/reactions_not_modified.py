from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReactionsNotModified(BaseModel):
    """
    types.messages.ReactionsNotModified
    ID: 0xb06fdbdf
    Layer: 181
    """
    QUALNAME: typing.Literal['types.messages.ReactionsNotModified', 'ReactionsNotModified'] = pydantic.Field(
        'types.messages.ReactionsNotModified',
        alias='_'
    )

