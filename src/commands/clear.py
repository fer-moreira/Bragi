from src.base import BaseCommand

class ClearCommand (BaseCommand):
    def __init__(self):
        super().__init__()
        
        self.COMMAND       = "clear"
        self.CATEGORY      = "utility"
        self.DESCRIPTION   = "Clear the selected chat."
        self.HAS_ARGUMENTS = True
        self.ARGUMENT_LABEL = "size"

        
    async def run (self, *args, **kwargs):
        try:
            size = kwargs["clean_content"]
            if size:
                size = int(size)
                deleted = await kwargs['channel'].purge(limit=size+1)
                await kwargs['channel'].send(
                    self.LOCALE(
                        "CLEAR_CMD_DELETED_MESSAGES"
                    ).format(
                        qtd_messages=len(deleted)-1
                    ), 
                    delete_after=5
                )
            else:
                await kwargs["channel"].send(self.LOCALE("CLEAR_CMD_EMPTY"))
        except:
            await kwargs['channel'].send(self.LOCALE("CLEAR_CMD_SPECIFY_NUMBER"))
            


    