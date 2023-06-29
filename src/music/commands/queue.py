import discord
from src.settings import PREFIX
from src.music.player import CurrentPlayer

USAGE        = "queue"
COMMAND      = f"{PREFIX}{USAGE}"
CATEGORY     = "music"
DESCRIPTION  = "Show queued songs."
ACCEPTS_ARGS = False


async def command (*args, **kwargs):
    channel = kwargs["channel"]
    
    _description = "\n".join([
        f"{index}. {song['title']}" 
        for index, song in enumerate(CurrentPlayer.queue)
    ])
    
    _now = CurrentPlayer.now_playing
    
    embed = discord.Embed()
    embed.title = "⏭️ Fila de músicas"
    embed.description="**Tocando agora:** {_now} \n\n{_description}"
    embed.set_footer(text="Página 1/2")

    await channel.send(embed=embed)