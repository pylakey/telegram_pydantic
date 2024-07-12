from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class JoinGroupCallPresentation(BaseModel):
    """
    functions.phone.JoinGroupCallPresentation
    ID: 0xcbea6bc4
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.JoinGroupCallPresentation', 'JoinGroupCallPresentation'] = pydantic.Field(
        'functions.phone.JoinGroupCallPresentation',
        alias='_'
    )

    call: "base.InputGroupCall"
    params: "base.DataJSON"
