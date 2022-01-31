import os
from dotenv.main import load_dotenv

# NOTE : Load .env file for token and testing guild id
load_dotenv(dotenv_path="/private")

# NOTE : Get the guild id from .env file
guild_id = int(os.getenv("GUILD_VAR", ""))

# NOTE : Get the bot token from .env file
token = os.getenv("MATH_VAR", "")

# NOTE : Get the owner id from .env file
owner_id = int(os.getenv("OWNER_VAR", ""))
