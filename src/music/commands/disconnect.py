from src.music.player import Jukebox
from src.base import BaseCommand


class DisconnectCommand (BaseCommand):
    def __init__(self):
        self.COMMAND = "disconnect"
        self.CATEGORY = "music"
        self.DESCRIPTION = "Disconnect bot from voice channel."
        self.HAS_ARGUMENTS = False
    
    async def run (self, *args, **kwargs):
        await kwargs["channel"].send(self.LOCALE("GENERIC_ERROR_DISCONNECTED"))
        await Jukebox.disconnect()