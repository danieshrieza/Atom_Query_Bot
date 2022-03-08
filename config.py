import json

# NOTE : Open json file
with open("env.json") as env:
    
    # NOTE : Load json file that contains private info about the bot
    priv=json.load(env)
    
    # NOTE : Get the bot token from json file
    TOKEN=str(priv["MATH_VAR"])
    
    # NOTE : Get the guild id from json file
    GUILD_ID=int(priv["GUILD_VAR"])

    # NOTE : Get the owner id from json file
    OWNER_ID=int(priv["OWNER_VAR"])
