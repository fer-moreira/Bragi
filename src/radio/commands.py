import discord
from src.radio.engine.youtube import YoutubeExtractor

voice_client = None
song_queue = [
    {
        "url" : "",
        "title" : "",
        "thumbnail" : ""
    }
]


async def play(*args, **kwargs):
    """play"""
    global voice_client
    global song_queue
    
    ctx = kwargs["ctx"]
    message = kwargs["message"]
    clean_content = kwargs["clean_content"]
        
    if not voice_client:
        voice_channel = message.author.voice.channel
        voice_client = await voice_channel.connect()
        
    url = YoutubeExtractor().get_best_audios(clean_content)


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
