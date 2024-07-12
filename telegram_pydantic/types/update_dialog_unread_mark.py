from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDialogUnreadMark(BaseModel):
    """
    types.UpdateDialogUnreadMark
    ID: 0xe16459c3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDialogUnreadMark', 'UpdateDialogUnreadMark'] = pydantic.Field(
        'types.UpdateDialogUnreadMark',
        alias='_'
    )

    peer: "base.DialogPeer"
    unread: typing.Optional[bool] = None
