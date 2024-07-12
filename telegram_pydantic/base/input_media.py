from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputMedia - Layer 181
InputMedia = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputMediaContact, pydantic.Tag('InputMediaContact')],
        typing.Annotated[types.InputMediaDice, pydantic.Tag('InputMediaDice')],
        typing.Annotated[types.InputMediaDocument, pydantic.Tag('InputMediaDocument')],
        typing.Annotated[types.InputMediaDocumentExternal, pydantic.Tag('InputMediaDocumentExternal')],
        typing.Annotated[types.InputMediaEmpty, pydantic.Tag('InputMediaEmpty')],
        typing.Annotated[types.InputMediaGame, pydantic.Tag('InputMediaGame')],
        typing.Annotated[types.InputMediaGeoLive, pydantic.Tag('InputMediaGeoLive')],
        typing.Annotated[types.InputMediaGeoPoint, pydantic.Tag('InputMediaGeoPoint')],
        typing.Annotated[types.InputMediaInvoice, pydantic.Tag('InputMediaInvoice')],
        typing.Annotated[types.InputMediaPhoto, pydantic.Tag('InputMediaPhoto')],
        typing.Annotated[types.InputMediaPhotoExternal, pydantic.Tag('InputMediaPhotoExternal')],
        typing.Annotated[types.InputMediaPoll, pydantic.Tag('InputMediaPoll')],
        typing.Annotated[types.InputMediaStory, pydantic.Tag('InputMediaStory')],
        typing.Annotated[types.InputMediaUploadedDocument, pydantic.Tag('InputMediaUploadedDocument')],
        typing.Annotated[types.InputMediaUploadedPhoto, pydantic.Tag('InputMediaUploadedPhoto')],
        typing.Annotated[types.InputMediaVenue, pydantic.Tag('InputMediaVenue')],
        typing.Annotated[types.InputMediaWebPage, pydantic.Tag('InputMediaWebPage')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
