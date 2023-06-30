from src import settings
from discord import Message

import traceback
import logging

from src.utils import find_class_by_path
from src.base import BaseCommand

logger = logging.getLogger("discord.py")

class BaseEvents:
    async def on_ready (self):
        logger.info("Bot inicializado.")
    
    async def on_message(self, message : Message):
        if message.author == self.user:
            return
        
        # get message content
        content = message.content
        
        # split message args and strip whitespaces
        msg_args = content.split()
        msg_args = [a.rstrip().lstrip() for a in msg_args]
        
        # if msg is empty
        if not msg_args:
            return
        
        # get first instruction
        command = msg_args[0]
        
        # seek for prefix
        if command.startswith(settings.PREFIX):
            # remove the prefix+command from message and join
            clean_content = " ".join(msg_args[1:])
            
            # clean command, removing prefix
            clean_command = command.replace(settings.PREFIX, "")
            
            # setup interaction
            await self.handle_interaction(
                message       = message,
                command       = clean_command,
                content       = message.content,
                clean_content = clean_content,
            )
    
    async def handle_interaction (self, message : Message, command, content, clean_content):
        try:
            if not command in settings.COMMANDS_MAP.keys():
                await message.channel.send(f"'{settings.PREFIX}{command}' não é um comando válido.")
                return
            
            command_path = settings.COMMANDS_MAP.get(command)
            command_class : BaseCommand = find_class_by_path(command_path)
            
            await command_class.run(
                ctx=self,
                message=message,
                channel=message.channel,
                command=command,
                content=content,
                clean_content=clean_content
            )
            
        except Exception as err:
            await message.channel.send(f"Command exited with error -> {str(err)} -> traceback:")
            await message.channel.send(traceback.format_exc())
