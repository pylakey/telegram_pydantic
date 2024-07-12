from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeactivateAllUsernames(BaseModel):
    """
    functions.channels.DeactivateAllUsernames
    ID: 0xa245dd3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.DeactivateAllUsernames', 'DeactivateAllUsernames'] = pydantic.Field(
        'functions.channels.DeactivateAllUsernames',
        alias='_'
    )

    channel: "base.InputChannel"
