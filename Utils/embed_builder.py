import discord

async def build_giveaway_embed(time, winners, prize, host, end_time):
    giveaway_embed = discord.Embed(color=0x2f3136, description="React with 🎉 to enter! \nTime remaining: **{}** hours \nHosted by <@!{}>".format(time, host), timestamp=end_time)
    giveaway_embed.set_author(name="{}".format(prize))
    giveaway_embed.set_footer(text="{} Winners | Ends at".format(winners))
    return giveaway_embed


async def edit_giveaway_embed_normal(time_left, winners, prize, host, end_time):
    new_giveaway_embed = discord.Embed(color=0x2f3136, description="React with 🎉 to enter! \nTime remaining: **{}** hours \nHosted by <@!{}>".format(time_left, host), timestamp=end_time)
    new_giveaway_embed.set_author(name="{}".format(prize))
    new_giveaway_embed.set_footer(text="{} Winners | Ends at".format(winners))
    return new_giveaway_embed


async def edit_giveaway_embed_fail(prize, users, winners):
    new_giveaway_embed = discord.Embed(color=0x2f3136, description="Giveaway has been canceled! \nNot enough attendees ({}/{})".format(users, (winners + 1)))
    new_giveaway_embed.set_author(name="{}".format(prize))
    return new_giveaway_embed


async def edit_giveaway_embed_win(prize, winners, end_time, win_msg):
    new_giveaway_embed = discord.Embed(color=0x2f3136, description="Giveaway has ended! Winner(s): {}".format(win_msg.jump_url), timestamp=end_time)
    new_giveaway_embed.set_author(name="{}".format(prize))
    new_giveaway_embed.set_footer(text="{} Winners | Ended at".format(winners))
    return new_giveaway_embed