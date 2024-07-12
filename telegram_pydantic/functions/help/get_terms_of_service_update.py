from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetTermsOfServiceUpdate(BaseModel):
    """
    functions.help.GetTermsOfServiceUpdate
    ID: 0x2ca51fd1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetTermsOfServiceUpdate', 'GetTermsOfServiceUpdate'] = pydantic.Field(
        'functions.help.GetTermsOfServiceUpdate',
        alias='_'
    )

