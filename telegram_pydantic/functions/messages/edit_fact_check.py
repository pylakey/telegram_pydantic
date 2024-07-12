from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditFactCheck(BaseModel):
    """
    functions.messages.EditFactCheck
    ID: 0x589ee75
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditFactCheck', 'EditFactCheck'] = pydantic.Field(
        'functions.messages.EditFactCheck',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
    text: "base.TextWithEntities"
