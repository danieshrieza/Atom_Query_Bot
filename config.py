import os
from dotenv.main import load_dotenv

# <--- Load .env file for token and testing guild id --->
load_dotenv()

# <--- Get the guild id from .env file --->
guild_var = os.getenv("GUILD_VAR", "")

guild_id = int(guild_var)

# <--- Get the bot token from .env file --->
token = os.getenv("MATH_VAR", "")