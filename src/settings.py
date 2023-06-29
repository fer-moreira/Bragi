import os

PREFIX = "!"

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

COMMANDS_MAP = {
    # utility
    "help" : "src.commands.help",
    "ping" : "src.commands.ping",
    
    # music
    "play"       : "src.music.commands.play",
    "queue"      : "src.music.commands.queue",
    "skip"       : "src.music.commands.skip",
    "disconnect" : "src.music.commands.disconnect"
}

CATEGORY_MAP = {
    "utility" : "🔧 Utility",
    "music"   : "🎵 Music"
}