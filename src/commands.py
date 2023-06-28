import discord
from src import settings

from src.radio.commands import play
from src.radio.commands import disconnect

async def help (*args, **kwargs):
    """ doctstring help """
    
    channel = kwargs["channel"]
    await channel.send(embed=settings.GENERIC_EMBED)

async def ping (*args, **kwargs):
    """ doctstring ping """
    
    channel = kwargs["channel"]
    ctx : discord.Client = kwargs["ctx"]
    
    latency = round(ctx.latency * 1000)
    
    await channel.send(f"Pong! {latency}ms")
