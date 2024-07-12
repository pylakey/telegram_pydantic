from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AcceptContact(BaseModel):
    """
    functions.contacts.AcceptContact
    ID: 0xf831a20f
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.AcceptContact', 'AcceptContact'] = pydantic.Field(
        'functions.contacts.AcceptContact',
        alias='_'
    )

    id: "base.InputUser"
