from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Update - Layer 181
Update = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.UpdateAttachMenuBots,
            pydantic.Tag('UpdateAttachMenuBots')        ],
        typing.Annotated[
            types.UpdateAutoSaveSettings,
            pydantic.Tag('UpdateAutoSaveSettings')        ],
        typing.Annotated[
            types.UpdateBotBusinessConnect,
            pydantic.Tag('UpdateBotBusinessConnect')        ],
        typing.Annotated[
            types.UpdateBotCallbackQuery,
            pydantic.Tag('UpdateBotCallbackQuery')        ],
        typing.Annotated[
            types.UpdateBotChatBoost,
            pydantic.Tag('UpdateBotChatBoost')        ],
        typing.Annotated[
            types.UpdateBotChatInviteRequester,
            pydantic.Tag('UpdateBotChatInviteRequester')        ],
        typing.Annotated[
            types.UpdateBotCommands,
            pydantic.Tag('UpdateBotCommands')        ],
        typing.Annotated[
            types.UpdateBotDeleteBusinessMessage,
            pydantic.Tag('UpdateBotDeleteBusinessMessage')        ],
        typing.Annotated[
            types.UpdateBotEditBusinessMessage,
            pydantic.Tag('UpdateBotEditBusinessMessage')        ],
        typing.Annotated[
            types.UpdateBotInlineQuery,
            pydantic.Tag('UpdateBotInlineQuery')        ],
        typing.Annotated[
            types.UpdateBotInlineSend,
            pydantic.Tag('UpdateBotInlineSend')        ],
        typing.Annotated[
            types.UpdateBotMenuButton,
            pydantic.Tag('UpdateBotMenuButton')        ],
        typing.Annotated[
            types.UpdateBotMessageReaction,
            pydantic.Tag('UpdateBotMessageReaction')        ],
        typing.Annotated[
            types.UpdateBotMessageReactions,
            pydantic.Tag('UpdateBotMessageReactions')        ],
        typing.Annotated[
            types.UpdateBotNewBusinessMessage,
            pydantic.Tag('UpdateBotNewBusinessMessage')        ],
        typing.Annotated[
            types.UpdateBotPrecheckoutQuery,
            pydantic.Tag('UpdateBotPrecheckoutQuery')        ],
        typing.Annotated[
            types.UpdateBotShippingQuery,
            pydantic.Tag('UpdateBotShippingQuery')        ],
        typing.Annotated[
            types.UpdateBotStopped,
            pydantic.Tag('UpdateBotStopped')        ],
        typing.Annotated[
            types.UpdateBotWebhookJSON,
            pydantic.Tag('UpdateBotWebhookJSON')        ],
        typing.Annotated[
            types.UpdateBotWebhookJSONQuery,
            pydantic.Tag('UpdateBotWebhookJSONQuery')        ],
        typing.Annotated[
            types.UpdateBroadcastRevenueTransactions,
            pydantic.Tag('UpdateBroadcastRevenueTransactions')        ],
        typing.Annotated[
            types.UpdateChannel,
            pydantic.Tag('UpdateChannel')        ],
        typing.Annotated[
            types.UpdateChannelAvailableMessages,
            pydantic.Tag('UpdateChannelAvailableMessages')        ],
        typing.Annotated[
            types.UpdateChannelMessageForwards,
            pydantic.Tag('UpdateChannelMessageForwards')        ],
        typing.Annotated[
            types.UpdateChannelMessageViews,
            pydantic.Tag('UpdateChannelMessageViews')        ],
        typing.Annotated[
            types.UpdateChannelParticipant,
            pydantic.Tag('UpdateChannelParticipant')        ],
        typing.Annotated[
            types.UpdateChannelPinnedTopic,
            pydantic.Tag('UpdateChannelPinnedTopic')        ],
        typing.Annotated[
            types.UpdateChannelPinnedTopics,
            pydantic.Tag('UpdateChannelPinnedTopics')        ],
        typing.Annotated[
            types.UpdateChannelReadMessagesContents,
            pydantic.Tag('UpdateChannelReadMessagesContents')        ],
        typing.Annotated[
            types.UpdateChannelTooLong,
            pydantic.Tag('UpdateChannelTooLong')        ],
        typing.Annotated[
            types.UpdateChannelUserTyping,
            pydantic.Tag('UpdateChannelUserTyping')        ],
        typing.Annotated[
            types.UpdateChannelViewForumAsMessages,
            pydantic.Tag('UpdateChannelViewForumAsMessages')        ],
        typing.Annotated[
            types.UpdateChannelWebPage,
            pydantic.Tag('UpdateChannelWebPage')        ],
        typing.Annotated[
            types.UpdateChat,
            pydantic.Tag('UpdateChat')        ],
        typing.Annotated[
            types.UpdateChatDefaultBannedRights,
            pydantic.Tag('UpdateChatDefaultBannedRights')        ],
        typing.Annotated[
            types.UpdateChatParticipant,
            pydantic.Tag('UpdateChatParticipant')        ],
        typing.Annotated[
            types.UpdateChatParticipantAdd,
            pydantic.Tag('UpdateChatParticipantAdd')        ],
        typing.Annotated[
            types.UpdateChatParticipantAdmin,
            pydantic.Tag('UpdateChatParticipantAdmin')        ],
        typing.Annotated[
            types.UpdateChatParticipantDelete,
            pydantic.Tag('UpdateChatParticipantDelete')        ],
        typing.Annotated[
            types.UpdateChatParticipants,
            pydantic.Tag('UpdateChatParticipants')        ],
        typing.Annotated[
            types.UpdateChatUserTyping,
            pydantic.Tag('UpdateChatUserTyping')        ],
        typing.Annotated[
            types.UpdateConfig,
            pydantic.Tag('UpdateConfig')        ],
        typing.Annotated[
            types.UpdateContactsReset,
            pydantic.Tag('UpdateContactsReset')        ],
        typing.Annotated[
            types.UpdateDcOptions,
            pydantic.Tag('UpdateDcOptions')        ],
        typing.Annotated[
            types.UpdateDeleteChannelMessages,
            pydantic.Tag('UpdateDeleteChannelMessages')        ],
        typing.Annotated[
            types.UpdateDeleteMessages,
            pydantic.Tag('UpdateDeleteMessages')        ],
        typing.Annotated[
            types.UpdateDeleteQuickReply,
            pydantic.Tag('UpdateDeleteQuickReply')        ],
        typing.Annotated[
            types.UpdateDeleteQuickReplyMessages,
            pydantic.Tag('UpdateDeleteQuickReplyMessages')        ],
        typing.Annotated[
            types.UpdateDeleteScheduledMessages,
            pydantic.Tag('UpdateDeleteScheduledMessages')        ],
        typing.Annotated[
            types.UpdateDialogFilter,
            pydantic.Tag('UpdateDialogFilter')        ],
        typing.Annotated[
            types.UpdateDialogFilterOrder,
            pydantic.Tag('UpdateDialogFilterOrder')        ],
        typing.Annotated[
            types.UpdateDialogFilters,
            pydantic.Tag('UpdateDialogFilters')        ],
        typing.Annotated[
            types.UpdateDialogPinned,
            pydantic.Tag('UpdateDialogPinned')        ],
        typing.Annotated[
            types.UpdateDialogUnreadMark,
            pydantic.Tag('UpdateDialogUnreadMark')        ],
        typing.Annotated[
            types.UpdateDraftMessage,
            pydantic.Tag('UpdateDraftMessage')        ],
        typing.Annotated[
            types.UpdateEditChannelMessage,
            pydantic.Tag('UpdateEditChannelMessage')        ],
        typing.Annotated[
            types.UpdateEditMessage,
            pydantic.Tag('UpdateEditMessage')        ],
        typing.Annotated[
            types.UpdateEncryptedChatTyping,
            pydantic.Tag('UpdateEncryptedChatTyping')        ],
        typing.Annotated[
            types.UpdateEncryptedMessagesRead,
            pydantic.Tag('UpdateEncryptedMessagesRead')        ],
        typing.Annotated[
            types.UpdateEncryption,
            pydantic.Tag('UpdateEncryption')        ],
        typing.Annotated[
            types.UpdateFavedStickers,
            pydantic.Tag('UpdateFavedStickers')        ],
        typing.Annotated[
            types.UpdateFolderPeers,
            pydantic.Tag('UpdateFolderPeers')        ],
        typing.Annotated[
            types.UpdateGeoLiveViewed,
            pydantic.Tag('UpdateGeoLiveViewed')        ],
        typing.Annotated[
            types.UpdateGroupCall,
            pydantic.Tag('UpdateGroupCall')        ],
        typing.Annotated[
            types.UpdateGroupCallConnection,
            pydantic.Tag('UpdateGroupCallConnection')        ],
        typing.Annotated[
            types.UpdateGroupCallParticipants,
            pydantic.Tag('UpdateGroupCallParticipants')        ],
        typing.Annotated[
            types.UpdateInlineBotCallbackQuery,
            pydantic.Tag('UpdateInlineBotCallbackQuery')        ],
        typing.Annotated[
            types.UpdateLangPack,
            pydantic.Tag('UpdateLangPack')        ],
        typing.Annotated[
            types.UpdateLangPackTooLong,
            pydantic.Tag('UpdateLangPackTooLong')        ],
        typing.Annotated[
            types.UpdateLoginToken,
            pydantic.Tag('UpdateLoginToken')        ],
        typing.Annotated[
            types.UpdateMessageExtendedMedia,
            pydantic.Tag('UpdateMessageExtendedMedia')        ],
        typing.Annotated[
            types.UpdateMessageID,
            pydantic.Tag('UpdateMessageID')        ],
        typing.Annotated[
            types.UpdateMessagePoll,
            pydantic.Tag('UpdateMessagePoll')        ],
        typing.Annotated[
            types.UpdateMessagePollVote,
            pydantic.Tag('UpdateMessagePollVote')        ],
        typing.Annotated[
            types.UpdateMessageReactions,
            pydantic.Tag('UpdateMessageReactions')        ],
        typing.Annotated[
            types.UpdateMoveStickerSetToTop,
            pydantic.Tag('UpdateMoveStickerSetToTop')        ],
        typing.Annotated[
            types.UpdateNewAuthorization,
            pydantic.Tag('UpdateNewAuthorization')        ],
        typing.Annotated[
            types.UpdateNewChannelMessage,
            pydantic.Tag('UpdateNewChannelMessage')        ],
        typing.Annotated[
            types.UpdateNewEncryptedMessage,
            pydantic.Tag('UpdateNewEncryptedMessage')        ],
        typing.Annotated[
            types.UpdateNewMessage,
            pydantic.Tag('UpdateNewMessage')        ],
        typing.Annotated[
            types.UpdateNewQuickReply,
            pydantic.Tag('UpdateNewQuickReply')        ],
        typing.Annotated[
            types.UpdateNewScheduledMessage,
            pydantic.Tag('UpdateNewScheduledMessage')        ],
        typing.Annotated[
            types.UpdateNewStickerSet,
            pydantic.Tag('UpdateNewStickerSet')        ],
        typing.Annotated[
            types.UpdateNewStoryReaction,
            pydantic.Tag('UpdateNewStoryReaction')        ],
        typing.Annotated[
            types.UpdateNotifySettings,
            pydantic.Tag('UpdateNotifySettings')        ],
        typing.Annotated[
            types.UpdatePeerBlocked,
            pydantic.Tag('UpdatePeerBlocked')        ],
        typing.Annotated[
            types.UpdatePeerHistoryTTL,
            pydantic.Tag('UpdatePeerHistoryTTL')        ],
        typing.Annotated[
            types.UpdatePeerLocated,
            pydantic.Tag('UpdatePeerLocated')        ],
        typing.Annotated[
            types.UpdatePeerSettings,
            pydantic.Tag('UpdatePeerSettings')        ],
        typing.Annotated[
            types.UpdatePeerWallpaper,
            pydantic.Tag('UpdatePeerWallpaper')        ],
        typing.Annotated[
            types.UpdatePendingJoinRequests,
            pydantic.Tag('UpdatePendingJoinRequests')        ],
        typing.Annotated[
            types.UpdatePhoneCall,
            pydantic.Tag('UpdatePhoneCall')        ],
        typing.Annotated[
            types.UpdatePhoneCallSignalingData,
            pydantic.Tag('UpdatePhoneCallSignalingData')        ],
        typing.Annotated[
            types.UpdatePinnedChannelMessages,
            pydantic.Tag('UpdatePinnedChannelMessages')        ],
        typing.Annotated[
            types.UpdatePinnedDialogs,
            pydantic.Tag('UpdatePinnedDialogs')        ],
        typing.Annotated[
            types.UpdatePinnedMessages,
            pydantic.Tag('UpdatePinnedMessages')        ],
        typing.Annotated[
            types.UpdatePinnedSavedDialogs,
            pydantic.Tag('UpdatePinnedSavedDialogs')        ],
        typing.Annotated[
            types.UpdatePrivacy,
            pydantic.Tag('UpdatePrivacy')        ],
        typing.Annotated[
            types.UpdatePtsChanged,
            pydantic.Tag('UpdatePtsChanged')        ],
        typing.Annotated[
            types.UpdateQuickReplies,
            pydantic.Tag('UpdateQuickReplies')        ],
        typing.Annotated[
            types.UpdateQuickReplyMessage,
            pydantic.Tag('UpdateQuickReplyMessage')        ],
        typing.Annotated[
            types.UpdateReadChannelDiscussionInbox,
            pydantic.Tag('UpdateReadChannelDiscussionInbox')        ],
        typing.Annotated[
            types.UpdateReadChannelDiscussionOutbox,
            pydantic.Tag('UpdateReadChannelDiscussionOutbox')        ],
        typing.Annotated[
            types.UpdateReadChannelInbox,
            pydantic.Tag('UpdateReadChannelInbox')        ],
        typing.Annotated[
            types.UpdateReadChannelOutbox,
            pydantic.Tag('UpdateReadChannelOutbox')        ],
        typing.Annotated[
            types.UpdateReadFeaturedEmojiStickers,
            pydantic.Tag('UpdateReadFeaturedEmojiStickers')        ],
        typing.Annotated[
            types.UpdateReadFeaturedStickers,
            pydantic.Tag('UpdateReadFeaturedStickers')        ],
        typing.Annotated[
            types.UpdateReadHistoryInbox,
            pydantic.Tag('UpdateReadHistoryInbox')        ],
        typing.Annotated[
            types.UpdateReadHistoryOutbox,
            pydantic.Tag('UpdateReadHistoryOutbox')        ],
        typing.Annotated[
            types.UpdateReadMessagesContents,
            pydantic.Tag('UpdateReadMessagesContents')        ],
        typing.Annotated[
            types.UpdateReadStories,
            pydantic.Tag('UpdateReadStories')        ],
        typing.Annotated[
            types.UpdateRecentEmojiStatuses,
            pydantic.Tag('UpdateRecentEmojiStatuses')        ],
        typing.Annotated[
            types.UpdateRecentReactions,
            pydantic.Tag('UpdateRecentReactions')        ],
        typing.Annotated[
            types.UpdateRecentStickers,
            pydantic.Tag('UpdateRecentStickers')        ],
        typing.Annotated[
            types.UpdateSavedDialogPinned,
            pydantic.Tag('UpdateSavedDialogPinned')        ],
        typing.Annotated[
            types.UpdateSavedGifs,
            pydantic.Tag('UpdateSavedGifs')        ],
        typing.Annotated[
            types.UpdateSavedReactionTags,
            pydantic.Tag('UpdateSavedReactionTags')        ],
        typing.Annotated[
            types.UpdateSavedRingtones,
            pydantic.Tag('UpdateSavedRingtones')        ],
        typing.Annotated[
            types.UpdateSentStoryReaction,
            pydantic.Tag('UpdateSentStoryReaction')        ],
        typing.Annotated[
            types.UpdateServiceNotification,
            pydantic.Tag('UpdateServiceNotification')        ],
        typing.Annotated[
            types.UpdateSmsJob,
            pydantic.Tag('UpdateSmsJob')        ],
        typing.Annotated[
            types.UpdateStarsBalance,
            pydantic.Tag('UpdateStarsBalance')        ],
        typing.Annotated[
            types.UpdateStickerSets,
            pydantic.Tag('UpdateStickerSets')        ],
        typing.Annotated[
            types.UpdateStickerSetsOrder,
            pydantic.Tag('UpdateStickerSetsOrder')        ],
        typing.Annotated[
            types.UpdateStoriesStealthMode,
            pydantic.Tag('UpdateStoriesStealthMode')        ],
        typing.Annotated[
            types.UpdateStory,
            pydantic.Tag('UpdateStory')        ],
        typing.Annotated[
            types.UpdateStoryID,
            pydantic.Tag('UpdateStoryID')        ],
        typing.Annotated[
            types.UpdateTheme,
            pydantic.Tag('UpdateTheme')        ],
        typing.Annotated[
            types.UpdateTranscribedAudio,
            pydantic.Tag('UpdateTranscribedAudio')        ],
        typing.Annotated[
            types.UpdateUser,
            pydantic.Tag('UpdateUser')        ],
        typing.Annotated[
            types.UpdateUserEmojiStatus,
            pydantic.Tag('UpdateUserEmojiStatus')        ],
        typing.Annotated[
            types.UpdateUserName,
            pydantic.Tag('UpdateUserName')        ],
        typing.Annotated[
            types.UpdateUserPhone,
            pydantic.Tag('UpdateUserPhone')        ],
        typing.Annotated[
            types.UpdateUserStatus,
            pydantic.Tag('UpdateUserStatus')        ],
        typing.Annotated[
            types.UpdateUserTyping,
            pydantic.Tag('UpdateUserTyping')        ],
        typing.Annotated[
            types.UpdateWebPage,
            pydantic.Tag('UpdateWebPage')        ],
        typing.Annotated[
            types.UpdateWebViewResultSent,
            pydantic.Tag('UpdateWebViewResultSent')        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
