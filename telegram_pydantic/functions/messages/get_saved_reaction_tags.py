from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSavedReactionTags(BaseModel):
    """
    functions.messages.GetSavedReactionTags
    ID: 0x3637e05b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSavedReactionTags', 'GetSavedReactionTags'] = pydantic.Field(
        'functions.messages.GetSavedReactionTags',
        alias='_'
    )

    hash: int
    peer: typing.Optional["base.InputPeer"] = None
