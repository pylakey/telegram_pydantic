from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HidePeerSettingsBar(BaseModel):
    """
    functions.messages.HidePeerSettingsBar
    ID: 0x4facb138
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.HidePeerSettingsBar', 'HidePeerSettingsBar'] = pydantic.Field(
        'functions.messages.HidePeerSettingsBar',
        alias='_'
    )

    peer: "base.InputPeer"
