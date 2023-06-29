from src.music.player import CurrentPlayer
from src.settings import PREFIX

USAGE        = "disconnect"
COMMAND      = f"{PREFIX}{USAGE}"
CATEGORY     = "music"
DESCRIPTION  = "Disconnect bot from voice channel."
ACCEPTS_ARGS = False

async def command (*args, **kwargs):
    channel = kwargs["channel"]
    channel.send("adeus")
    await CurrentPlayer.disconnect()
