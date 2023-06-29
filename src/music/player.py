
import asyncio
import discord

class MusicPlayer:
    def __init__(self):
        self.queue = []
        self.voice_client = None
        self.now_playing = None
    
    def add_to_queue(self, song):
        self.queue.append(song)
    
    def get_next (self):
        try:
            self.now_playing = self.queue.pop(0)
            return self.now_playing
        except IndexError as r:
            return None
        
    async def play_next(self, ctx : discord.Client):
        if self.queue:
            next_song = self.get_next()
            
            self.voice_client.play(
                discord.FFmpegPCMAudio(next_song["url"]),
                after=lambda e: ctx.loop.create_task(self.play_next(ctx))
            )
        else:
            asyncio.sleep(10)
            await self.disconnect()

    async def disconnect(self):
        await self.voice_client.disconnect()
        self.queue = []
        self.voice_client = None
        self.now_playing = None
        
    async def skip(self):
        if self.voice_client and self.voice_client.is_playing():
            self.voice_client.stop()
        else:
            raise ValueError("No song is currently playing.")


CurrentPlayer = MusicPlayer()