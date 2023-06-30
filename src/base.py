from src.settings import PREFIX

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
    
    async def run (self, *args, **kwargs):
        await kwargs["channel"].send("Example Command")
        