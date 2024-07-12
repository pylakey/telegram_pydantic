from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# KeyboardButton - Layer 181
KeyboardButton = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputKeyboardButtonRequestPeer, pydantic.Tag('InputKeyboardButtonRequestPeer')],
        typing.Annotated[types.InputKeyboardButtonUrlAuth, pydantic.Tag('InputKeyboardButtonUrlAuth')],
        typing.Annotated[types.InputKeyboardButtonUserProfile, pydantic.Tag('InputKeyboardButtonUserProfile')],
        typing.Annotated[types.KeyboardButton, pydantic.Tag('KeyboardButton')],
        typing.Annotated[types.KeyboardButtonBuy, pydantic.Tag('KeyboardButtonBuy')],
        typing.Annotated[types.KeyboardButtonCallback, pydantic.Tag('KeyboardButtonCallback')],
        typing.Annotated[types.KeyboardButtonGame, pydantic.Tag('KeyboardButtonGame')],
        typing.Annotated[types.KeyboardButtonRequestGeoLocation, pydantic.Tag('KeyboardButtonRequestGeoLocation')],
        typing.Annotated[types.KeyboardButtonRequestPeer, pydantic.Tag('KeyboardButtonRequestPeer')],
        typing.Annotated[types.KeyboardButtonRequestPhone, pydantic.Tag('KeyboardButtonRequestPhone')],
        typing.Annotated[types.KeyboardButtonRequestPoll, pydantic.Tag('KeyboardButtonRequestPoll')],
        typing.Annotated[types.KeyboardButtonSimpleWebView, pydantic.Tag('KeyboardButtonSimpleWebView')],
        typing.Annotated[types.KeyboardButtonSwitchInline, pydantic.Tag('KeyboardButtonSwitchInline')],
        typing.Annotated[types.KeyboardButtonUrl, pydantic.Tag('KeyboardButtonUrl')],
        typing.Annotated[types.KeyboardButtonUrlAuth, pydantic.Tag('KeyboardButtonUrlAuth')],
        typing.Annotated[types.KeyboardButtonUserProfile, pydantic.Tag('KeyboardButtonUserProfile')],
        typing.Annotated[types.KeyboardButtonWebView, pydantic.Tag('KeyboardButtonWebView')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
