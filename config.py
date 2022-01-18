import os
from dotenv.main import load_dotenv

load_dotenv()

guild_id = int(os.getenv("GUILD_VAR", ""))

token = os.getenv("MATH_VAR", "")