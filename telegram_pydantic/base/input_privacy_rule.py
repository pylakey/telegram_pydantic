from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputPrivacyRule - Layer 181
InputPrivacyRule = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputPrivacyValueAllowAll, pydantic.Tag('InputPrivacyValueAllowAll')],
        typing.Annotated[types.InputPrivacyValueAllowChatParticipants, pydantic.Tag('InputPrivacyValueAllowChatParticipants')],
        typing.Annotated[types.InputPrivacyValueAllowCloseFriends, pydantic.Tag('InputPrivacyValueAllowCloseFriends')],
        typing.Annotated[types.InputPrivacyValueAllowContacts, pydantic.Tag('InputPrivacyValueAllowContacts')],
        typing.Annotated[types.InputPrivacyValueAllowPremium, pydantic.Tag('InputPrivacyValueAllowPremium')],
        typing.Annotated[types.InputPrivacyValueAllowUsers, pydantic.Tag('InputPrivacyValueAllowUsers')],
        typing.Annotated[types.InputPrivacyValueDisallowAll, pydantic.Tag('InputPrivacyValueDisallowAll')],
        typing.Annotated[types.InputPrivacyValueDisallowChatParticipants, pydantic.Tag('InputPrivacyValueDisallowChatParticipants')],
        typing.Annotated[types.InputPrivacyValueDisallowContacts, pydantic.Tag('InputPrivacyValueDisallowContacts')],
        typing.Annotated[types.InputPrivacyValueDisallowUsers, pydantic.Tag('InputPrivacyValueDisallowUsers')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
