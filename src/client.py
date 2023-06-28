import logging
from typing import Any, Optional
from discord import Client, Intents
from discord.flags import Intents
from discord.utils import MISSING

from src import settings
from src.events import BaseEvents

class DiscordClient(Client, BaseEvents):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        
        super().__init__(intents=intents)
        
        self.token = settings.DISCORD_TOKEN
        self.reconnect = True
    
    def run(self):
        return super().run(self.token, reconnect=self.reconnect)