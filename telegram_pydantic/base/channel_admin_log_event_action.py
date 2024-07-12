from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ChannelAdminLogEventAction - Layer 181
ChannelAdminLogEventAction = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ChannelAdminLogEventActionChangeAbout, pydantic.Tag('ChannelAdminLogEventActionChangeAbout')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeAvailableReactions, pydantic.Tag('ChannelAdminLogEventActionChangeAvailableReactions')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeEmojiStatus, pydantic.Tag('ChannelAdminLogEventActionChangeEmojiStatus')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeEmojiStickerSet, pydantic.Tag('ChannelAdminLogEventActionChangeEmojiStickerSet')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeHistoryTTL, pydantic.Tag('ChannelAdminLogEventActionChangeHistoryTTL')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeLinkedChat, pydantic.Tag('ChannelAdminLogEventActionChangeLinkedChat')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeLocation, pydantic.Tag('ChannelAdminLogEventActionChangeLocation')],
        typing.Annotated[types.ChannelAdminLogEventActionChangePeerColor, pydantic.Tag('ChannelAdminLogEventActionChangePeerColor')],
        typing.Annotated[types.ChannelAdminLogEventActionChangePhoto, pydantic.Tag('ChannelAdminLogEventActionChangePhoto')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeProfilePeerColor, pydantic.Tag('ChannelAdminLogEventActionChangeProfilePeerColor')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeStickerSet, pydantic.Tag('ChannelAdminLogEventActionChangeStickerSet')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeTitle, pydantic.Tag('ChannelAdminLogEventActionChangeTitle')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeUsername, pydantic.Tag('ChannelAdminLogEventActionChangeUsername')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeUsernames, pydantic.Tag('ChannelAdminLogEventActionChangeUsernames')],
        typing.Annotated[types.ChannelAdminLogEventActionChangeWallpaper, pydantic.Tag('ChannelAdminLogEventActionChangeWallpaper')],
        typing.Annotated[types.ChannelAdminLogEventActionCreateTopic, pydantic.Tag('ChannelAdminLogEventActionCreateTopic')],
        typing.Annotated[types.ChannelAdminLogEventActionDefaultBannedRights, pydantic.Tag('ChannelAdminLogEventActionDefaultBannedRights')],
        typing.Annotated[types.ChannelAdminLogEventActionDeleteMessage, pydantic.Tag('ChannelAdminLogEventActionDeleteMessage')],
        typing.Annotated[types.ChannelAdminLogEventActionDeleteTopic, pydantic.Tag('ChannelAdminLogEventActionDeleteTopic')],
        typing.Annotated[types.ChannelAdminLogEventActionDiscardGroupCall, pydantic.Tag('ChannelAdminLogEventActionDiscardGroupCall')],
        typing.Annotated[types.ChannelAdminLogEventActionEditMessage, pydantic.Tag('ChannelAdminLogEventActionEditMessage')],
        typing.Annotated[types.ChannelAdminLogEventActionEditTopic, pydantic.Tag('ChannelAdminLogEventActionEditTopic')],
        typing.Annotated[types.ChannelAdminLogEventActionExportedInviteDelete, pydantic.Tag('ChannelAdminLogEventActionExportedInviteDelete')],
        typing.Annotated[types.ChannelAdminLogEventActionExportedInviteEdit, pydantic.Tag('ChannelAdminLogEventActionExportedInviteEdit')],
        typing.Annotated[types.ChannelAdminLogEventActionExportedInviteRevoke, pydantic.Tag('ChannelAdminLogEventActionExportedInviteRevoke')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantInvite, pydantic.Tag('ChannelAdminLogEventActionParticipantInvite')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantJoin, pydantic.Tag('ChannelAdminLogEventActionParticipantJoin')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantJoinByInvite, pydantic.Tag('ChannelAdminLogEventActionParticipantJoinByInvite')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantJoinByRequest, pydantic.Tag('ChannelAdminLogEventActionParticipantJoinByRequest')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantLeave, pydantic.Tag('ChannelAdminLogEventActionParticipantLeave')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantMute, pydantic.Tag('ChannelAdminLogEventActionParticipantMute')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantToggleAdmin, pydantic.Tag('ChannelAdminLogEventActionParticipantToggleAdmin')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantToggleBan, pydantic.Tag('ChannelAdminLogEventActionParticipantToggleBan')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantUnmute, pydantic.Tag('ChannelAdminLogEventActionParticipantUnmute')],
        typing.Annotated[types.ChannelAdminLogEventActionParticipantVolume, pydantic.Tag('ChannelAdminLogEventActionParticipantVolume')],
        typing.Annotated[types.ChannelAdminLogEventActionPinTopic, pydantic.Tag('ChannelAdminLogEventActionPinTopic')],
        typing.Annotated[types.ChannelAdminLogEventActionSendMessage, pydantic.Tag('ChannelAdminLogEventActionSendMessage')],
        typing.Annotated[types.ChannelAdminLogEventActionStartGroupCall, pydantic.Tag('ChannelAdminLogEventActionStartGroupCall')],
        typing.Annotated[types.ChannelAdminLogEventActionStopPoll, pydantic.Tag('ChannelAdminLogEventActionStopPoll')],
        typing.Annotated[types.ChannelAdminLogEventActionToggleAntiSpam, pydantic.Tag('ChannelAdminLogEventActionToggleAntiSpam')],
        typing.Annotated[types.ChannelAdminLogEventActionToggleForum, pydantic.Tag('ChannelAdminLogEventActionToggleForum')],
        typing.Annotated[types.ChannelAdminLogEventActionToggleGroupCallSetting, pydantic.Tag('ChannelAdminLogEventActionToggleGroupCallSetting')],
        typing.Annotated[types.ChannelAdminLogEventActionToggleInvites, pydantic.Tag('ChannelAdminLogEventActionToggleInvites')],
        typing.Annotated[types.ChannelAdminLogEventActionToggleNoForwards, pydantic.Tag('ChannelAdminLogEventActionToggleNoForwards')],
        typing.Annotated[types.ChannelAdminLogEventActionTogglePreHistoryHidden, pydantic.Tag('ChannelAdminLogEventActionTogglePreHistoryHidden')],
        typing.Annotated[types.ChannelAdminLogEventActionToggleSignatures, pydantic.Tag('ChannelAdminLogEventActionToggleSignatures')],
        typing.Annotated[types.ChannelAdminLogEventActionToggleSlowMode, pydantic.Tag('ChannelAdminLogEventActionToggleSlowMode')],
        typing.Annotated[types.ChannelAdminLogEventActionUpdatePinned, pydantic.Tag('ChannelAdminLogEventActionUpdatePinned')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
