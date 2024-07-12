from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetDiscussionGroup(BaseModel):
    """
    functions.channels.SetDiscussionGroup
    ID: 0x40582bb2
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.SetDiscussionGroup', 'SetDiscussionGroup'] = pydantic.Field(
        'functions.channels.SetDiscussionGroup',
        alias='_'
    )

    broadcast: "base.InputChannel"
    group: "base.InputChannel"
