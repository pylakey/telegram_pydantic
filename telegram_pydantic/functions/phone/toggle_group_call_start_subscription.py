from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleGroupCallStartSubscription(BaseModel):
    """
    functions.phone.ToggleGroupCallStartSubscription
    ID: 0x219c34e6
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ToggleGroupCallStartSubscription', 'ToggleGroupCallStartSubscription'] = pydantic.Field(
        'functions.phone.ToggleGroupCallStartSubscription',
        alias='_'
    )

    call: "base.InputGroupCall"
    subscribed: bool
