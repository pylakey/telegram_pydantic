from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateAttachMenuBots(BaseModel):
    """
    types.UpdateAttachMenuBots
    ID: 0x17b7a20b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateAttachMenuBots', 'UpdateAttachMenuBots'] = pydantic.Field(
        'types.UpdateAttachMenuBots',
        alias='_'
    )

