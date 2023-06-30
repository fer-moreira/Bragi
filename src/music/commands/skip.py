from src.music.player import Jukebox
from src.base import BaseCommand

class SkipCommand (BaseCommand):
    def __init__(self):
        self.COMMAND        = "skip"
        self.CATEGORY       = "music"
        self.DESCRIPTION    = "Skip current music"
        self.HAS_ARGUMENTS  = False
        
    async def run (self, *args, **kwargs):
        try:
            await Jukebox.skip()
        except ValueError as r:
            await kwargs["channel"].send(self.LOCALE("GENERIC_ERROR_IDLE"))