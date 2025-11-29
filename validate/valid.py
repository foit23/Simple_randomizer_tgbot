import dotenv
import os

dotenv.load_dotenv("validate/token.env")
TOKEN = os.getenv("TOKEN")
print(TOKEN)