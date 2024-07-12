from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionExportedInviteEdit(BaseModel):
    """
    types.ChannelAdminLogEventActionExportedInviteEdit
    ID: 0xe90ebb59
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionExportedInviteEdit', 'ChannelAdminLogEventActionExportedInviteEdit'] = pydantic.Field(
        'types.ChannelAdminLogEventActionExportedInviteEdit',
        alias='_'
    )

    prev_invite: "base.ExportedChatInvite"
    new_invite: "base.ExportedChatInvite"
