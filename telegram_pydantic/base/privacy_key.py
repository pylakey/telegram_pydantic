from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PrivacyKey - Layer 181
PrivacyKey = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PrivacyKeyAbout, pydantic.Tag('PrivacyKeyAbout')],
        typing.Annotated[types.PrivacyKeyAddedByPhone, pydantic.Tag('PrivacyKeyAddedByPhone')],
        typing.Annotated[types.PrivacyKeyBirthday, pydantic.Tag('PrivacyKeyBirthday')],
        typing.Annotated[types.PrivacyKeyChatInvite, pydantic.Tag('PrivacyKeyChatInvite')],
        typing.Annotated[types.PrivacyKeyForwards, pydantic.Tag('PrivacyKeyForwards')],
        typing.Annotated[types.PrivacyKeyPhoneCall, pydantic.Tag('PrivacyKeyPhoneCall')],
        typing.Annotated[types.PrivacyKeyPhoneNumber, pydantic.Tag('PrivacyKeyPhoneNumber')],
        typing.Annotated[types.PrivacyKeyPhoneP2P, pydantic.Tag('PrivacyKeyPhoneP2P')],
        typing.Annotated[types.PrivacyKeyProfilePhoto, pydantic.Tag('PrivacyKeyProfilePhoto')],
        typing.Annotated[types.PrivacyKeyStatusTimestamp, pydantic.Tag('PrivacyKeyStatusTimestamp')],
        typing.Annotated[types.PrivacyKeyVoiceMessages, pydantic.Tag('PrivacyKeyVoiceMessages')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
