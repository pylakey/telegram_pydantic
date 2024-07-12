from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Block(BaseModel):
    """
    functions.contacts.Block
    ID: 0x2e2e8734
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.Block', 'Block'] = pydantic.Field(
        'functions.contacts.Block',
        alias='_'
    )

    id: "base.InputPeer"
    my_stories_from: typing.Optional[bool] = None
