from src.settings import PREFIX
from src.locale import LOCALE as LOC

class BaseCommand:
    def __init__ (self):
        self.COMMAND        = "command"
        self.CATEGORY       = "generic"
        self.DESCRIPTION    = "Command detailed description"
        self.HAS_ARGUMENTS  = True
        self.ARGUMENT_LABEL = "command"
    
    @property
    def EXAMPLE (self):
        return f"{PREFIX}{self.COMMAND}"
    
    def LOCALE (self, id) -> str:
        return LOC.get(id)
    
    async def run (self, *args, **kwargs):
        await kwargs["channel"].send("Example Command")
