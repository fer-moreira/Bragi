import discord
import importlib
from src.settings import PREFIX, COMMANDS_MAP

USAGE = "help"

COMMAND = f"{PREFIX}{USAGE}"

CATEGORY = "utility"

DESCRIPTION = "Provides you with the commands list.\nDo `!help <command>` for extended command info."

ACCEPTS_ARGS = True


def get_command_embed (command):
    command_path = COMMANDS_MAP.get(command, None)
    
    if not command_path: return {}
    
    cmd_module = importlib.import_module(command_path)
    
    embed = discord.Embed()
    embed.title = cmd_module.USAGE
    embed.description = cmd_module.DESCRIPTION
    
    if cmd_module.ACCEPTS_ARGS:
        embed.add_field(name="Usage", value=f"`{cmd_module.COMMAND} <argument>`", inline=True)
    
    embed.add_field(name="Example", value=f"`{cmd_module.COMMAND}`", inline=True)
    
    return embed


async def command (*args, **kwargs):
    channel = kwargs["channel"]
    clean_content = kwargs["clean_content"]
    
    if clean_content:
        embed = get_command_embed(clean_content)
        await channel.send(embed=embed)
    else:
        await channel.send("xereca")
