from src.music.player import CurrentPlayer
from src.base import BaseCommand


class RemoveCommand (BaseCommand):
    def __init__(self):
        self.COMMAND = "remove"
        self.CATEGORY = "music"
        self.DESCRIPTION = "Remove selected index from queue."
        self.HAS_ARGUMENTS = True
        self.ARGUMENT_LABEL = "music index from queue"
    
    async def run (*args, **kwargs):
        try:
            await CurrentPlayer.remove_from_queue(
                kwargs['channel'], 
                int(kwargs['clean_content'])
            )
        except:
            await kwargs['channel'].send("⛔ Could not find that song in the queue.")