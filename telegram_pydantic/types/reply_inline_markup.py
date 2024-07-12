from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ReplyInlineMarkup(BaseModel):
    """
    types.ReplyInlineMarkup
    ID: 0x48a30254
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ReplyInlineMarkup', 'ReplyInlineMarkup'] = pydantic.Field(
        'types.ReplyInlineMarkup',
        alias='_'
    )

    rows: list["base.KeyboardButtonRow"]
