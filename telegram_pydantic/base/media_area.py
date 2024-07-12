from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# MediaArea - Layer 181
MediaArea = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputMediaAreaChannelPost, pydantic.Tag('InputMediaAreaChannelPost')],
        typing.Annotated[types.InputMediaAreaVenue, pydantic.Tag('InputMediaAreaVenue')],
        typing.Annotated[types.MediaAreaChannelPost, pydantic.Tag('MediaAreaChannelPost')],
        typing.Annotated[types.MediaAreaGeoPoint, pydantic.Tag('MediaAreaGeoPoint')],
        typing.Annotated[types.MediaAreaSuggestedReaction, pydantic.Tag('MediaAreaSuggestedReaction')],
        typing.Annotated[types.MediaAreaVenue, pydantic.Tag('MediaAreaVenue')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
