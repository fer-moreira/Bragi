import discord
import importlib
from src.base import BaseCommand
from src.settings import PREFIX, COMMANDS_MAP, CATEGORY_MAP
from src.utils import find_class_by_path


class HelpCommand (BaseCommand):
    def __init__(self):
        super().__init__()
        
        self.COMMAND = "help"
        self.CATEGORY = "utility"
        self.HAS_ARGUMENTS = True
        self.ARGUMENT_LABEL = "command"
        self.DESCRIPTION = f"""Provides you with the commands list.
        Do `!help <{self.ARGUMENT_LABEL}>` for extended command info."""
    
    def command_detailed_info(self, command):
        command_path = COMMANDS_MAP.get(command)
        
        if not command_path:
            return {}
        
        cmd_module = find_class_by_path(command_path)
        
        embed = discord.Embed(
            title=cmd_module.COMMAND,
            description=cmd_module.DESCRIPTION
        )
        
        if cmd_module.HAS_ARGUMENTS:
            embed.add_field(
                name="Usage",
                value=f"`{cmd_module.EXAMPLE} <{cmd_module.ARGUMENT_LABEL}>`",
                inline=True
            )
        
        embed.add_field(
            name="Example",
            value=f"`{cmd_module.EXAMPLE}`",
            inline=True
        )
        
        return embed

    def all_commands(self):
        # create empty data structure based on category
        BY_CATEGORY = {
            cat: []
            for cat in CATEGORY_MAP.keys()
        }
        
        
        # Populate categories with the commands and clear empty categories
        BY_CATEGORY = {
            category: [
                command.COMMAND
                for commands_path in COMMANDS_MAP.values()
                for command in [find_class_by_path(commands_path)]
                if command.CATEGORY == category
            ]
            for category in BY_CATEGORY.keys()
        }
        
        # Quick way to clear categories without commands
        BY_CATEGORY = {
            category: command 
            for category, command in BY_CATEGORY.items() 
            if command
        }
        
        # Build embed description
        _desc = [
            f"""{CATEGORY_MAP.get(cat)}
            {", ".join([f"`{cmd}`" for cmd in cmds])}"""
            for cat, cmds in BY_CATEGORY.items()
        ]
        
        # Build embed
        embed = discord.Embed(
            title="Todos os Comandos",
            description="\n\n".join(_desc)
        )
        
        return embed
        
    
    async def run(self, *args, **kwargs):
        channel = kwargs["channel"]
        desired_command = kwargs["clean_content"]
        
        if desired_command:
            embed = self.command_detailed_info(desired_command)
            await channel.send(embed=embed)
        else:
            embed = self.all_commands()
            await channel.send(embed=embed)

