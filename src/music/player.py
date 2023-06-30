
import asyncio
import discord
from src.locale import LOCALE

class MusicPlayer:
    def __init__(self):
        self.queue = []
        self.voice_client = None
        self.now_playing = None
        
    def playing_embed (self, song):
        embed = discord.Embed(
            title=LOCALE.get(
                "PLAYER_NOWPLAYING_EMBED_TITLE"
            )
        )
        embed.add_field(
            name=song['title'],
            value=f"`[0:00 / {song['duration']}]`"
        )
        embed.set_thumbnail(url=song['thumbnail'])
        embed.set_footer(
            text=LOCALE.get(
                "PLAYER_NOWPLAYING_EMBEB_REQUESTED"
            ).format(
                author=song['author']
            )
        )
        
        return embed
    
    def queue_embed (self, song):
        embed = discord.Embed(
            title=LOCALE.get("PLAYER_QUEUE_EMBED_TITLE")
        )

        embed.add_field(
            name=song['title'],
            value=LOCALE.get(
                "PLAYER_QUEUE_EMBED_POSITION"
            ).format(
                position=song.get('position', 0)
            )
        )

        embed.set_thumbnail(url=song["thumbnail"])
        return embed
    
    def get_next (self):
        try:
            self.now_playing = self.queue.pop(0)
            return self.now_playing
        except IndexError as r:
            return None
        
    async def add_to_queue(self, channel, song):
        song.update({"position" : (len(self.queue) + 1)})
        self.queue.append(song)
        
        if self.now_playing:
            await channel.send(embed=self.queue_embed(song))
            
    async def remove_from_queue(self, channel, to_remove):
        try:
            index = int(int(to_remove) - 1)
            
            await channel.send(LOCALE.get(
                "PLAYER_QUEUE_REMOVED_LABEL"
            ).format(
                title=self.queue[index]['title']
            ))
            del self.queue[index]
        except:
            await channel.send(LOCALE.get("PLAYER_QUEUE_REMOVED_ERROR"))
        
    async def play_next(self, ctx : discord.Client, channel):
        if self.queue:
            next_song = self.get_next()
            
            await channel.send(embed=self.playing_embed(next_song))
            
            self.voice_client.play(
                discord.FFmpegPCMAudio(next_song["url"]),
                after=lambda e: ctx.loop.create_task(self.play_next(ctx, channel))
            )
        else:
            await asyncio.sleep(30)
            await self.disconnect()
            await channel.send(LOCALE.get("GENERIC_ERROR_DISCONNECTED"))

    async def disconnect(self):
        await self.voice_client.disconnect()
        self.queue = []
        self.voice_client = None
        self.now_playing = None
        
    async def skip(self):
        if self.voice_client and self.voice_client.is_playing():
            self.voice_client.stop()
        else:
            raise ValueError("I'm not playing anything.")


Jukebox = MusicPlayer()