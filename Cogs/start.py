import discord
from discord.ext import commands
import datetime
import asyncio

from Types.types import Prize, Time, Winners

from Database.db_connector import db_connection
from Config.config import DB_PASS

from Database.db_utils import create_giveaway, delete_giveaway, get_all_giveaway_users

from Schemas.schemas import giveaway

from Utils.embed_builder import build_giveaway_embed, edit_giveaway_embed_normal, edit_giveaway_embed_fail, edit_giveaway_embed_win
from Utils.giveaway_utils import draw_winner



db = db_connection(DB_PASS)

class start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def start(self, ctx, time: Time = None, winners: Winners = None, *, prize: Prize = None):
        if time == None:
            await ctx.send("``Missing arg: time``")
            return
        if winners == None:
            await ctx.send("``Missing arg: winners``")
            return
        if prize == None:
            await ctx.send("``Missing arg: prize``")
            return
        try:
            ending = datetime.datetime.now() + datetime.timedelta(hours=time)
            embed = await build_giveaway_embed(time, winners, prize, ctx.message.author.id, ending)
            giveaway_message = await ctx.send(embed=embed)

            giveaway_id = f"{giveaway_message.id}-{ctx.message.channel.id}"
            schema = giveaway(giveaway_id, ctx.message.author, ctx.message.channel.id, ctx.message.id, winners, prize)
            await create_giveaway(schema)

            await giveaway_message.add_reaction('🎉')

            time_left = time

            while time_left > 0:
                time_left -= 1
                await asyncio.sleep(3600)
                new_embed = await edit_giveaway_embed_normal(time_left, winners, prize, ctx.message.author.id, ending)
                await giveaway_message.edit(embed=new_embed)
                if time_left <= 0:
                    break
            
            all_users = get_all_giveaway_users(giveaway_id)

            if "x" in all_users:
                all_users.remove("x")

            if all_users == None or len(all_users) < (winners + 1):
                await ctx.send("Sorry, but a winner could not be determinated. (Not enough attendees) \n{}".format(giveaway_message.jump_url))
                fail_embed = await edit_giveaway_embed_fail(prize, len(all_users), winners)
                await giveaway_message.clear_reactions()
                await giveaway_message.edit(embed=fail_embed)
                await delete_giveaway(giveaway_id)
                return
            
            winner = await draw_winner(giveaway_id, winners)
            win_msg = await ctx.send("🎉 Congrats {}, you won **{}**".format(", ".join(winner), prize))
            await giveaway_message.clear_reactions()
            winner_embed = await edit_giveaway_embed_win(prize, winners, ending, win_msg)
            await giveaway_message.edit(embed=winner_embed)
            await delete_giveaway(giveaway_id)
        except Exception as error:
            print(error)



def setup(bot):
    bot.add_cog(start(bot))