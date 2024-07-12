from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DialogFilter(BaseModel):
    """
    types.DialogFilter
    ID: 0x5fb5523b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.DialogFilter', 'DialogFilter'] = pydantic.Field(
        'types.DialogFilter',
        alias='_'
    )

    id: int
    title: str
    pinned_peers: list["base.InputPeer"]
    include_peers: list["base.InputPeer"]
    exclude_peers: list["base.InputPeer"]
    contacts: typing.Optional[bool] = None
    non_contacts: typing.Optional[bool] = None
    groups: typing.Optional[bool] = None
    broadcasts: typing.Optional[bool] = None
    bots: typing.Optional[bool] = None
    exclude_muted: typing.Optional[bool] = None
    exclude_read: typing.Optional[bool] = None
    exclude_archived: typing.Optional[bool] = None
    emoticon: typing.Optional[str] = None
    color: typing.Optional[int] = None
