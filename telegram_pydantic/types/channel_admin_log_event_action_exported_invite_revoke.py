from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ChannelAdminLogEventActionExportedInviteRevoke(BaseModel):
    """
    types.ChannelAdminLogEventActionExportedInviteRevoke
    ID: 0x410a134e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ChannelAdminLogEventActionExportedInviteRevoke', 'ChannelAdminLogEventActionExportedInviteRevoke'] = pydantic.Field(
        'types.ChannelAdminLogEventActionExportedInviteRevoke',
        alias='_'
    )

    invite: "base.ExportedChatInvite"
