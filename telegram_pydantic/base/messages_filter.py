from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# MessagesFilter - Layer 181
MessagesFilter = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputMessagesFilterChatPhotos, pydantic.Tag('InputMessagesFilterChatPhotos')],
        typing.Annotated[types.InputMessagesFilterContacts, pydantic.Tag('InputMessagesFilterContacts')],
        typing.Annotated[types.InputMessagesFilterDocument, pydantic.Tag('InputMessagesFilterDocument')],
        typing.Annotated[types.InputMessagesFilterEmpty, pydantic.Tag('InputMessagesFilterEmpty')],
        typing.Annotated[types.InputMessagesFilterGeo, pydantic.Tag('InputMessagesFilterGeo')],
        typing.Annotated[types.InputMessagesFilterGif, pydantic.Tag('InputMessagesFilterGif')],
        typing.Annotated[types.InputMessagesFilterMusic, pydantic.Tag('InputMessagesFilterMusic')],
        typing.Annotated[types.InputMessagesFilterMyMentions, pydantic.Tag('InputMessagesFilterMyMentions')],
        typing.Annotated[types.InputMessagesFilterPhoneCalls, pydantic.Tag('InputMessagesFilterPhoneCalls')],
        typing.Annotated[types.InputMessagesFilterPhotoVideo, pydantic.Tag('InputMessagesFilterPhotoVideo')],
        typing.Annotated[types.InputMessagesFilterPhotos, pydantic.Tag('InputMessagesFilterPhotos')],
        typing.Annotated[types.InputMessagesFilterPinned, pydantic.Tag('InputMessagesFilterPinned')],
        typing.Annotated[types.InputMessagesFilterRoundVideo, pydantic.Tag('InputMessagesFilterRoundVideo')],
        typing.Annotated[types.InputMessagesFilterRoundVoice, pydantic.Tag('InputMessagesFilterRoundVoice')],
        typing.Annotated[types.InputMessagesFilterUrl, pydantic.Tag('InputMessagesFilterUrl')],
        typing.Annotated[types.InputMessagesFilterVideo, pydantic.Tag('InputMessagesFilterVideo')],
        typing.Annotated[types.InputMessagesFilterVoice, pydantic.Tag('InputMessagesFilterVoice')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
