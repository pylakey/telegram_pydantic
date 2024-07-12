from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPinnedDialogs(BaseModel):
    """
    functions.messages.GetPinnedDialogs
    ID: 0xd6b94df2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetPinnedDialogs', 'GetPinnedDialogs'] = pydantic.Field(
        'functions.messages.GetPinnedDialogs',
        alias='_'
    )

    folder_id: int
