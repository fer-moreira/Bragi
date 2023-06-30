import discord
import math
from src.music.player import Jukebox
from src.base import BaseCommand

class QueueCommand (BaseCommand):
    def __init__(self):
        self.COMMAND        = "queue"
        self.CATEGORY       = "music"
        self.DESCRIPTION    = "Show queued songs."
        self.HAS_ARGUMENTS  = False
    
    async def run (self, *args, **kwargs):
        channel = kwargs["channel"]
        
        if not Jukebox.voice_client:
            await channel.send(self.LOCALE("GENERIC_ERROR_IDLE"))
            return
        
        _now = Jukebox.now_playing["title"]
        
        _description = "\n".join([
            f"{index}. {song['title']}" 
            for index, song in enumerate(Jukebox.queue[:10])
        ])
        
        
        embed = discord.Embed()
        embed.title = self.LOCALE("QUEUE_CMD_EMBED_TITLE")
        embed.description=self.LOCALE(
            "QUEUE_CMD_EMBED_DESC"
        ).format(
            now=_now,
            description=_description
        )
        
        try:
            page_count = math.ceil(len(Jukebox.queue) / 10)
            if page_count == 0:
                page_count = 1
        except:
            page_count = "+8000"
        
        embed.set_footer(text=
            self.LOCALE(
                "QUEUE_CMD_EMBED_PAGECOUNT"
            ).format(
                count=page_count
            )
        )

        await channel.send(embed=embed)