from src.base import BaseCommand

class PingCommand (BaseCommand):
    def __init__(self):
        super().__init__()
        
        self.COMMAND       = "ping"
        self.CATEGORY      = "utility"
        self.DESCRIPTION   = "Shows Enigma's latency to Discord's API."
        self.HAS_ARGUMENTS = False
        
    async def run (self, *args, **kwargs):
        await kwargs['channel'].send(f"Pong! { round(kwargs['ctx'].latency * 1000) }ms")