from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Config(BaseModel):
    """
    types.Config
    ID: 0xcc1a241e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.Config', 'Config'] = pydantic.Field(
        'types.Config',
        alias='_'
    )

    date: Datetime
    expires: Datetime
    test_mode: bool
    this_dc: int
    dc_options: list["base.DcOption"]
    dc_txt_domain_name: str
    chat_size_max: int
    megagroup_size_max: int
    forwarded_count_max: int
    online_update_period_ms: int
    offline_blur_timeout_ms: int
    offline_idle_timeout_ms: int
    online_cloud_timeout_ms: int
    notify_cloud_delay_ms: int
    notify_default_delay_ms: int
    push_chat_period_ms: int
    push_chat_limit: int
    edit_time_limit: int
    revoke_time_limit: int
    revoke_pm_time_limit: int
    rating_e_decay: int
    stickers_recent_limit: int
    channels_read_media_period: int
    call_receive_timeout_ms: int
    call_ring_timeout_ms: int
    call_connect_timeout_ms: int
    call_packet_timeout_ms: int
    me_url_prefix: str
    caption_length_max: int
    message_length_max: int
    webfile_dc_id: int
    default_p2p_contacts: typing.Optional[bool] = None
    preload_featured_stickers: typing.Optional[bool] = None
    revoke_pm_inbox: typing.Optional[bool] = None
    blocked_mode: typing.Optional[bool] = None
    force_try_ipv6: typing.Optional[bool] = None
    tmp_sessions: typing.Optional[int] = None
    autoupdate_url_prefix: typing.Optional[str] = None
    gif_search_username: typing.Optional[str] = None
    venue_search_username: typing.Optional[str] = None
    img_search_username: typing.Optional[str] = None
    static_maps_provider: typing.Optional[str] = None
    suggested_lang_code: typing.Optional[str] = None
    lang_pack_version: typing.Optional[int] = None
    base_lang_pack_version: typing.Optional[int] = None
    reactions_default: typing.Optional["base.Reaction"] = None
    autologin_token: typing.Optional[str] = None
