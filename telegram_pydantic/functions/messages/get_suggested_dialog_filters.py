from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetSuggestedDialogFilters(BaseModel):
    """
    functions.messages.GetSuggestedDialogFilters
    ID: 0xa29cd42c
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetSuggestedDialogFilters', 'GetSuggestedDialogFilters'] = pydantic.Field(
        'functions.messages.GetSuggestedDialogFilters',
        alias='_'
    )

