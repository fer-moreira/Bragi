from src.settings import PREFIX

USAGE        = "disconnect"
COMMAND      = f"{PREFIX}{USAGE}"
CATEGORY     = "music"
DESCRIPTION  = "Disconnect bot from voice channel."
ACCEPTS_ARGS = False

async def command (*args, **kwargs):
    channel = kwargs["channel"]
    await channel.send("xereca")
