from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupsForDiscussion(BaseModel):
    """
    functions.channels.GetGroupsForDiscussion
    ID: 0xf5dad378
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.GetGroupsForDiscussion', 'GetGroupsForDiscussion'] = pydantic.Field(
        'functions.channels.GetGroupsForDiscussion',
        alias='_'
    )

