import discord
from discord.ext import commands

from Database.db_utils import add_user_to_giveaway, get_all_giveaway_users

from Database.db_connector import db_connection
from Config.config import DB_PASS


db = db_connection(DB_PASS)

class event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        message_id = reaction.message.id
        ids = []
        if str(user.id) == str(self.bot.user.id):
            return
        for x in db.giveaways.find():
            ids.append(x["giveawayId"].split("-")[0])
        if not str(message_id) in ids:
            return
        else:
            giveaway_id = f"{message_id}-{reaction.message.channel.id}"
            await add_user_to_giveaway(giveaway_id, user.id)

def setup(bot):
    bot.add_cog(event(bot))