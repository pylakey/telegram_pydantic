from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DismissSuggestion(BaseModel):
    """
    functions.help.DismissSuggestion
    ID: 0xf50dbaa1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.DismissSuggestion', 'DismissSuggestion'] = pydantic.Field(
        'functions.help.DismissSuggestion',
        alias='_'
    )

    peer: "base.InputPeer"
    suggestion: str
