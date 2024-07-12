from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# ForumTopic - Layer 181
ForumTopic = typing.Annotated[
    typing.Union[
        typing.Annotated[types.ForumTopic, pydantic.Tag('ForumTopic')],
        typing.Annotated[types.ForumTopicDeleted, pydantic.Tag('ForumTopicDeleted')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
