from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Folder(BaseModel):
    """
    types.Folder
    ID: 0xff544e65
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Folder', 'Folder'] = pydantic.Field(
        'types.Folder',
        alias='_'
    )

    id: int
    title: str
    autofill_new_broadcasts: typing.Optional[bool] = None
    autofill_public_groups: typing.Optional[bool] = None
    autofill_new_correspondents: typing.Optional[bool] = None
    photo: typing.Optional["base.ChatPhoto"] = None
