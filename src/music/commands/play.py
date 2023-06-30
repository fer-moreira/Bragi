import json
import discord
import asyncio

from src.music.player import CurrentPlayer
from src.music.engine.youtube import YoutubeExtractor
from src.base import BaseCommand

class PlayCommand (BaseCommand):
    def __init__(self):
        self.COMMAND        = "play"
        self.CATEGORY       = "music"
        self.DESCRIPTION    = "Play music."
        self.HAS_ARGUMENTS  = True
        self.ARGUMENT_LABEL = "youtube url"

    async def run(self, *args, **kwargs):
        ctx : discord.Client = kwargs["ctx"]
        
        message     = kwargs["message"]
        channel     = kwargs["channel"]
        youtube_url = kwargs["clean_content"]
        
        
        if not CurrentPlayer.voice_client:
            voice_channel = message.author.voice.channel
            CurrentPlayer.voice_client = await voice_channel.connect()
        
        searching_message = await channel.send("<a:loading:1123724699017416945> Pesquisando...")
        
        try:
            song = YoutubeExtractor().extract_song_data(youtube_url)
            song.update({
                "author" : message.author
            })
            
            await CurrentPlayer.add_to_queue(channel, song)
            
            if not CurrentPlayer.voice_client.is_playing():
                await CurrentPlayer.play_next(ctx, channel)
                await searching_message.delete()
            else:
                await searching_message.delete()
        except:
            raise
