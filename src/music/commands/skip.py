from src.music.player import CurrentPlayer
from src.base import BaseCommand

class SkipCommand (BaseCommand):
    def __init__(self):
        self.COMMAND        = "skip"
        self.CATEGORY       = "music"
        self.DESCRIPTION    = "Skip current music"
        self.HAS_ARGUMENTS  = False
        
    async def run (self, *args, **kwargs):
        try:
            await CurrentPlayer.skip()
        except ValueError as r:
            await kwargs["channel"].send("No song playing")