from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateDraftMessage(BaseModel):
    """
    types.UpdateDraftMessage
    ID: 0x1b49ec6d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateDraftMessage', 'UpdateDraftMessage'] = pydantic.Field(
        'types.UpdateDraftMessage',
        alias='_'
    )

    peer: "base.Peer"
    draft: "base.DraftMessage"
    top_msg_id: typing.Optional[int] = None
