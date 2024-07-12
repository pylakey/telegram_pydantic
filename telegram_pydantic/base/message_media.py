from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# MessageMedia - Layer 181
MessageMedia = typing.Annotated[
    typing.Union[
        typing.Annotated[types.MessageMediaContact, pydantic.Tag('MessageMediaContact')],
        typing.Annotated[types.MessageMediaDice, pydantic.Tag('MessageMediaDice')],
        typing.Annotated[types.MessageMediaDocument, pydantic.Tag('MessageMediaDocument')],
        typing.Annotated[types.MessageMediaEmpty, pydantic.Tag('MessageMediaEmpty')],
        typing.Annotated[types.MessageMediaGame, pydantic.Tag('MessageMediaGame')],
        typing.Annotated[types.MessageMediaGeo, pydantic.Tag('MessageMediaGeo')],
        typing.Annotated[types.MessageMediaGeoLive, pydantic.Tag('MessageMediaGeoLive')],
        typing.Annotated[types.MessageMediaGiveaway, pydantic.Tag('MessageMediaGiveaway')],
        typing.Annotated[types.MessageMediaGiveawayResults, pydantic.Tag('MessageMediaGiveawayResults')],
        typing.Annotated[types.MessageMediaInvoice, pydantic.Tag('MessageMediaInvoice')],
        typing.Annotated[types.MessageMediaPhoto, pydantic.Tag('MessageMediaPhoto')],
        typing.Annotated[types.MessageMediaPoll, pydantic.Tag('MessageMediaPoll')],
        typing.Annotated[types.MessageMediaStory, pydantic.Tag('MessageMediaStory')],
        typing.Annotated[types.MessageMediaUnsupported, pydantic.Tag('MessageMediaUnsupported')],
        typing.Annotated[types.MessageMediaVenue, pydantic.Tag('MessageMediaVenue')],
        typing.Annotated[types.MessageMediaWebPage, pydantic.Tag('MessageMediaWebPage')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
