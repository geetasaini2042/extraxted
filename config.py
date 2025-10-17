#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 
#api_id = 24673538
#api_hash = "555639745e6ceee1ae3797866136998f"
import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8498552239:AAFQjLU6DePHb5sPvAFD7DR5sUCwsXdIFIc")
    API_ID = int(os.environ.get("API_ID", "24673538"))
    API_HASH = os.environ.get("API_HASH", "555639745e6ceee1ae3797866136998f")
    AUTH_USERS = "6150091802"



