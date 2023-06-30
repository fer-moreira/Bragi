import os

PREFIX = "!"

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

COMMANDS_MAP = {
    # utility
    "help"      : "src.commands.help.HelpCommand",
    "ping"      : "src.commands.ping.PingCommand",
    
    # music
    "play"       : "src.music.commands.play.PlayCommand",
    "skip"       : "src.music.commands.skip.SkipCommand",
    "queue"      : "src.music.commands.queue.QueueCommand",
    "disconnect" : "src.music.commands.disconnect.DisconnectCommand",
}

CATEGORY_MAP = {
    "utility"  : "🔧 Utility",
    "music  "  : "🎵 Music  ",
    "fallback" : "🗿 Generic"
}
