from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ActivateStealthMode(BaseModel):
    """
    functions.stories.ActivateStealthMode
    ID: 0x57bbd166
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.ActivateStealthMode', 'ActivateStealthMode'] = pydantic.Field(
        'functions.stories.ActivateStealthMode',
        alias='_'
    )

    past: typing.Optional[bool] = None
    future: typing.Optional[bool] = None
