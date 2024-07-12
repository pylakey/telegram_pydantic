from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleGroupCallSettings(BaseModel):
    """
    functions.phone.ToggleGroupCallSettings
    ID: 0x74bbb43d
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.ToggleGroupCallSettings', 'ToggleGroupCallSettings'] = pydantic.Field(
        'functions.phone.ToggleGroupCallSettings',
        alias='_'
    )

    call: "base.InputGroupCall"
    reset_invite_hash: typing.Optional[bool] = None
    join_muted: typing.Optional[bool] = None
