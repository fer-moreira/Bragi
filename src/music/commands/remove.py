from src.music.player import Jukebox
from src.base import BaseCommand


class RemoveCommand (BaseCommand):
    def __init__(self):
        self.COMMAND = "remove"
        self.CATEGORY = "music"
        self.DESCRIPTION = "Remove selected index from queue."
        self.HAS_ARGUMENTS = True
        self.ARGUMENT_LABEL = "music index from queue"
    
    async def run (self, *args, **kwargs):
        await Jukebox.remove_from_queue(
            kwargs['channel'], 
            kwargs['clean_content']
        )