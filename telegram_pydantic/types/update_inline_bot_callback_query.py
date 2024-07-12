from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateInlineBotCallbackQuery(BaseModel):
    """
    types.UpdateInlineBotCallbackQuery
    ID: 0x691e9052
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateInlineBotCallbackQuery', 'UpdateInlineBotCallbackQuery'] = pydantic.Field(
        'types.UpdateInlineBotCallbackQuery',
        alias='_'
    )

    query_id: int
    user_id: int
    msg_id: "base.InputBotInlineMessageID"
    chat_instance: int
    data: typing.Optional[Bytes] = None
    game_short_name: typing.Optional[str] = None
