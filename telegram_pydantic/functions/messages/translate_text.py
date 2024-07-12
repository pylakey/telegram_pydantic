from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TranslateText(BaseModel):
    """
    functions.messages.TranslateText
    ID: 0x63183030
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.TranslateText', 'TranslateText'] = pydantic.Field(
        'functions.messages.TranslateText',
        alias='_'
    )

    to_lang: str
    peer: typing.Optional["base.InputPeer"] = None
    id: typing.Optional[list[int]] = None
    text: typing.Optional[list["base.TextWithEntities"]] = None
