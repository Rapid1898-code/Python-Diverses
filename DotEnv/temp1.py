from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())
GMAIL_TOKEN = os.environ.get("GMAIL_TOKEN")