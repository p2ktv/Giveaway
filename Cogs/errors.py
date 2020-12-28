import discord
from discord.ext import commands


class errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("``Type Error``")
            return
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("``Missing Perms``")
            return

def setup(bot):
    bot.add_cog(errors(bot))