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
        
    def playing_embed (self):
        embed = discord.Embed(title="💿 Tocando agora")
        embed.add_field(
            name="TÁ FALANDO QUE ME AMA - MC RB [ PL TORVIC ]",
            value="`[0:00 / 02:17]`"
        )
        embed.set_thumbnail(url="https://i.ytimg.com/vi/CEzKEoFozwE/hqdefault.jpg")
        embed.set_footer(text="Solicitado por: @Carvalho")
        
        return embed
    
    def queue_embed (self):
        embed = discord.Embed(title="🔢 Adicionado a fila")

        embed.add_field(
            name="DE 4 EU JOGO RABO, SEQUENCIA DE TOMA TOMA, SEQUENCIA DE VAPO VAPO ♪ ♫ MC INGRYD 2020",
            value="`Posição: #1`"
        )

        embed.set_thumbnail(url="https://i.ytimg.com/vi/CEzKEoFozwE/hqdefault.jpg")
        return embed

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
            
            CurrentPlayer.add_to_queue(song)
            
            if not CurrentPlayer.voice_client.is_playing():
                await CurrentPlayer.play_next(ctx)
                await searching_message.delete()
                await channel.send(embed=self.playing_embed())
            else:
                await searching_message.delete()
                await channel.send(embed=self.queue_embed())
        except:
            raise
