from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditChatAbout(BaseModel):
    """
    functions.messages.EditChatAbout
    ID: 0xdef60797
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.EditChatAbout', 'EditChatAbout'] = pydantic.Field(
        'functions.messages.EditChatAbout',
        alias='_'
    )

    peer: "base.InputPeer"
    about: str
