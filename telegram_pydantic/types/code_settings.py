from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CodeSettings(BaseModel):
    """
    types.CodeSettings
    ID: 0xad253d78
    Layer: 181
    """
    QUALNAME: typing.Literal['types.CodeSettings', 'CodeSettings'] = pydantic.Field(
        'types.CodeSettings',
        alias='_'
    )

    allow_flashcall: typing.Optional[bool] = None
    current_number: typing.Optional[bool] = None
    allow_app_hash: typing.Optional[bool] = None
    allow_missed_call: typing.Optional[bool] = None
    allow_firebase: typing.Optional[bool] = None
    unknown_number: typing.Optional[bool] = None
    logout_tokens: typing.Optional[list[Bytes]] = None
    token: typing.Optional[str] = None
    app_sandbox: typing.Optional[bool] = None
