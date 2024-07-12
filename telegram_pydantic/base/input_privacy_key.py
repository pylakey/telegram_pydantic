from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputPrivacyKey - Layer 181
InputPrivacyKey = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputPrivacyKeyAbout, pydantic.Tag('InputPrivacyKeyAbout')],
        typing.Annotated[types.InputPrivacyKeyAddedByPhone, pydantic.Tag('InputPrivacyKeyAddedByPhone')],
        typing.Annotated[types.InputPrivacyKeyBirthday, pydantic.Tag('InputPrivacyKeyBirthday')],
        typing.Annotated[types.InputPrivacyKeyChatInvite, pydantic.Tag('InputPrivacyKeyChatInvite')],
        typing.Annotated[types.InputPrivacyKeyForwards, pydantic.Tag('InputPrivacyKeyForwards')],
        typing.Annotated[types.InputPrivacyKeyPhoneCall, pydantic.Tag('InputPrivacyKeyPhoneCall')],
        typing.Annotated[types.InputPrivacyKeyPhoneNumber, pydantic.Tag('InputPrivacyKeyPhoneNumber')],
        typing.Annotated[types.InputPrivacyKeyPhoneP2P, pydantic.Tag('InputPrivacyKeyPhoneP2P')],
        typing.Annotated[types.InputPrivacyKeyProfilePhoto, pydantic.Tag('InputPrivacyKeyProfilePhoto')],
        typing.Annotated[types.InputPrivacyKeyStatusTimestamp, pydantic.Tag('InputPrivacyKeyStatusTimestamp')],
        typing.Annotated[types.InputPrivacyKeyVoiceMessages, pydantic.Tag('InputPrivacyKeyVoiceMessages')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
