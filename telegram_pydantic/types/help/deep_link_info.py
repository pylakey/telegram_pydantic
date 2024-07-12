from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeepLinkInfo(BaseModel):
    """
    types.help.DeepLinkInfo
    ID: 0x6a4ee832
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.DeepLinkInfo', 'DeepLinkInfo'] = pydantic.Field(
        'types.help.DeepLinkInfo',
        alias='_'
    )

    message: str
    update_app: typing.Optional[bool] = None
    entities: typing.Optional[list["base.MessageEntity"]] = None
