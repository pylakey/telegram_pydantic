from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditBusinessChatLink(BaseModel):
    """
    functions.account.EditBusinessChatLink
    ID: 0x8c3410af
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.EditBusinessChatLink', 'EditBusinessChatLink'] = pydantic.Field(
        'functions.account.EditBusinessChatLink',
        alias='_'
    )

    slug: str
    link: "base.InputBusinessChatLink"
