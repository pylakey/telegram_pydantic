from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageFwdHeader(BaseModel):
    """
    types.MessageFwdHeader
    ID: 0x4e4df4bb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageFwdHeader', 'MessageFwdHeader'] = pydantic.Field(
        'types.MessageFwdHeader',
        alias='_'
    )

    date: Datetime
    imported: typing.Optional[bool] = None
    saved_out: typing.Optional[bool] = None
    from_id: typing.Optional["base.Peer"] = None
    from_name: typing.Optional[str] = None
    channel_post: typing.Optional[int] = None
    post_author: typing.Optional[str] = None
    saved_from_peer: typing.Optional["base.Peer"] = None
    saved_from_msg_id: typing.Optional[int] = None
    saved_from_id: typing.Optional["base.Peer"] = None
    saved_from_name: typing.Optional[str] = None
    saved_date: Datetime
    psa_type: typing.Optional[str] = None
