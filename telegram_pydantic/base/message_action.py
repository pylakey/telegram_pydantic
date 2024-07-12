from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# MessageAction - Layer 181
MessageAction = typing.Annotated[
    typing.Union[
        typing.Annotated[types.MessageActionBoostApply, pydantic.Tag('MessageActionBoostApply')],
        typing.Annotated[types.MessageActionBotAllowed, pydantic.Tag('MessageActionBotAllowed')],
        typing.Annotated[types.MessageActionChannelCreate, pydantic.Tag('MessageActionChannelCreate')],
        typing.Annotated[types.MessageActionChannelMigrateFrom, pydantic.Tag('MessageActionChannelMigrateFrom')],
        typing.Annotated[types.MessageActionChatAddUser, pydantic.Tag('MessageActionChatAddUser')],
        typing.Annotated[types.MessageActionChatCreate, pydantic.Tag('MessageActionChatCreate')],
        typing.Annotated[types.MessageActionChatDeletePhoto, pydantic.Tag('MessageActionChatDeletePhoto')],
        typing.Annotated[types.MessageActionChatDeleteUser, pydantic.Tag('MessageActionChatDeleteUser')],
        typing.Annotated[types.MessageActionChatEditPhoto, pydantic.Tag('MessageActionChatEditPhoto')],
        typing.Annotated[types.MessageActionChatEditTitle, pydantic.Tag('MessageActionChatEditTitle')],
        typing.Annotated[types.MessageActionChatJoinedByLink, pydantic.Tag('MessageActionChatJoinedByLink')],
        typing.Annotated[types.MessageActionChatJoinedByRequest, pydantic.Tag('MessageActionChatJoinedByRequest')],
        typing.Annotated[types.MessageActionChatMigrateTo, pydantic.Tag('MessageActionChatMigrateTo')],
        typing.Annotated[types.MessageActionContactSignUp, pydantic.Tag('MessageActionContactSignUp')],
        typing.Annotated[types.MessageActionCustomAction, pydantic.Tag('MessageActionCustomAction')],
        typing.Annotated[types.MessageActionEmpty, pydantic.Tag('MessageActionEmpty')],
        typing.Annotated[types.MessageActionGameScore, pydantic.Tag('MessageActionGameScore')],
        typing.Annotated[types.MessageActionGeoProximityReached, pydantic.Tag('MessageActionGeoProximityReached')],
        typing.Annotated[types.MessageActionGiftCode, pydantic.Tag('MessageActionGiftCode')],
        typing.Annotated[types.MessageActionGiftPremium, pydantic.Tag('MessageActionGiftPremium')],
        typing.Annotated[types.MessageActionGiveawayLaunch, pydantic.Tag('MessageActionGiveawayLaunch')],
        typing.Annotated[types.MessageActionGiveawayResults, pydantic.Tag('MessageActionGiveawayResults')],
        typing.Annotated[types.MessageActionGroupCall, pydantic.Tag('MessageActionGroupCall')],
        typing.Annotated[types.MessageActionGroupCallScheduled, pydantic.Tag('MessageActionGroupCallScheduled')],
        typing.Annotated[types.MessageActionHistoryClear, pydantic.Tag('MessageActionHistoryClear')],
        typing.Annotated[types.MessageActionInviteToGroupCall, pydantic.Tag('MessageActionInviteToGroupCall')],
        typing.Annotated[types.MessageActionPaymentSent, pydantic.Tag('MessageActionPaymentSent')],
        typing.Annotated[types.MessageActionPaymentSentMe, pydantic.Tag('MessageActionPaymentSentMe')],
        typing.Annotated[types.MessageActionPhoneCall, pydantic.Tag('MessageActionPhoneCall')],
        typing.Annotated[types.MessageActionPinMessage, pydantic.Tag('MessageActionPinMessage')],
        typing.Annotated[types.MessageActionRequestedPeer, pydantic.Tag('MessageActionRequestedPeer')],
        typing.Annotated[types.MessageActionRequestedPeerSentMe, pydantic.Tag('MessageActionRequestedPeerSentMe')],
        typing.Annotated[types.MessageActionScreenshotTaken, pydantic.Tag('MessageActionScreenshotTaken')],
        typing.Annotated[types.MessageActionSecureValuesSent, pydantic.Tag('MessageActionSecureValuesSent')],
        typing.Annotated[types.MessageActionSecureValuesSentMe, pydantic.Tag('MessageActionSecureValuesSentMe')],
        typing.Annotated[types.MessageActionSetChatTheme, pydantic.Tag('MessageActionSetChatTheme')],
        typing.Annotated[types.MessageActionSetChatWallPaper, pydantic.Tag('MessageActionSetChatWallPaper')],
        typing.Annotated[types.MessageActionSetMessagesTTL, pydantic.Tag('MessageActionSetMessagesTTL')],
        typing.Annotated[types.MessageActionSuggestProfilePhoto, pydantic.Tag('MessageActionSuggestProfilePhoto')],
        typing.Annotated[types.MessageActionTopicCreate, pydantic.Tag('MessageActionTopicCreate')],
        typing.Annotated[types.MessageActionTopicEdit, pydantic.Tag('MessageActionTopicEdit')],
        typing.Annotated[types.MessageActionWebViewDataSent, pydantic.Tag('MessageActionWebViewDataSent')],
        typing.Annotated[types.MessageActionWebViewDataSentMe, pydantic.Tag('MessageActionWebViewDataSentMe')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
