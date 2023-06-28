import discord
from src.radio.engine.youtube import YoutubeExtractor

voice_client = None
song_queue = []


async def play(*args, **kwargs):
    """play"""
    global voice_client
    
    ctx = kwargs["ctx"]
    message = kwargs["message"]
    clean_content = kwargs["clean_content"]
        
    if not voice_client:
        voice_channel = message.author.voice.channel
        voice_client = await voice_channel.connect()
        
    url = YoutubeExtractor().extract_bestaudio_url(clean_content)
    song_queue.append(url)
    
    if len(song_queue) == 1:
        await play_next(ctx, message)


async def play_next(ctx, message):
    """Play the next song from the queue"""
    global voice_client, song_queue

    if len(song_queue) > 0:
        url = song_queue[0]
        voice_client.play(discord.FFmpegPCMAudio(
            url), after=lambda e: ctx.loop.create_task(play_next(ctx, message)))
        await message.channel.send("Now playing: " + url)
        song_queue.pop(0)
    else:
        await voice_client.disconnect()
        voice_client = None


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



async def queue(*args, **kwargs):
    """ list queue """

    ctx = kwargs["ctx"]
    message = kwargs["message"]

    for q in song_queue:
        await message.channel.send(f"MUSICA {q}")