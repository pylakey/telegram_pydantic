from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# RichText - Layer 181
RichText = typing.Annotated[
    typing.Union[
        typing.Annotated[types.TextAnchor, pydantic.Tag('TextAnchor')],
        typing.Annotated[types.TextBold, pydantic.Tag('TextBold')],
        typing.Annotated[types.TextConcat, pydantic.Tag('TextConcat')],
        typing.Annotated[types.TextEmail, pydantic.Tag('TextEmail')],
        typing.Annotated[types.TextEmpty, pydantic.Tag('TextEmpty')],
        typing.Annotated[types.TextFixed, pydantic.Tag('TextFixed')],
        typing.Annotated[types.TextImage, pydantic.Tag('TextImage')],
        typing.Annotated[types.TextItalic, pydantic.Tag('TextItalic')],
        typing.Annotated[types.TextMarked, pydantic.Tag('TextMarked')],
        typing.Annotated[types.TextPhone, pydantic.Tag('TextPhone')],
        typing.Annotated[types.TextPlain, pydantic.Tag('TextPlain')],
        typing.Annotated[types.TextStrike, pydantic.Tag('TextStrike')],
        typing.Annotated[types.TextSubscript, pydantic.Tag('TextSubscript')],
        typing.Annotated[types.TextSuperscript, pydantic.Tag('TextSuperscript')],
        typing.Annotated[types.TextUnderline, pydantic.Tag('TextUnderline')],
        typing.Annotated[types.TextUrl, pydantic.Tag('TextUrl')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
