def giveaway(giveaway_id, author, channel, original_message, winners, prize):
    schema = {
        "giveawayId": f"{giveaway_id}",
        "author": f"{author.id}",
        "channel": f"{channel}",
        "message": f"{original_message}",
        "winners": f"{winners}",
        "prize": f"{prize}",
        "users": [f"{author.id}"]
    }
    return schema