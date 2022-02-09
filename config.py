import os
from dotenv.main import load_dotenv

# NOTE : Load .env file for token and testing guild id
load_dotenv()

# NOTE : Get the guild id from .env file
GUILD_ID = int(os.getenv("GUILD_VAR", ""))

# NOTE : Get the bot token from .env file
TOKEN = os.getenv("MATH_VAR", "")

# NOTE : Get the owner id from .env file
OWNER_ID = int(os.getenv("OWNER_VAR", ""))
