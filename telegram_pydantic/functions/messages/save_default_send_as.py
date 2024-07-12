from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveDefaultSendAs(BaseModel):
    """
    functions.messages.SaveDefaultSendAs
    ID: 0xccfddf96
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SaveDefaultSendAs', 'SaveDefaultSendAs'] = pydantic.Field(
        'functions.messages.SaveDefaultSendAs',
        alias='_'
    )

    peer: "base.InputPeer"
    send_as: "base.InputPeer"
