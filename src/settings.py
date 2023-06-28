import os

PREFIX = "!"

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

COMMANDS_MAP = {
    "help" : "src.commands.help",
    "ping" : "src.commands.ping"
}

CATEGORY_MAP = {
    "utility" : "🔧 Utility",
    "music"   : "🎵 Music"
}