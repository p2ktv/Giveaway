def start(client, cogs, commands):
    removed_commands = 0
    loaded_cogs = 0
    for cmd in commands:
        try:
            client.remove_command(cmd)
            removed_commands += 1
            print("Removed {}!".format(cmd))
        except Exception as command_removal_error:
            print("Error while removing command {}: {}".format(cmd, command_removal_error))
    
    for cog in cogs:
        try:
            client.load_extension("Cogs." + cog)
            loaded_cogs += 1
            print("Loaded {}!".format(cog))
        except Exception as cog_error:
            print("Error while loading cog {}: {}".format(cog, cog_error))
            pass
    
    print("Removed {}/{} commands & loaded {}/{} cogs! \n\nReady as {} ({})".format(removed_commands, len(commands), loaded_cogs, len(cogs), client.user, client.user.id))