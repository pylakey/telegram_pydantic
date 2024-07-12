from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetAuthorizations(BaseModel):
    """
    functions.auth.ResetAuthorizations
    ID: 0x9fab0d1a
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.auth.ResetAuthorizations', 'ResetAuthorizations'] = pydantic.Field(
        'functions.auth.ResetAuthorizations',
        alias='_'
    )

