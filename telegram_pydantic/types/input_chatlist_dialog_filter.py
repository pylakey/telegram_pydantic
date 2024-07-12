from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputChatlistDialogFilter(BaseModel):
    """
    types.InputChatlistDialogFilter
    ID: 0xf3e0da33
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputChatlistDialogFilter', 'InputChatlistDialogFilter'] = pydantic.Field(
        'types.InputChatlistDialogFilter',
        alias='_'
    )

    filter_id: int
