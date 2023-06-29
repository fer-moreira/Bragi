import json
import discord
import asyncio

from src.settings import PREFIX
from src.music.player import CurrentPlayer
from src.music.engine.youtube import YoutubeExtractor

USAGE        = "play"
COMMAND      = f"{PREFIX}{USAGE}"
CATEGORY     = "music"
DESCRIPTION  = "Play music."
ACCEPTS_ARGS = True


async def command(*args, **kwargs):
    ctx : discord.Client = kwargs["ctx"]
    message     = kwargs["message"]
    channel     = kwargs["channel"]
    youtube_url = kwargs["clean_content"]
    
    
    if not CurrentPlayer.voice_client:
        voice_channel = message.author.voice.channel
        CurrentPlayer.voice_client = await voice_channel.connect()
    
    
    comunication_msg = await channel.send("<a:loading:1123724699017416945> Pesquisando...")
    
    try:
        song = YoutubeExtractor().extract_song_data(youtube_url)
        
        CurrentPlayer.add_to_queue(song)
        
        if not CurrentPlayer.voice_client.is_playing():
            await CurrentPlayer.play_next(ctx)
            await comunication_msg.edit(content=f"Now Playing -> {song['title']}")
        else:
            await comunication_msg.edit(content=f"Added to queue -> {song['title']}")
    except:
        raise
