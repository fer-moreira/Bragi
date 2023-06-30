import discord
import math
from src.music.player import CurrentPlayer
from src.base import BaseCommand

class QueueCommand (BaseCommand):
    def __init__(self):
        self.COMMAND        = "queue"
        self.CATEGORY       = "music"
        self.DESCRIPTION    = "Show queued songs."
        self.HAS_ARGUMENTS  = False
    
    async def run (self, *args, **kwargs):
        channel = kwargs["channel"]
        
        if not CurrentPlayer.voice_client or not CurrentPlayer.queue:
            await channel.send("I'm not playing anything.")
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