from Database.db_connector import db_connection
from Config.config import DB_PASS


giveaways = db_connection(DB_PASS).giveaways



def get_all_giveaway_users(giveaway_id):
    try:
        raw = giveaways.find({"giveawayId": f"{giveaway_id}"})
        for key in raw:
            return key["users"]
    except Exception as e:
        print("Error while fetching users: {}".format(e))

async def create_giveaway(schema):
    try:
        giveaways.insert_one(schema)
    except Exception as e:
        print("Error while creating a new giveaway: {}".format(e))


async def add_user_to_giveaway(giveaway_id, user):
    try:
        users = get_all_giveaway_users(giveaway_id)
        if str(user) in users or user in users:
            return
        global new_users
        new_users = []
        if users == None:
            new_users.append("x")
            new_users.append(user)
        else:
            new_users.append(user)
            new_users.extend(users)
        giveaways.update({"giveawayId": f"{giveaway_id}"}, {"$set": {"users": new_users}}, upsert=False, multi=False)
    except Exception as e:
        print("Error while adding user {} to giveaway {}: {}".format(user, giveaway_id, e))



async def delete_giveaway(giveaway_id):
    try:
        giveaways.delete_one({"giveawayId": f"{giveaway_id}"})
    except Exception as e:
        print("Error while deleting giveaway {}: {}".format(giveaway_id, e))
    