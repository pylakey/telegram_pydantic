from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputNotifyForumTopic(BaseModel):
    """
    types.InputNotifyForumTopic
    ID: 0x5c467992
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputNotifyForumTopic', 'InputNotifyForumTopic'] = pydantic.Field(
        'types.InputNotifyForumTopic',
        alias='_'
    )

    peer: "base.InputPeer"
    top_msg_id: int
