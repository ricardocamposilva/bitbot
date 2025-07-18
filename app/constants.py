import os

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

ALPHAVANTAGE_BASE_URL="https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY=os.getenv('ALPHAVANTAGE_API_KEY', 'dummy_key')

