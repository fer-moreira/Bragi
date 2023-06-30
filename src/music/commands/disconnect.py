from src.music.player import CurrentPlayer
from src.base import BaseCommand


class DisconnectCommand (BaseCommand):
    def __init__(self):
        self.COMMAND = "disconnect"
        self.CATEGORY = "music"
        self.DESCRIPTION = "Disconnect bot from voice channel."
        self.HAS_ARGUMENTS = False
    
    async def run (*args, **kwargs):
        kwargs["channel"].send("fodase entao")
        await CurrentPlayer.disconnect()