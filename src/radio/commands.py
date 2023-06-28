import json
import discord
import asyncio
from src.radio.engine.youtube import YoutubeExtractor


voice_client = None
song_queue = []


async def play(*args, **kwargs):
    """play"""
    global voice_client
    global song_queue
    
    ctx = kwargs["ctx"]
    message = kwargs["message"]
    channel = kwargs["channel"]
    clean_content = kwargs["clean_content"]

    async def play_next_song(ctx, channel, searching_message):
        global voice_client
        
        if song_queue:
            next_song = song_queue.pop(0)
            
            await searching_message.edit(content=f"Tocando agora: {next_song['title']}")
            
            voice_client.play(
                discord.FFmpegPCMAudio(next_song["url"]),
                after=lambda e: ctx.loop.create_task(
                    play_next_song(ctx, channel, searching_message)
                )
            )
            
            # piece of code to fix faster voice on start
            voice_client.pause()
            await asyncio.sleep(1)
            voice_client.resume()
        else:
            await voice_client.disconnect()
            voice_client = None

    if not voice_client:
        voice_channel = message.author.voice.channel
        voice_client = await voice_channel.connect()

    searching_message = await channel.send("<a:loading:1123724699017416945> Pesquisando...")

    song = YoutubeExtractor().extract_song_data(clean_content)
    song_queue.append(song)

    if not voice_client.is_playing():
        await play_next_song(ctx, channel, searching_message)
    else:
        await searching_message.edit(content=f"Added to queue -> {song['title']}")
    

async def disconnect(*args, **kwargs):
    """ disconnect """
    global voice_client

    ctx = kwargs["ctx"]
    message = kwargs["message"]

    if voice_client:
        if voice_client.is_connected():
            await voice_client.disconnect()
            voice_client = None
    else:
        await message.channel.send("Já estou fora do canal de voz")

async def skip(*args, **kwargs):
    """Skip the current song."""
    global voice_client
    
    if voice_client and voice_client.is_playing():
        voice_client.stop()
