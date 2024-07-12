from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ToggleDialogFilterTags(BaseModel):
    """
    functions.messages.ToggleDialogFilterTags
    ID: 0xfd2dda49
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.ToggleDialogFilterTags', 'ToggleDialogFilterTags'] = pydantic.Field(
        'functions.messages.ToggleDialogFilterTags',
        alias='_'
    )

    enabled: bool
