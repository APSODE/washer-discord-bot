from typing import Dict, List, Optional
from discord.ext import commands

import discord


class WasherDiscordBot(commands.Bot):
    def __init__(self):
        self._token = "MTA3NzI3MjMzMDYyMDg5NTI5Mg.GYAqie.JKvD818TqiHAJA2rWKiThuQ58dxsgjprO9rMyI"
        self._intent = discord.Intents.default()

        super(WasherDiscordBot, self).__init__(
            command_prefix = "!",
            intents = self._intent,
            
        )


    def _CreateInstanse(self):
        pass