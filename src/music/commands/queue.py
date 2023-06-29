import discord
import math
from src.settings import PREFIX
from src.music.player import CurrentPlayer

USAGE        = "queue"
COMMAND      = f"{PREFIX}{USAGE}"
CATEGORY     = "music"
DESCRIPTION  = "Show queued songs."
ACCEPTS_ARGS = False


async def command (*args, **kwargs):
    channel = kwargs["channel"]
    
    if not CurrentPlayer.queue:
        await channel.send("empty queue")
        return
    
    _now = CurrentPlayer.now_playing["title"]
    
    _description = "\n".join([
        f"{index}. {song['title']}" 
        for index, song in enumerate(CurrentPlayer.queue[:10])
    ])
    
    
    embed = discord.Embed()
    embed.title = "⏭️ Fila de músicas"
    embed.description=f"**Tocando agora:** {_now} \n\n{_description}"
    
    try:
        page_count = math.ceil(len(CurrentPlayer.queue) / 10)
    except:
        page_count = "+8000"
    
    embed.set_footer(text=f"Página 1/{page_count}")

    await channel.send(embed=embed)