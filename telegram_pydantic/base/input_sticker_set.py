from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputStickerSet - Layer 181
InputStickerSet = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputStickerSetAnimatedEmoji, pydantic.Tag('InputStickerSetAnimatedEmoji')],
        typing.Annotated[types.InputStickerSetAnimatedEmojiAnimations, pydantic.Tag('InputStickerSetAnimatedEmojiAnimations')],
        typing.Annotated[types.InputStickerSetDice, pydantic.Tag('InputStickerSetDice')],
        typing.Annotated[types.InputStickerSetEmojiChannelDefaultStatuses, pydantic.Tag('InputStickerSetEmojiChannelDefaultStatuses')],
        typing.Annotated[types.InputStickerSetEmojiDefaultStatuses, pydantic.Tag('InputStickerSetEmojiDefaultStatuses')],
        typing.Annotated[types.InputStickerSetEmojiDefaultTopicIcons, pydantic.Tag('InputStickerSetEmojiDefaultTopicIcons')],
        typing.Annotated[types.InputStickerSetEmojiGenericAnimations, pydantic.Tag('InputStickerSetEmojiGenericAnimations')],
        typing.Annotated[types.InputStickerSetEmpty, pydantic.Tag('InputStickerSetEmpty')],
        typing.Annotated[types.InputStickerSetID, pydantic.Tag('InputStickerSetID')],
        typing.Annotated[types.InputStickerSetPremiumGifts, pydantic.Tag('InputStickerSetPremiumGifts')],
        typing.Annotated[types.InputStickerSetShortName, pydantic.Tag('InputStickerSetShortName')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
