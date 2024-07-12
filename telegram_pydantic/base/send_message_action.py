from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# SendMessageAction - Layer 181
SendMessageAction = typing.Annotated[
    typing.Union[
        typing.Annotated[types.SendMessageCancelAction, pydantic.Tag('SendMessageCancelAction')],
        typing.Annotated[types.SendMessageChooseContactAction, pydantic.Tag('SendMessageChooseContactAction')],
        typing.Annotated[types.SendMessageChooseStickerAction, pydantic.Tag('SendMessageChooseStickerAction')],
        typing.Annotated[types.SendMessageEmojiInteraction, pydantic.Tag('SendMessageEmojiInteraction')],
        typing.Annotated[types.SendMessageEmojiInteractionSeen, pydantic.Tag('SendMessageEmojiInteractionSeen')],
        typing.Annotated[types.SendMessageGamePlayAction, pydantic.Tag('SendMessageGamePlayAction')],
        typing.Annotated[types.SendMessageGeoLocationAction, pydantic.Tag('SendMessageGeoLocationAction')],
        typing.Annotated[types.SendMessageHistoryImportAction, pydantic.Tag('SendMessageHistoryImportAction')],
        typing.Annotated[types.SendMessageRecordAudioAction, pydantic.Tag('SendMessageRecordAudioAction')],
        typing.Annotated[types.SendMessageRecordRoundAction, pydantic.Tag('SendMessageRecordRoundAction')],
        typing.Annotated[types.SendMessageRecordVideoAction, pydantic.Tag('SendMessageRecordVideoAction')],
        typing.Annotated[types.SendMessageTypingAction, pydantic.Tag('SendMessageTypingAction')],
        typing.Annotated[types.SendMessageUploadAudioAction, pydantic.Tag('SendMessageUploadAudioAction')],
        typing.Annotated[types.SendMessageUploadDocumentAction, pydantic.Tag('SendMessageUploadDocumentAction')],
        typing.Annotated[types.SendMessageUploadPhotoAction, pydantic.Tag('SendMessageUploadPhotoAction')],
        typing.Annotated[types.SendMessageUploadRoundAction, pydantic.Tag('SendMessageUploadRoundAction')],
        typing.Annotated[types.SendMessageUploadVideoAction, pydantic.Tag('SendMessageUploadVideoAction')],
        typing.Annotated[types.SpeakingInGroupCallAction, pydantic.Tag('SpeakingInGroupCallAction')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
