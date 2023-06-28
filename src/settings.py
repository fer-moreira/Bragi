import discord
import inspect
import importlib

PREFIX = "!"

DISCORD_TOKEN = "TOKEN CHANGED"

COMMANDS_DIR = "src.commands"


def get_fields():
    module = importlib.import_module(COMMANDS_DIR)
    async_commands = []
    
    for name, obj in inspect.getmembers(module):
        if inspect.iscoroutinefunction(obj):
            docstring = inspect.getdoc(obj)
            async_commands.append({
                "name": name, 
                "value": docstring, 
                "inline": False
            })

    return async_commands
    

GENERIC_EMBED = discord.Embed.from_dict({
    "title": "Command List",
    "fields": get_fields()
})
