from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdatePinnedDialogs(BaseModel):
    """
    types.UpdatePinnedDialogs
    ID: 0xfa0f3ca2
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdatePinnedDialogs', 'UpdatePinnedDialogs'] = pydantic.Field(
        'types.UpdatePinnedDialogs',
        alias='_'
    )

    folder_id: typing.Optional[int] = None
    order: typing.Optional[list["base.DialogPeer"]] = None
