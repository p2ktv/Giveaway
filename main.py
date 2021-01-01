import discord
from discord.ext import commands
from discord.ext.commands import Bot

from Config.start import * #wildcard import entire config file
from Config.config import cogs, to_remove_commands, TOKEN


client: Bot = commands.Bot(command_prefix=PREFIX) #actual client

discord.Intents().default() # activation intents


@client.event
async def on_ready():
    start(client, cogs, to_remove_commands) #init bot -> load cogs & remove cmds
    pass


client.run(TOKEN) #run client
