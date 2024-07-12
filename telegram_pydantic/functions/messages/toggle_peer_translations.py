from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TogglePeerTranslations(BaseModel):
    """
    functions.messages.TogglePeerTranslations
    ID: 0xe47cb579
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.TogglePeerTranslations', 'TogglePeerTranslations'] = pydantic.Field(
        'functions.messages.TogglePeerTranslations',
        alias='_'
    )

    peer: "base.InputPeer"
    disabled: typing.Optional[bool] = None
