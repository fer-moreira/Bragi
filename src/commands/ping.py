from src.settings import PREFIX

USAGE = "ping"

COMMAND = f"{PREFIX}{USAGE}"

CATEGORY = "utility"

DESCRIPTION = "Shows Enigma's latency to Discord's API."

ACCEPTS_ARGS = False

async def command (*args, **kwargs):
    channel = kwargs["channel"]
    ctx : discord.Client = kwargs["ctx"]
    await channel.send(f"Pong! {round(ctx.latency * 1000)}ms")