from src.music.player import CurrentPlayer
from src.settings import PREFIX

USAGE        = "skip"
COMMAND      = f"{PREFIX}{USAGE}"
CATEGORY     = "music"
DESCRIPTION  = "Skip current music"
ACCEPTS_ARGS = False

async def command (*args, **kwargs):
    channel = kwargs["channel"]
    
    try:
        await CurrentPlayer.skip()
    except ValueError as r:
        await channel.send("No song playing")
