import discord
from discord.ext import commands
from discord.ext.commands import Bot

from Config.start import *
from Config.config import cogs, to_remove_commands, TOKEN


client: Bot = commands.Bot(command_prefix=PREFIX)

discord.Intents().default()


@client.event
async def on_ready():
    start(client, cogs, to_remove_commands)
    pass


client.run(TOKEN)
