from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResolveUsername(BaseModel):
    """
    functions.contacts.ResolveUsername
    ID: 0xf93ccba3
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.ResolveUsername', 'ResolveUsername'] = pydantic.Field(
        'functions.contacts.ResolveUsername',
        alias='_'
    )

    username: str
