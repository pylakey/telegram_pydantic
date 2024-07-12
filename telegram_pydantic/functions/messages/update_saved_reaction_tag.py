from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateSavedReactionTag(BaseModel):
    """
    functions.messages.UpdateSavedReactionTag
    ID: 0x60297dec
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.UpdateSavedReactionTag', 'UpdateSavedReactionTag'] = pydantic.Field(
        'functions.messages.UpdateSavedReactionTag',
        alias='_'
    )

    reaction: "base.Reaction"
    title: typing.Optional[str] = None
