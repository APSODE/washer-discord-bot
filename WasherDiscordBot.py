from typing import Dict, List, Optional
from src.token.Token import Token
from discord.ext import commands

import discord


class WasherDiscordBot(commands.Bot):
    def __init__(self):
        self._token = Token.GetToken()
        self._intent = discord.Intents.default()

        super(WasherDiscordBot, self).__init__(
            command_prefix = "!",
            intents = self._intent,

        )


    def _CreateInstanse(self):
        pass