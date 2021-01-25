import random

from Database.db_utils import get_all_giveaway_users

async def draw_winner(giveaway_id, winners):
    all_users = get_all_giveaway_users(giveaway_id)
    if "x" in all_users:
        all_users.remove("x")
    choosen = random.sample(all_users, winners)
    return ["<@!%s>" % (winner) for winner in choosen]
