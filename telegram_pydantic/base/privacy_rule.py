from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PrivacyRule - Layer 181
PrivacyRule = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PrivacyValueAllowAll, pydantic.Tag('PrivacyValueAllowAll')],
        typing.Annotated[types.PrivacyValueAllowChatParticipants, pydantic.Tag('PrivacyValueAllowChatParticipants')],
        typing.Annotated[types.PrivacyValueAllowCloseFriends, pydantic.Tag('PrivacyValueAllowCloseFriends')],
        typing.Annotated[types.PrivacyValueAllowContacts, pydantic.Tag('PrivacyValueAllowContacts')],
        typing.Annotated[types.PrivacyValueAllowPremium, pydantic.Tag('PrivacyValueAllowPremium')],
        typing.Annotated[types.PrivacyValueAllowUsers, pydantic.Tag('PrivacyValueAllowUsers')],
        typing.Annotated[types.PrivacyValueDisallowAll, pydantic.Tag('PrivacyValueDisallowAll')],
        typing.Annotated[types.PrivacyValueDisallowChatParticipants, pydantic.Tag('PrivacyValueDisallowChatParticipants')],
        typing.Annotated[types.PrivacyValueDisallowContacts, pydantic.Tag('PrivacyValueDisallowContacts')],
        typing.Annotated[types.PrivacyValueDisallowUsers, pydantic.Tag('PrivacyValueDisallowUsers')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
